import json, re, os
from concurrent.futures import ThreadPoolExecutor, as_completed
import urllib.request

DATA_FILE = 'C:\\Users\\Student\\Desktop\\summer-school\\skins_data.json'
OUT_FILE = 'C:\\Users\\Student\\Desktop\\summer-school\\skins_detail.json'

with open(DATA_FILE) as f:
    data = json.load(f)

skins = []
for wn, sn, url, r in data['all']:
    if 'raw.githubusercontent' in url:
        url = url.replace('/330x192', '')
    skins.append((wn, sn, url, r))

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
    return ''.join(c for c in s if c.isalnum() or c == '-')

def extract_text(html):
    main = re.search(r'<main[^>]*>(.*?)</main>', html, re.DOTALL)
    if not main:
        return ''
    text = main.group(1)
    text = re.sub(r'<script[^>]*>.*?</script>', '', text, flags=re.DOTALL)
    text = re.sub(r'<style[^>]*>.*?</style>', '', text, flags=re.DOTALL)
    text = re.sub(r'<[^>]+>', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def fetch_skin(wn, sn):
    slug = slugify(wn, sn)
    try:
        req = urllib.request.Request(f'https://csgoskins.gg/items/{slug}',
            headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='replace')
    except Exception:
        return slug, None
    
    text = extract_text(html)
    if len(text) < 500:
        return slug, None
    
    result = {}
    
    # Description - get first substantial paragraph (after weapon intro)
    dp = re.search(r'(?:rifle|pistol|smg|shotgun|machine gun|knife|glove)[^.]+\.\s*(.{100,800})', text, re.IGNORECASE)
    if dp:
        desc = dp.group(1).strip()
        if len(desc) < 30:
            # Fallback: get any 100-600 char block
            dp = re.search(r'(.{100,600})', text)
            if dp: desc = dp.group(1).strip()
        result['description'] = desc[:500]
    else:
        dp = re.search(r'(.{100,600})', text)
        if dp: result['description'] = dp.group(1).strip()[:500]
    
    # Specific field extraction
    patterns = {
        'weapon': r'Weapon\s+(\S[^\n]{1,40}?)(?=\s{2,}|\s*(Finish|Rarity|Popularity|Designer|Released|Model|Pattern|Collection|Container))',
        'finish': r'Finish\s+(\S[^\n]{1,40}?)(?=\s{2,}|\s*(Finish|Rarity|Popularity|Designer|Released|Model|Pattern|Collection|Container|Style))',
        'finish_style': r'Finish Style\s+(\S[^\n]{1,40}?)(?=\s{2,}|\s*(Finish|Rarity|Popularity|Designer|Released|Model|Pattern|Collection|Container))',
        'designer': r'Designer\s+([^\n]{1,40}?)(?=\s{2,}|\s*(Workshop|Released|Update|Rarity))',
    }
    
    for key, pat in patterns.items():
        m = re.search(pat, text)
        if m:
            result[key] = m.group(1).strip()
    
    # Rarity
    m = re.search(r'(?:Rarity|Item Class Rarity)\s+(Covert|Classified|Restricted|Mil-Spec|Mil-Spec Grade|Industrial Grade|Consumer Grade|Extraordinary|Contraband)', text, re.IGNORECASE)
    if m:
        result['rarity'] = m.group(1)
    
    # Popularity
    m = re.search(r'Popularity\s+(\d+)%', text)
    if m:
        result['popularity'] = m.group(1) + '%'
    
    # Release date
    m = re.search(r'Released\s+([A-Z][a-z]+ \d{1,2}[a-z]{2},? \d{4})', text)
    if m:
        result['released'] = m.group(1)
    else:
        m = re.search(r'Released\s+(\d+ \w+ \w+[\s\w]*ago)', text)
        if m:
            result['released'] = m.group(1)
    
    # Update
    m = re.search(r'Update\s+"([^"]+)"', text)
    if m:
        result['update'] = m.group(1)
    
    # Collection
    m = re.search(r'Collection\s+([A-Z][A-Za-z\s&-]+?)(?:\s+\d+\s+items?)?(?:\s{2,}|\s*\n)', text)
    if m:
        result['collection'] = m.group(1).strip()
        ci = re.search(rf'{re.escape(m.group(1).strip())}.*?collections/([a-f0-9]+)\.[a-z]+', html)
        if not ci:
            ci = re.search(r'collections/([a-f0-9]+)\.[a-z]+', html)
        if ci:
            result['collection_img'] = f'https://cdn.csgoskins.gg/public/images/collections/{ci.group(1)}.png'
    
    # Container
    m = re.search(r'(?:Containers?|Obtained from)\s+([A-Z][A-Za-z\s&-]+?(?:Case|Package|Container|Collection|Box|Capsule))(?:\s|$)', text)
    if m:
        result['container'] = m.group(1).strip()
    
    # Float range
    m = re.search(r'(?:wear range|ranges from)\s+([\d.]+)\s+to\s+([\d.]+)', text, re.IGNORECASE)
    if m:
        result['float_min'] = m.group(1)
        result['float_max'] = m.group(2)
    
    # Exteriors
    m = re.search(r'available in\s+(.+?)(?:\.\s|For each|$)', text, re.IGNORECASE)
    if m:
        result['exteriors'] = m.group(1).strip()
    
    # Rating
    m = re.search(r'(\d+\.?\d*)\s*out of\s*5\s*([\d,.]+[KM]?)\s*Votes?', text)
    if m:
        result['rating'] = m.group(1)
        result['votes'] = m.group(2)
    
    # Pro players
    m = re.search(r'(?:Professional CS2 players?|Used by)\s+(.+?)(?:\s{3,}|$)', text)
    if m:
        result['pro_players'] = m.group(1).strip()[:200]
    
    return slug, result if len(result) > 1 else None

# Load existing
existing = {}
if os.path.exists(OUT_FILE):
    with open(OUT_FILE) as f:
        existing = json.load(f)
    print(f"Loaded {len(existing)} existing results")

to_fetch = [(wn, sn) for wn, sn, _, _ in unique if slugify(wn, sn) not in existing]
print(f"Need to fetch {len(to_fetch)} skins")

done = 0
total = len(to_fetch)
batch = []
save_every = 200

with ThreadPoolExecutor(max_workers=8) as executor:
    futures = {executor.submit(fetch_skin, wn, sn): (wn, sn) for wn, sn in to_fetch}
    for future in as_completed(futures):
        try:
            slug, result = future.result()
            if result:
                existing[slug] = result
            done += 1
            if done % 50 == 0:
                print(f"  {done}/{total} ({len(existing)} with data)")
            if done % save_every == 0:
                with open(OUT_FILE, 'w') as f:
                    json.dump(existing, f)
                print(f"  Saved {len(existing)} results")
        except Exception as e:
            done += 1
            if done % 100 == 0: print(f"  {done}/{total} (error: {e})")

with open(OUT_FILE, 'w') as f:
    json.dump(existing, f)

print(f"\nDone! {len(existing)} skins with detail data saved")
