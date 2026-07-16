import json, os

with open(os.path.join(os.path.dirname(__file__), 'skins_data.json')) as f:
    raw = json.load(f)

all_skins = raw['all']

fixed = []
for wn, sn, url, r in all_skins:
    if 'raw.githubusercontent' in url:
        url = url.replace('/330x192', '')
    fixed.append((wn, sn, url, r))
all_skins = fixed

ra_info = {
    'Covert': ('covert', '#eb4b4b', 'rgba(235,75,75,0.12)'),
    'Classified': ('classified', '#d32ce6', 'rgba(211,44,230,0.12)'),
    'Restricted': ('restricted', '#8847ff', 'rgba(136,71,255,0.12)'),
    'Mil-Spec Grade': ('milspec', '#4b69ff', 'rgba(75,105,255,0.12)'),
    'Industrial Grade': ('industrial', '#5e98d9', 'rgba(94,152,217,0.12)'),
    'Consumer Grade': ('consumer', '#b0b0b0', 'rgba(176,176,176,0.12)'),
    'Extraordinary': ('knife', '#ffd700', 'rgba(255,215,0,0.12)'),
}
r_order = {'Covert':0,'Classified':1,'Restricted':2,'Mil-Spec Grade':3,'Industrial Grade':4,'Consumer Grade':5,'Extraordinary':0}

categories = [
    ('rifles', 'Rifles', ['ak-47','m4a4','m4a1-s','awp','ssg 08','sg 553','aug','famas','galil ar','scar-20','g3sg1']),
    ('pistols', 'Pistols', ['desert eagle','usp-s','glock-18','p2000','p250','cz75-auto','five-seven','tec-9','dual berettas','r8 revolver']),
    ('smgs', 'SMGs', ['mac-10','mp9','mp5-sd','mp7','ump-45','p90','pp-bizon']),
    ('heavies', 'Heavy', ['mag-7','nova','xm1014','sawed-off','m249','negev']),
    ('knives', 'Knives', ['karambit','butterfly knife','m9 bayonet','talon knife','bayonet','flip knife','shadow daggers','bowie knife','stiletto knife','ursus knife','nomad knife','skeleton knife','classic knife','gut knife','huntsman knife','falchion knife','navaja knife','paracord knife','survival knife','kukri knife']),
    ('gloves', 'Gloves', ['hand wraps','sport gloves','moto gloves','driver gloves','specialist gloves','bloodhound gloves','broken fang gloves','hydra gloves']),
]

weapon_display = {
    'ak-47':'AK-47','m4a4':'M4A4','m4a1-s':'M4A1-S','awp':'AWP','ssg 08':'SSG 08',
    'sg 553':'SG 553','aug':'AUG','famas':'FAMAS','galil ar':'Galil AR','scar-20':'SCAR-20','g3sg1':'G3SG1',
    'desert eagle':'Deagle','usp-s':'USP-S','glock-18':'Glock','p2000':'P2000','p250':'P250',
    'cz75-auto':'CZ75','five-seven':'Five-SeveN','tec-9':'Tec-9','dual berettas':'Dualies','r8 revolver':'R8',
    'mac-10':'MAC-10','mp9':'MP9','mp5-sd':'MP5-SD','mp7':'MP7','ump-45':'UMP-45','p90':'P90','pp-bizon':'PP-Bizon',
    'mag-7':'MAG-7','nova':'Nova','xm1014':'XM1014','sawed-off':'Sawed-Off','m249':'M249','negev':'Negev',
    'karambit':'Karambit','butterfly knife':'Butterfly','m9 bayonet':'M9 Bayonet','talon knife':'Talon',
    'bayonet':'Bayonet','flip knife':'Flip','shadow daggers':'Shadow D.','bowie knife':'Bowie',
    'stiletto knife':'Stiletto','ursus knife':'Ursus','nomad knife':'Nomad','skeleton knife':'Skeleton',
    'classic knife':'Classic','gut knife':'Gut','huntsman knife':'Huntsman','falchion knife':'Falchion',
    'navaja knife':'Navaja','paracord knife':'Paracord','survival knife':'Survival','kukri knife':'Kukri',
    'hand wraps':'Hand Wraps','sport gloves':'Sport','moto gloves':'Moto','driver gloves':'Driver',
    'specialist gloves':'Specialist','bloodhound gloves':'Bloodhound','broken fang gloves':'Broken Fang','hydra gloves':'Hydra'
}

