import json, re, os
from concurrent.futures import ThreadPoolExecutor, as_completed
import urllib.request
import urllib.error

DATA_FILE = 'C:\\Users\\Student\\Desktop\\summer-school\\skins_data.json'
OUT_FILE = 'C:\\Users\\Student\\Desktop\\summer-school\\skins_detail.json'

with open(DATA_FILE) as f:
    data = json.load(f)

skins = []
for wn, sn, url, r in data['all']:
    if 'raw.githubusercontent' in url:
        url = url.replace('/330x192', '')
    skins.append((wn, sn, url, r))

# Remove duplicates by (wn, sn)
seen = set()
unique = []
for wn, sn, url, r in skins:
    key = (wn.lower(), sn.lower())
    if key not in seen:
        seen.add(key)
        unique.append((wn, sn, url, r))

print(f"Total unique skins: {len(unique)}")

def slugify(wn, sn):
    s = f'{wn} {sn}'.lower()
    s = re.sub(r'[|&]', '', s)
    s = re.sub(r'\s+', '-', s)
    s = re.sub(r'[^a-z0-9-]', '', s)
    return s

def fetch_skin(wn, sn):
    slug = slugify(wn, sn)
    try:
        req = urllib.request.Request(f'https://csgoskins.gg/items/{slug}',
            headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='replace')
    except Exception:
        return None
    
    # Extract text between <main> tags
    main = re.search(r'<main[^>]*>(.*?)</main>', html, re.DOTALL)
    if not main:
        return None
    text = main.group(1)
    text = re.sub(r'<script[^>]*>.*?</script>', '', text, flags=re.DOTALL)
    text = re.sub(r'<style[^>]*>.*?</style>', '', text, flags=re.DOTALL)
    text = re.sub(r'<[^>]+>', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    
    result = {}
    
    # Description - first paragraph
    desc_match = re.search(r'Powerful and reliable.*?limit', text, re.IGNORECASE)
    if not desc_match:
        desc_match = re.search(r'(.{100,600}?)(?=\s{2,}|\s{3,})', text)
    if desc_match:
        result['description'] = desc_match.group(0).strip()[:500]
    
    # Rarity
    r_match = re.search(r'Rarity\s+(Covert|Classified|Restricted|Mil-Spec|Industrial Grade|Consumer Grade|Extraordinary|Contraband)', text, re.IGNORECASE)
    if r_match:
        result['rarity'] = r_match.group(1)
    
    # Weapon
    wp_match = re.search(r'Weapon\s+(.+)', text)
    if wp_match:
        result['weapon'] = wp_match.group(1).strip().split()[0]
    
    # Finish
    f_match = re.search(r'Finish\s+(.+?)(?=\s{2,}|\s+Finish|\s+Pattern)', text)
    if f_match:
        result['finish'] = f_match.group(1).strip()
    
    # Finish Style
    fs_match = re.search(r'Finish Style\s+(.+?)(?=\s{2,}|\s+Finish|\s+Pattern|\s+Model)', text)
    if fs_match:
        result['finish_style'] = fs_match.group(1).strip()
    
    # Designer
    d_match = re.search(r'Designer\s+(.+?)(?=\s{2,}|\s+Workshop|\s+Released)', text)
    if d_match:
        result['designer'] = d_match.group(1).strip()
    
    # Released
    rel_match = re.search(r'Released\s+(.+?)(?=\s{2,}|\s+Update)', text)
    if rel_match:
        result['released'] = rel_match.group(1).strip()
    
    # Update  
    upd_match = re.search(r'Update\s+"([^"]+)"', text)
    if upd_match:
        result['update'] = upd_match.group(1)
    
    # Popularity
    pop_match = re.search(r'Popularity\s+(\d+)%', text)
    if pop_match:
        result['popularity'] = pop_match.group(1) + '%'
    
    # Collection
    col_match = re.search(r'Collection\s+(.+?)(?:\s+\d+\s+items?)', text)
    if col_match:
        result['collection'] = col_match.group(1).strip()
        # Collection image
        ci_match = re.search(r'collections/([a-f0-9]+)\.[a-z]+', html)
        if ci_match:
            result['collection_img'] = f'https://cdn.csgoskins.gg/public/images/collections/{ci_match.group(1)}.png'
    
    # Container
    cont_match = re.search(r'Containers?\s+(.+?)(?:\s{2,}|\s+Weapon Case)', text)
    if cont_match:
        result['container'] = cont_match.group(1).strip()
    
    # Float range
    fr_match = re.search(r'float value.*?ranges from\s+([\d.]+)\s+to\s+([\d.]+)', text, re.IGNORECASE)
    if fr_match:
        result['float_min'] = fr_match.group(1)
        result['float_max'] = fr_match.group(2)
    
    # Exteriors
    ext_match = re.search(r'available in\s+(.+?)(?:\.|For each)', text, re.IGNORECASE)
    if ext_match:
        result['exteriors'] = ext_match.group(1).strip()
    
    # Community rating
    cr_match = re.search(r'(\d+\.?\d*)\s*out of\s*5\s*([\d.]+[KM]?)\s*Votes?', text)
    if cr_match:
        result['rating'] = cr_match.group(1)
        result['votes'] = cr_match.group(2)
    
    # Pro players
    pp_match = re.search(r'Professional CS2 players?\s+(.+)', text)
    if pp_match:
        result['pro_players'] = pp_match.group(1).strip()[:200]
    
    return result

# Fetch in parallel
results = {}
done = 0
total = len(unique)

print(f"Fetching {total} skins...")
# Load existing results if any
if os.path.exists(OUT_FILE):
    with open(OUT_FILE) as f:
        results = json.load(f)
    print(f"Loaded {len(results)} existing results")

to_fetch = [(wn, sn) for wn, sn, _, _ in unique if slugify(wn, sn) not in results]

print(f"Need to fetch {len(to_fetch)} skins")

with ThreadPoolExecutor(max_workers=10) as executor:
    futures = {executor.submit(fetch_skin, wn, sn): (wn, sn) for wn, sn in to_fetch}
    for future in as_completed(futures):
        wn, sn = futures[future]
        try:
            result = future.result()
            slug = slugify(wn, sn)
            if result:
                results[slug] = result
            done += 1
            if done % 100 == 0:
                print(f"  {done}/{len(to_fetch)} ({len(results)} with data)")
                # Save periodically
                with open(OUT_FILE, 'w') as f:
                    json.dump(results, f)
        except Exception as e:
            done += 1

# Final save
with open(OUT_FILE, 'w') as f:
    json.dump(results, f)

print(f"\nDone! {len(results)} skins with detail data saved to skins_detail.json")