total = len(all_skins)

cat_data = {}
cat_wp_list = {}
for sid, title, wp_list in categories:
    group = []
    wp_map = {}
    for wl in wp_list:
        wp_map[wl] = []
    for wn, sn, url, r in all_skins:
        wl = wn.lower()
        if wl in wp_map:
            wp_map[wl].append((wn, sn, url, r))
    for wl in wp_list:
        wp_map[wl].sort(key=lambda x: (r_order.get(x[3], 99), x[1]))
        group.extend(wp_map[wl])
    cat_data[sid] = group

def card_html(wn, sn, url, r):
    cls, hex, bg = ra_info.get(r, ('milspec', '#4b69ff', 'rgba(75,105,255,0.12)'))
    rup = r.upper()
    wep = wn.lower().replace("'", "&apos;")
    nm = (wn + ' | ' + sn).lower()
    return ('<div class="card" data-w="{w}" data-r="{rar}" data-n="{nm}">'
            '<div class="card-shine"></div>'
            '<div class="card-img"><img src="{u}" alt="{wn} {sn}" loading="lazy"></div>'
            '<div class="card-body">'
            '<span class="card-rarity" style="color:{h}">{rup}</span>'
            '<h3 class="card-name">{wn}<br>{sn}</h3>'
            '</div></div>').format(c=cls, w=wep, rar=r, nm=nm, u=url, wn=wn, sn=sn, h=hex, rup=rup)

cat_counts = {}
for sid, title, wp_list in categories:
    cat_counts[sid] = len(cat_data[sid])

lines = []
def L(s): lines.append(s)

L('<!DOCTYPE html><html lang="en"><head>')
L('<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">')
L('<title>CS2 Skin Vault \u2014 Complete Armory</title>')
L('<link rel="preconnect" href="https://fonts.googleapis.com">')
L('<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>')
L('<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Orbitron:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">')
L('<style>')
L('*{box-sizing:border-box;margin:0;padding:0}')
L('html{scroll-behavior:smooth}')
L('body{font-family:"Inter",-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;-webkit-font-smoothing:antialiased;background:#050508;color:#e0e0e0;line-height:1.5}')
L('.f{font-family:"Orbitron",sans-serif}')
L(':root{--c1:#eb4b4b;--c2:#d32ce6;--c3:#8847ff;--c4:#4b69ff;--c5:#5e98d9;--c6:#b0b0b0;--c7:#ffd700;--bg:#050508;--bg2:#0b0b12;--bg3:#111120}')
L('')
L('.hero{background:linear-gradient(160deg,#050508,#0b0b12,#111120);position:relative;overflow:hidden;min-height:50vh;display:flex;align-items:center;padding-top:64px}')
L('.hero::before{content:"";position:absolute;inset:0;background:radial-gradient(ellipse at 30% 50%,rgba(235,75,75,0.06) 0%,transparent 70%),radial-gradient(ellipse at 70% 50%,rgba(136,71,255,0.04) 0%,transparent 60%);pointer-events:none}')
L('.hero-glow{position:absolute;width:500px;height:500px;border-radius:50%;background:radial-gradient(circle,rgba(235,75,75,0.04) 0%,transparent 70%);top:-200px;left:50%;transform:translateX(-50%);pointer-events:none}')
L('')
L('.nav{background:rgba(5,5,8,0.9);backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);border-bottom:1px solid rgba(255,255,255,0.04);position:fixed;top:0;left:0;width:100%;z-index:100;height:64px}')
L('.nav-in{max-width:1400px;margin:0 auto;padding:0 24px;height:100%;display:flex;align-items:center;justify-content:space-between}')
L('.nav-l{display:flex;align-items:center;gap:8px}')
L('.nav-logo{width:32px;height:32px;border-radius:8px;background:var(--c1);display:flex;align-items:center;justify-content:center;color:#fff;font-size:12px;font-weight:900;font-family:"Orbitron",sans-serif}')
L('.nav-title{font-family:"Orbitron",sans-serif;font-size:14px;font-weight:700;color:#fff;letter-spacing:.5px}')
L('.nav-badge{padding:2px 8px;border-radius:4px;background:rgba(255,255,255,0.04);font-size:9px;color:#666;font-weight:600;letter-spacing:.5px;text-transform:uppercase;border:1px solid rgba(255,255,255,0.04)}')
L('.nav-links{display:none;gap:24px}')
L('@media(min-width:768px){.nav-links{display:flex}}')
L('.nav-links a{color:#666;font-size:13px;font-weight:500;text-decoration:none;transition:color .2s}')
L('.nav-links a:hover{color:#fff}')
L('.nav-links a.active{color:var(--c1)}')
L('')
L('.search-section{background:var(--bg2);border-bottom:1px solid rgba(255,255,255,0.04);position:sticky;top:64px;z-index:50;padding:16px 0}')
L('.search-in{max-width:1400px;margin:0 auto;padding:0 24px}')
L('.search-wrap{position:relative;margin-bottom:12px}')
L('.search-wrap svg{position:absolute;left:14px;top:50%;transform:translateY(-50%);color:#444}')
L('.search-wrap input{width:100%;padding:14px 14px 14px 44px;border-radius:10px;border:1px solid rgba(255,255,255,0.06);background:rgba(255,255,255,0.03);color:#fff;font-size:14px;outline:none;transition:border .2s}')
L('.search-wrap input:focus{border-color:var(--c1)}')
L('.search-wrap input::placeholder{color:#444}')
L('.filters{display:flex;flex-wrap:wrap;align-items:center;gap:5px}')
L('.filters .l{color:#444;font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.5px;margin-right:4px;min-width:45px}')
L('.fb{padding:5px 13px;border-radius:20px;border:1px solid rgba(255,255,255,0.06);background:transparent;font-size:11px;font-weight:500;cursor:pointer;transition:all .2s;color:#aaa}')
L('.fb:hover{border-color:rgba(255,255,255,0.15);color:#ddd}')
L('.fb.off{opacity:.15;text-decoration:line-through;pointer-events:none}')
L('.fb.off:hover{opacity:.2}')
L('.fb-reset{border-color:rgba(235,75,75,0.3);color:var(--c1);font-weight:600}')
L('.fb-reset:hover{background:rgba(235,75,75,0.08);border-color:rgba(235,75,75,0.5)}')
L('')
L('.stats{background:var(--bg2);border-bottom:1px solid rgba(255,255,255,0.04);padding:14px 0}')
L('.stats-in{max-width:1400px;margin:0 auto;padding:0 24px;display:grid;grid-template-columns:repeat(2,1fr);gap:8px;text-align:center}')
L('@media(min-width:640px){.stats-in{grid-template-columns:repeat(4,1fr)}}')
L('.stat-num{font-size:20px;font-weight:800;color:#fff;font-family:"Orbitron",sans-serif}')
L('.stat-lbl{font-size:11px;color:#555;margin-top:2px}')
L('')
L('.main{max-width:1400px;margin:0 auto;padding:24px}')
L('')
L('.section{margin-bottom:32px}')
L('.section-h{display:flex;align-items:center;justify-content:space-between;margin-bottom:16px;padding-bottom:12px;border-bottom:1px solid rgba(255,255,255,0.04)}')
L('.section-h-l{display:flex;align-items:center;gap:10px}')
L('.section-icon{width:28px;height:28px;border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:14px}')
L('.section-title{font-size:18px;font-weight:700;color:#fff;font-family:"Orbitron",sans-serif;letter-spacing:.3px}')
L('.section-count{font-size:12px;color:#555;font-weight:500}')
L('.section.hidden{display:none}')
L('')
L('.grid{display:grid;grid-template-columns:repeat(2,1fr);gap:10px}')
L('@media(min-width:540px){.grid{grid-template-columns:repeat(3,1fr)}}')
L('@media(min-width:768px){.grid{grid-template-columns:repeat(4,1fr)}}')
L('@media(min-width:1024px){.grid{grid-template-columns:repeat(5,1fr)}}')
L('@media(min-width:1280px){.grid{grid-template-columns:repeat(6,1fr)}}')
L('')
L('.card{background:var(--bg2);border-radius:10px;overflow:hidden;border:1px solid rgba(255,255,255,0.04);transition:all .3s;cursor:pointer;position:relative}')
L('.card:hover{transform:translateY(-4px);border-color:rgba(255,255,255,0.1);box-shadow:0 12px 40px rgba(0,0,0,.4)}')
L('.card.hidden{display:none!important}')
L('.card-shine{position:absolute;top:-50%;left:-50%;width:200%;height:200%;background:linear-gradient(45deg,transparent 20%,rgba(255,255,255,0.02) 50%,transparent 80%);transform:rotate(25deg);opacity:0;transition:opacity .5s;pointer-events:none;z-index:1}')
L('.card:hover .card-shine{opacity:1;animation:sh 1s ease-in-out}')
L('@keyframes sh{0%{transform:translateX(-100%) rotate(25deg)}100%{transform:translateX(100%) rotate(25deg)}}')
L('.card-img{background:linear-gradient(180deg,rgba(255,255,255,0.02),transparent);display:flex;align-items:center;justify-content:center;padding:12px;aspect-ratio:16/9}')
L('.card-img img{width:100%;height:100%;object-fit:contain;transition:transform .4s;filter:drop-shadow(0 4px 12px rgba(0,0,0,.5))}')
L('.card:hover .card-img img{transform:scale(1.06)}')
L('.card-body{padding:10px 12px 12px}')
L('.card-rarity{font-size:9px;font-weight:700;letter-spacing:.5px;text-transform:uppercase}')
L('.card-name{color:#fff;font-size:11px;font-weight:600;line-height:1.4;margin-top:3px}')
L('')
L('.ft{background:var(--bg2);border-top:1px solid rgba(255,255,255,0.04);padding:32px 24px;text-align:center}')
L('.ft p{color:#444;font-size:12px;line-height:1.6}')
L('.ft p a{color:#666;text-decoration:none;transition:color .2s}')
L('.ft p a:hover{color:#fff}')
L('')
L('.toast{position:fixed;bottom:24px;left:50%;transform:translateX(-50%);background:rgba(235,75,75,0.15);border:1px solid rgba(235,75,75,0.3);border-radius:10px;padding:8px 20px;font-size:12px;color:var(--c1);z-index:200;opacity:0;transition:opacity .3s;pointer-events:none;backdrop-filter:blur(10px)}')
L('.toast.show{opacity:1}')
L('</style></head><body>')

# Navbar
L('<nav class="nav"><div class="nav-in"><div class="nav-l">')
L('<span class="nav-logo">CS</span><span class="nav-title">Skin Vault</span><span class="nav-badge">v2.0</span></div>')
L('<div class="nav-links">')
for sid, title, _ in categories:
    L('<a href="#s-'+sid+'">'+title+'</a>')
L('</div>')
L('<button id="mb" style="background:none;border:none;color:#666;font-size:20px;cursor:pointer;display:block;padding:4px" onclick="document.getElementById(\'mm\').classList.toggle(\'show\')">☰</button></div>')
L('<div id="mm" style="display:none;background:var(--bg2);border-top:1px solid rgba(255,255,255,0.04);padding:12px 24px;flex-direction:column;gap:8px">')
for sid, title, _ in categories:
    L('<a href="#s-'+sid+'" style="color:#666;font-size:13px;text-decoration:none;padding:4px 0" onclick="document.getElementById(\'mm\').style.display=\'none\'">'+title+'</a>')
L('</div></nav>')

# Hero
r0 = cat_data['rifles'][0] if cat_data['rifles'] else ('','','','')
r2d = [x for x in cat_data['rifles'] if 'asiimov' in x[1].lower() and 'm4a4' in x[0].lower()]
r2 = r2d[0] if r2d else (cat_data['rifles'][2] if len(cat_data['rifles'])>2 else ('','','',''))
k0 = cat_data['knives'][0] if cat_data['knives'] else ('','','','')
L('<section class="hero"><div class="hero-glow"></div>')
L('<div style="max-width:1400px;margin:0 auto;padding:60px 24px;position:relative;z-index:1;width:100%">')
L('<div style="max-width:600px">')
L('<div style="display:inline-flex;align-items:center;gap:6px;padding:4px 12px;border-radius:20px;background:rgba(235,75,75,0.08);border:1px solid rgba(235,75,75,0.15);margin-bottom:16px">')
L('<span style="width:6px;height:6px;border-radius:50%;background:var(--c1);animation:pulse 2s infinite"></span>')
L('<span style="font-size:11px;color:var(--c1);font-weight:600">Complete Armory &bull; '+str(total)+' skins</span></div>')
L('<h1 class="f" style="font-size:36px;font-weight:900;color:#fff;line-height:1.1;margin-bottom:12px">CS2<br><span style="background:linear-gradient(135deg,var(--c1),#ff8c00);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text">Skin Vault</span></h1>')
L('<p style="color:#555;font-size:14px;line-height:1.6;max-width:480px">Every weapon finish in Counter-Strike 2. Filter by rarity, weapon, or search by name.</p></div></div></section>')
L('<style>@keyframes pulse{0%,100%{opacity:1}50%{opacity:.4}}</style>')

# Stats
L('<div class="stats"><div class="stats-in">')
L('<div><div class="stat-num">'+str(total)+'+</div><div class="stat-lbl">Total Skins</div></div>')
L('<div><div class="stat-num">7</div><div class="stat-lbl">Rarity Tiers</div></div>')
L('<div><div class="stat-num">5</div><div class="stat-lbl">Wear Levels</div></div>')
L('<div><div class="stat-num" id="fc">'+str(total)+'</div><div class="stat-lbl">Showing</div></div>')
L('</div></div>')

# Search + Filters
L('<div class="search-section"><div class="search-in">')
L('<div class="search-wrap"><svg width="16" height="16" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg>')
L('<input type="text" id="gs" placeholder="Search any skin by name..." oninput="af()"></div>')
L('<div class="filters"><span class="l">Rarity</span>')
for rn in ['Covert','Classified','Restricted','Mil-Spec Grade','Industrial Grade','Consumer Grade']:
    c = {'Covert':'#eb4b4b','Classified':'#d32ce6','Restricted':'#8847ff','Mil-Spec Grade':'#4b69ff','Industrial Grade':'#5e98d9','Consumer Grade':'#b0b0b0'}[rn]
    dn = rn.replace('Mil-Spec Grade','Mil-Spec').replace('Industrial Grade','Industrial').replace('Consumer Grade','Consumer')
    L('<button class="fb fr" data-r="' + rn + '" onclick="tr(this.dataset.r)" style="color:' + c + '">' + dn + '</button>')
L('<button class="fb fb-reset" onclick="rf()">Reset</button></div>')
L('<div class="filters" style="margin-top:6px"><span class="l">Weapon</span>')

all_weps = []
seen = set()
for sid, title, wp_list in categories:
    for wl in wp_list:
        if wl not in seen:
            seen.add(wl)
            all_weps.append(wl)
for wl in all_weps:
    dn = weapon_display.get(wl, wl.title())
    L('<button class="fb fw" data-w="' + wl + '" onclick="tw(this.dataset.w)">' + dn + '</button>')
L('</div></div></div>')

# Sections
section_icons = {'rifles':'🔫','pistols':'🔫','smgs':'⚡','heavies':'💥','knives':'★','gloves':'🧤'}
section_colors = {'rifles':'#eb4b4b','pistols':'#4b69ff','smgs':'#8847ff','heavies':'#5e98d9','knives':'#ffd700','gloves':'#b8860b'}

L('<div class="main">')
for sid, title, wp_list in categories:
    group = cat_data[sid]
    icon = section_icons.get(sid, '')
    col = section_colors.get(sid, '#fff')
    cards = '\n'.join(card_html(wn, sn, url, r) for wn, sn, url, r in group)
    L('<div class="section" id="s-'+sid+'">')
    L('<div class="section-h"><div class="section-h-l"><div class="section-icon" style="background:'+col+'20;color:'+col+'">'+icon+'</div>')
    L('<span class="section-title">'+title+'</span><span class="section-count" id="sc-'+sid+'">'+str(len(group))+'</span></div></div>')
    L('<div class="grid" id="g-'+sid+'">'+cards+'</div></div>')

L('</div>')

# Footer
L('<div class="ft"><p style="margin-bottom:6px">CS2 Skin Vault &bull; '+str(total)+' weapon finishes catalogued</p>')
L('<p style="font-size:11px">Not affiliated with Valve Corporation. CS2 is a trademark of Valve.<br>Images sourced from Steam Community CDN.</p></div>')

# Toast
L('<div class="toast" id="toast"></div>')

# JS
L('<script>')
L('function af(){const s=document.getElementById("gs").value.toLowerCase().trim();')
L('const rb=document.querySelectorAll(".fr");const wb=document.querySelectorAll(".fw");')
L('const ar=new Set();rb.forEach(b=>{if(!b.classList.contains("off"))ar.add(b.dataset.r)});')
L('const aw=new Set();wb.forEach(b=>{if(!b.classList.contains("off"))aw.add(b.dataset.w)});')
L('const c=document.querySelectorAll(".card");let v=0;')
L('c.forEach(cd=>{const w=cd.dataset.w;const r=cd.dataset.r;const n=cd.dataset.n;')
L('const ms=!s||n.includes(s);const mr=ar.size===0||ar.has(r);const mw=aw.size===0||aw.has(w);')
L('if(ms&&mr&&mw){cd.classList.remove("hidden");v++}else{cd.classList.add("hidden")}});')
L('document.getElementById("fc").textContent=v;')
L('document.querySelectorAll(".section").forEach(sec=>{const g=sec.querySelector("[id^=\\"g-\\"]");')
L('if(g){const hv=g.querySelector(".card:not(.hidden)");')
L('sec.classList.toggle("hidden",!hv);')
L('const sc=sec.querySelector("[id^=\\"sc-\\"]");if(sc){sc.textContent=hv?g.querySelectorAll(".card:not(.hidden)").length:"0"}}})}')
L('function tr(r){const b=document.querySelector(".fr[data-r=\\""+r+"\\"]");if(b)b.classList.toggle("off");af()}')
L('function tw(w){const b=document.querySelector(".fw[data-w=\\""+w+"\\"]");if(b)b.classList.toggle("off");af()}')
L('function rf(){document.getElementById("gs").value="";document.querySelectorAll(".fb.off").forEach(b=>b.classList.remove("off"));af();showToast("Filters reset")}')
L('function showToast(m){const t=document.getElementById("toast");t.textContent=m;t.classList.add("show");setTimeout(()=>t.classList.remove("show"),2000)}')
L('document.getElementById("mb").addEventListener("click",function(){const m=document.getElementById("mm");m.style.display=m.style.display==="flex"?"none":"flex"})')
L('document.querySelectorAll("#mm a").forEach(a=>a.addEventListener("click",function(){document.getElementById("mm").style.display="none"}))')
L('const nav=document.querySelector(".nav");window.addEventListener("scroll",function(){nav.style.borderBottom=window.scrollY>64?"1px solid rgba(235,75,75,0.1)":"1px solid rgba(255,255,255,0.04)"})')
L('</script>')
L('</body></html>')

outpath = os.path.join(os.path.dirname(__file__), 'index.html')
with open(outpath, 'w') as f:
    f.write(''.join(lines))

print('Done! '+str(total)+' skins')
for sid, title, _ in categories:
    print('  '+title+': '+str(len(cat_data[sid])))
