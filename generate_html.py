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
    'Covert': ('covert', '#eb4b4b'), 'Classified': ('classified', '#d32ce6'),
    'Restricted': ('restricted', '#8847ff'), 'Mil-Spec Grade': ('milspec', '#4b69ff'),
    'Industrial Grade': ('industrial', '#5e98d9'), 'Consumer Grade': ('consumer', '#b0b0b0'),
    'Extraordinary': ('knife', '#ffd700'),
}
r_order = {'Covert':0,'Classified':1,'Restricted':2,'Mil-Spec Grade':3,'Industrial Grade':4,'Consumer Grade':5,'Extraordinary':0}

categories = [
    ('rifles', 'Rifles', '🔫', ['ak-47','m4a4','m4a1-s','awp','ssg 08','sg 553','aug','famas','galil ar','scar-20','g3sg1']),
    ('pistols', 'Pistols', '🔫', ['desert eagle','usp-s','glock-18','p2000','p250','cz75-auto','five-seven','tec-9','dual berettas','r8 revolver']),
    ('smgs', 'SMGs', '⚡', ['mac-10','mp9','mp5-sd','mp7','ump-45','p90','pp-bizon']),
    ('heavies', 'Heavy', '💥', ['mag-7','nova','xm1014','sawed-off','m249','negev']),
    ('knives', 'Knives', '★', ['karambit','butterfly knife','m9 bayonet','talon knife','bayonet','flip knife','shadow daggers','bowie knife','stiletto knife','ursus knife','nomad knife','skeleton knife','classic knife','gut knife','huntsman knife','falchion knife','navaja knife','paracord knife','survival knife','kukri knife']),
    ('gloves', 'Gloves', '🧤', ['hand wraps','sport gloves','moto gloves','driver gloves','specialist gloves','bloodhound gloves','broken fang gloves','hydra gloves']),
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
for sid, title, icon, wp_list in categories:
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
    cls, hex = ra_info.get(r, ('milspec', '#4b69ff'))
    nm_lower = (wn + ' | ' + sn).lower()
    return ('<div class="c" data-w="' + wn.lower() + '" data-r="' + r + '" data-n="' + nm_lower + '">'
            '<div class="ci"><img src="' + url + '" alt="' + wn + ' ' + sn + '" loading="lazy"></div>'
            '<div class="cb">'
            '<span class="cr" style="color:' + hex + '">' + r.upper() + '</span>'
            '<h3 class="cn">' + wn + '<br>' + sn + '</h3>'
            '</div></div>')

lines = []
def L(s): lines.append(s)

L('<!DOCTYPE html><html lang="en"><head>')
L('<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">')
L('<title>CS2 Skin Vault</title>')
L('<link rel="preconnect" href="https://fonts.googleapis.com">')
L('<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>')
L('<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Orbitron:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">')

# CSS
L('<style>')
L('*{box-sizing:border-box;margin:0;padding:0}')
L('html{scroll-behavior:smooth}')
L('body{font-family:"Inter",sans-serif;background:#07070d;color:#ddd;line-height:1.5;-webkit-font-smoothing:antialiased}')
L('.f{font-family:"Orbitron",sans-serif}')
L(':root{--r1:#eb4b4b;--r2:#d32ce6;--r3:#8847ff;--r4:#4b69ff;--r5:#5e98d9;--r6:#b0b0b0;--r7:#ffd700}')

# Nav
L('.nv{position:fixed;top:0;left:0;width:100%;height:60px;z-index:100;background:rgba(7,7,13,.92);backdrop-filter:blur(16px);border-bottom:1px solid rgba(255,255,255,.04)}')
L('.nvi{max-width:1200px;margin:0 auto;padding:0 20px;height:100%;display:flex;align-items:center;justify-content:space-between}')
L('.nvl{display:flex;align-items:center;gap:10px}')
L('.nvg{width:30px;height:30px;border-radius:6px;background:var(--r1);display:flex;align-items:center;justify-content:center;color:#fff;font-size:11px;font-weight:900;font-family:"Orbitron",sans-serif}')
L('.nvt{font-family:"Orbitron",sans-serif;font-size:14px;font-weight:700;color:#fff}')
L('.nvb{padding:2px 7px;border-radius:4px;background:rgba(255,255,255,.04);font-size:9px;color:#555;border:1px solid rgba(255,255,255,.04)}')
L('.nvr{display:none;gap:20px}@media(min-width:768px){.nvr{display:flex}}')
L('.nvr a{color:#555;font-size:13px;text-decoration:none;transition:color .2s}')
L('.nvr a:hover{color:#eee}')

# Hero
L('.hr{background:linear-gradient(160deg,#07070d,#0c0c18,#121225);position:relative;overflow:hidden;padding:100px 0 60px}')
L('.hr::before{content:"";position:absolute;inset:0;background:radial-gradient(ellipse at 30% 50%,rgba(235,75,75,.07) 0%,transparent 70%),radial-gradient(ellipse at 70% 50%,rgba(136,71,255,.05) 0%,transparent 60%);pointer-events:none}')
L('.hri{max-width:1200px;margin:0 auto;padding:0 20px;position:relative;z-index:1}')
L('.hrt{display:inline-flex;align-items:center;gap:6px;padding:5px 14px;border-radius:20px;background:rgba(235,75,75,.08);border:1px solid rgba(235,75,75,.15);margin-bottom:16px;font-size:11px;color:var(--r1);font-weight:600}')
L('.hrh{font-size:34px;font-weight:900;color:#fff;line-height:1.15;margin-bottom:12px}')
L('.hrp{color:#555;font-size:14px;max-width:450px;line-height:1.6}')

# Search bar - clean, minimal
L('.sr{background:#0c0c18;border-bottom:1px solid rgba(255,255,255,.04);padding:16px 0;position:sticky;top:60px;z-index:50}')
L('.sri{max-width:1200px;margin:0 auto;padding:0 20px}')
L('.sw{position:relative}')
L('.sw svg{position:absolute;left:14px;top:50%;transform:translateY(-50%);color:#444}')
L('.sw input{width:100%;padding:13px 16px 13px 44px;border-radius:10px;border:1px solid rgba(255,255,255,.06);background:rgba(255,255,255,.03);color:#fff;font-size:15px;outline:none;transition:border .25s}')
L('.sw input:focus{border-color:var(--r1)}')
L('.sw input::placeholder{color:#444}')
L('.ft{overflow:hidden;max-height:0;transition:max-height .35s ease,opacity .3s ease, margin .3s ease;opacity:0;margin-top:0}')
L('.ft.show{max-height:500px;opacity:1;margin-top:14px}')
L('.ftr{display:flex;flex-wrap:wrap;align-items:center;gap:6px}')
L('.ftl{color:#444;font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.5px;margin-right:6px;min-width:42px}')
L('.fb{padding:5px 14px;border-radius:20px;border:1px solid rgba(255,255,255,.06);background:transparent;font-size:11px;cursor:pointer;transition:all .2s;color:#999}')
L('.fb:hover{border-color:rgba(255,255,255,.15);color:#ddd}')
L('.fb.off{opacity:.15;text-decoration:line-through}')
L('.fbr{color:var(--r1);border-color:rgba(235,75,75,.3);font-weight:600}')
L('.fbr:hover{background:rgba(235,75,75,.08)}')

# Stats
L('.st{background:#0c0c18;border-bottom:1px solid rgba(255,255,255,.04);padding:12px 0}')
L('.sti{max-width:1200px;margin:0 auto;padding:0 20px;display:grid;grid-template-columns:repeat(4,1fr);gap:8px;text-align:center}')
L('.stn{font-size:18px;font-weight:800;color:#fff;font-family:"Orbitron",sans-serif}')
L('.stl{font-size:10px;color:#555;margin-top:2px}')

# Main page
L('.mn{max-width:1200px;margin:0 auto;padding:24px 20px}')

# Section
L('.sc{margin-bottom:36px}')
L('.sch{display:flex;align-items:center;justify-content:space-between;margin-bottom:16px;padding-bottom:12px;border-bottom:1px solid rgba(255,255,255,.04)}')
L('.schl{display:flex;align-items:center;gap:8px}')
L('.sci{width:26px;height:26px;border-radius:6px;display:flex;align-items:center;justify-content:center;font-size:13px}')
L('.sct{font-size:16px;font-weight:700;color:#fff;font-family:"Orbitron",sans-serif}')
L('.scc{font-size:11px;color:#555}')
L('.scv{padding:8px 18px;border-radius:8px;border:1px solid var(--r1);color:var(--r1);font-size:12px;cursor:pointer;background:transparent;transition:all .25s;font-weight:600;text-decoration:none}')
L('.scv:hover{background:rgba(235,75,75,.08)}')

# Grid - main page shows 10 items
L('.gd{display:grid;grid-template-columns:repeat(2,1fr);gap:10px}')
L('@media(min-width:500px){.gd{grid-template-columns:repeat(3,1fr)}}')
L('@media(min-width:700px){.gd{grid-template-columns:repeat(4,1fr)}}')
L('@media(min-width:900px){.gd{grid-template-columns:repeat(5,1fr)}}')

# Card
L('.c{background:#0c0c18;border-radius:8px;overflow:hidden;border:1px solid rgba(255,255,255,.04);transition:all .3s;cursor:pointer}')
L('.c:hover{transform:translateY(-3px);border-color:rgba(255,255,255,.08);box-shadow:0 8px 30px rgba(0,0,0,.4)}')
L('.c.hide{display:none!important}')
L('.ci{background:linear-gradient(180deg,rgba(255,255,255,.02),transparent);display:flex;align-items:center;justify-content:center;padding:8px;aspect-ratio:16/10}')
L('.ci img{width:100%;height:100%;object-fit:contain;transition:transform .35s;filter:drop-shadow(0 3px 10px rgba(0,0,0,.5))}')
L('.c:hover .ci img{transform:scale(1.05)}')
L('.cb{padding:8px 10px 10px}')
L('.cr{font-size:8px;font-weight:700;letter-spacing:.5px;text-transform:uppercase}')
L('.cn{color:#fff;font-size:11px;font-weight:600;line-height:1.35;margin-top:3px}')

# Catalog overlay (full page per category)
L('.cato{position:fixed;inset:0;background:#07070d;z-index:200;overflow-y:auto;display:none}')
L('.cato.show{display:block}')
L('.cath{position:sticky;top:0;z-index:10;background:#0c0c18;border-bottom:1px solid rgba(255,255,255,.06);display:flex;align-items:center;justify-content:space-between;padding:12px 20px}')
L('.cathl{display:flex;align-items:center;gap:10px}')
L('.catb{display:flex;align-items:center;gap:6px;padding:8px 16px;border-radius:8px;border:1px solid rgba(255,255,255,.08);color:#aaa;font-size:12px;cursor:pointer;background:transparent;transition:all .2s}')
L('.catb:hover{border-color:var(--r1);color:var(--r1)}')
L('.catt{font-family:"Orbitron",sans-serif;font-size:15px;font-weight:700;color:#fff}')
L('.cato .sri{padding:14px 20px}')
L('.cato .gd{gap:10px}')
L('@media(min-width:500px){.cato .gd{grid-template-columns:repeat(3,1fr)}}')
L('@media(min-width:700px){.cato .gd{grid-template-columns:repeat(4,1fr)}}')
L('@media(min-width:1000px){.cato .gd{grid-template-columns:repeat(5,1fr)}}')
L('@media(min-width:1200px){.cato .gd{grid-template-columns:repeat(6,1fr)}}')
L('.catg{padding:16px 20px 40px}')
L('.catc{font-size:11px;color:#555;margin-top:12px;text-align:center}')

# Footer
L('.ftr2{background:#0c0c18;border-top:1px solid rgba(255,255,255,.04);padding:28px 20px;text-align:center}')
L('.ftr2 p{color:#444;font-size:11px;max-width:400px;margin:0 auto;line-height:1.6}')

L('</style></head><body>')

# Navbar
L('<nav class="nv"><div class="nvi"><div class="nvl"><span class="nvg">CS</span><span class="nvt">Skin Vault</span><span class="nvb">v2.0</span></div>')
L('<div class="nvr">')
for sid, title, icon, _ in categories:
    L('<a href="#s-'+sid+'">'+title+'</a>')
L('</div><button id="mb" style="background:none;border:none;color:#555;font-size:20px;cursor:pointer" onclick="document.getElementById(\'mm\').style.display=document.getElementById(\'mm\').style.display==\'block\'?\'none\':\'block\'">☰</button></div>')
L('<div id="mm" style="display:none;background:#0c0c18;border-top:1px solid rgba(255,255,255,.04);padding:12px 20px;flex-direction:column;gap:6px">')
for sid, title, icon, _ in categories:
    L('<a href="#s-'+sid+'" style="color:#888;font-size:13px;text-decoration:none;padding:4px 0" onclick="document.getElementById(\'mm\').style.display=\'none\'">'+icon+' '+title+'</a>')
L('</div></nav>')

# Hero
L('<div class="hr"><div class="hri">')
L('<div class="hrt">Complete Armory &bull; '+str(total)+' finishes</div>')
L('<h1 class="hrh">CS2 <span style="background:linear-gradient(135deg,var(--r1),#ff8c00);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text">Skin Vault</span></h1>')
L('<p class="hrp">Every weapon finish in CS2. Browse featured skins or dive into a category.</p>')
L('</div></div>')

# Stats
L('<div class="st"><div class="sti">')
L('<div><div class="stn">'+str(total)+'+</div><div class="stl">Total Skins</div></div>')
L('<div><div class="stn">7</div><div class="stl">Rarity Tiers</div></div>')
L('<div><div class="stn">5</div><div class="stl">Wear Levels</div></div>')
L('<div><div class="stn" id="fc">10</div><div class="stl">Per Category</div></div>')
L('</div></div>')

# Search bar (toggles appear on focus)
L('<div class="sr"><div class="sri">')
L('<div class="sw"><svg width="16" height="16" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg>')
L('<input type="text" id="gs" placeholder="Search skins across all categories..." onfocus="document.getElementById(\'ftm\').classList.add(\'show\')" oninput="af()">')
L('</div>')
L('<div class="ft" id="ftm">')
L('<div class="ftr"><span class="ftl">Rarity</span>')
for rn in ['Covert','Classified','Restricted','Mil-Spec Grade','Industrial Grade','Consumer Grade']:
    c = {'Covert':'#eb4b4b','Classified':'#d32ce6','Restricted':'#8847ff','Mil-Spec Grade':'#4b69ff','Industrial Grade':'#5e98d9','Consumer Grade':'#b0b0b0'}[rn]
    ln = rn.replace('Mil-Spec Grade','Mil-Spec').replace('Industrial Grade','Industrial').replace('Consumer Grade','Consumer')
    L('<button class="fb" data-r="'+rn+'" onclick="tr(this.dataset.r)" style="color:'+c+'">'+ln+'</button>')
L('</div>')
L('<div class="ftr" style="margin-top:6px"><span class="ftl">Weapon</span>')
for sid, title, icon, wp_list in categories:
    for wl in wp_list:
        dn = weapon_display.get(wl, wl.title())
        L('<button class="fb" data-w="'+wl+'" onclick="tw(this.dataset.w)" style="font-size:10px">'+dn+'</button>')
L('</div>')
L('<div class="ftr" style="margin-top:8px"><button class="fb fbr" onclick="rf()">Reset Filters</button></div>')
L('</div></div></div>')

# Main page sections
L('<div class="mn">')
for sid, title, icon, wp_list in categories:
    group = cat_data[sid]
    total_cat = len(group)
    preview = group[:10]
    cards = '\n'.join(card_html(wn, sn, url, r) for wn, sn, url, r in preview)
    
    section_icon_colors = {'rifles':'#eb4b4b','pistols':'#4b69ff','smgs':'#8847ff','heavies':'#5e98d9','knives':'#ffd700','gloves':'#b8860b'}
    col = section_icon_colors.get(sid, '#fff')
    
    L('<div class="sc" id="s-'+sid+'">')
    L('<div class="sch"><div class="schl"><div class="sci" style="background:'+col+'15;color:'+col+'">'+icon+'</div><span class="sct">'+title+'</span><span class="scc">'+str(total_cat)+'</span></div>')
    L('<button class="scv" onclick="openCat(\''+sid+'\',\''+title+'\',\''+icon+'\')">View All '+str(total_cat)+' &rarr;</button></div>')
    L('<div class="gd">'+cards+'</div></div>')

L('</div>')

# Catalog overlays (one per category)
for sid, title, icon, wp_list in categories:
    group = cat_data[sid]
    total_cat = len(group)
    all_cards = '\n'.join(card_html(wn, sn, url, r) for wn, sn, url, r in group)
    
    L('<div class="cato" id="cato-'+sid+'">')
    L('<div class="cath"><div class="cathl"><button class="catb" onclick="closeCat(\''+sid+'\')">&larr; Back</button><span class="catt">'+icon+' '+title+'</span></div><span style="color:#555;font-size:12px">'+str(total_cat)+' skins</span></div>')
    # Filters inside catalog
    L('<div class="sr" style="top:0;position:sticky"><div class="sri">')
    L('<div class="sw"><svg width="16" height="16" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg>')
    L('<input type="text" id="cgs-'+sid+'" placeholder="Search in '+title+'..." oninput="cf(\''+sid+'\')" class="cgi-'+sid+'">')
    L('</div>')
    L('<div class="ft show">')  # Always visible in catalog
    L('<div class="ftr"><span class="ftl">Rarity</span>')
    for rn in ['Covert','Classified','Restricted','Mil-Spec Grade','Industrial Grade','Consumer Grade']:
        c = {'Covert':'#eb4b4b','Classified':'#d32ce6','Restricted':'#8847ff','Mil-Spec Grade':'#4b69ff','Industrial Grade':'#5e98d9','Consumer Grade':'#b0b0b0'}[rn]
        ln = rn.replace('Mil-Spec Grade','Mil-Spec').replace('Industrial Grade','Industrial').replace('Consumer Grade','Consumer')
        L('<button class="fb cfr-'+sid+'" data-r="'+rn+'" onclick="ctr(\''+sid+'\',this.dataset.r)" style="color:'+c+'">'+ln+'</button>')
    L('</div>')
    L('<div class="ftr" style="margin-top:6px"><span class="ftl">Weapon</span>')
    for wl in wp_list:
        dn = weapon_display.get(wl, wl.title())
        L('<button class="fb cfw-'+sid+'" data-w="'+wl+'" onclick="ctw(\''+sid+'\',this.dataset.w)" style="font-size:10px">'+dn+'</button>')
    L('</div>')
    L('<div class="ftr" style="margin-top:8px"><button class="fb fbr" onclick="crf(\''+sid+'\')">Reset</button><span class="crc-'+sid+'" style="color:#555;font-size:11px;margin-left:12px">'+str(total_cat)+' matching</span></div>')
    L('</div></div></div>')
    L('<div class="catg"><div class="gd" id="cg-'+sid+'">'+all_cards+'</div><div class="catc" id="cem-'+sid+'"></div></div>')
    L('</div>')

# Footer
L('<div class="ftr2"><p>CS2 Skin Vault &bull; '+str(total)+' weapon finishes &bull; Not affiliated with Valve Corporation</p></div>')

# JS
L('<script>')
L('function af(){const s=document.getElementById("gs").value.toLowerCase().trim();')
L('const rb=document.querySelectorAll(".sr .fb[data-r]");const wb=document.querySelectorAll(".sr .fb[data-w]");')
L('const ar=new Set();rb.forEach(b=>{if(!b.classList.contains("off"))ar.add(b.dataset.r)});')
L('const aw=new Set();wb.forEach(b=>{if(!b.classList.contains("off"))aw.add(b.dataset.w)});')
L('const c=document.querySelectorAll(".c");let v=0;c.forEach(cd=>{const w=cd.dataset.w;const r=cd.dataset.r;const n=cd.dataset.n;')
L('const ms=!s||n.includes(s);const mr=ar.size===0||ar.has(r);const mw=aw.size===0||aw.has(w);')
L('if(ms&&mr&&mw){cd.classList.remove("hide");v++}else{cd.classList.add("hide")}})}')
L('function tr(r){const b=document.querySelector(".sr .fb[data-r=\'"+r+"\']");if(b){b.classList.toggle("off");af()}}')
L('function tw(w){const b=document.querySelector(".sr .fb[data-w=\'"+w+"\']");if(b){b.classList.toggle("off");af()}}')
L('function rf(){document.getElementById("gs").value="";document.querySelectorAll(".sr .fb.off").forEach(b=>b.classList.remove("off"));af()}')
L('function openCat(sid,title,icon){document.querySelectorAll(".cato").forEach(o=>o.classList.remove("show"));document.getElementById("cato-"+sid).classList.add("show");document.body.style.overflow="hidden";cf(sid)}')
L('function closeCat(sid){document.getElementById("cato-"+sid).classList.remove("show");document.body.style.overflow=""}')
L('function cf(sid){const s=document.getElementById("cgs-"+sid).value.toLowerCase().trim();')
L('const rb=document.querySelectorAll(".cfr-"+sid);const wb=document.querySelectorAll(".cfw-"+sid);')
L('const ar=new Set();rb.forEach(b=>{if(!b.classList.contains("off"))ar.add(b.dataset.r)});')
L('const aw=new Set();wb.forEach(b=>{if(!b.classList.contains("off"))aw.add(b.dataset.w)});')
L('const c=document.querySelectorAll("#cg-"+sid+" .c");let v=0;')
L('c.forEach(cd=>{const w=cd.dataset.w;const r=cd.dataset.r;const n=cd.dataset.n;')
L('const ms=!s||n.includes(s);const mr=ar.size===0||ar.has(r);const mw=aw.size===0||aw.has(w);')
L('if(ms&&mr&&mw){cd.classList.remove("hide");v++}else{cd.classList.add("hide")}});')
L('const el=document.querySelector(".crc-"+sid);if(el)el.textContent=v+" matching";')
L('const em=document.getElementById("cem-"+sid);if(em)em.textContent=v===0?"No skins match your filters":""}')
L('function ctr(sid,r){const b=document.querySelector(".cfr-"+sid+"[data-r=\'"+r+"\']");if(b){b.classList.toggle("off");cf(sid)}}')
L('function ctw(sid,w){const b=document.querySelector(".cfw-"+sid+"[data-w=\'"+w+"\']");if(b){b.classList.toggle("off");cf(sid)}}')
L('function crf(sid){document.getElementById("cgs-"+sid).value="";document.querySelectorAll(".cfr-"+sid+".off,.cfw-"+sid+".off").forEach(b=>b.classList.remove("off"));cf(sid)}')
L('document.addEventListener("keydown",function(e){if(e.key==="Escape"){document.querySelectorAll(".cato.show").forEach(o=>{o.classList.remove("show");document.body.style.overflow=""})}})')
L('document.getElementById("mb").addEventListener("click",function(){const m=document.getElementById("mm");m.style.display=m.style.display==="block"?"none":"block"});')
L('document.querySelectorAll("#mm a").forEach(a=>a.addEventListener("click",function(){document.getElementById("mm").style.display="none"}))')
L('window.addEventListener("scroll",function(){document.querySelector(".nv").style.borderBottom=window.scrollY>60?"1px solid rgba(235,75,75,.1)":"1px solid rgba(255,255,255,.04)"})')
L('</script>')
L('</body></html>')

outpath = os.path.join(os.path.dirname(__file__), 'index.html')
with open(outpath, 'w') as f:
    f.write(''.join(lines))

total_cards = sum(len(cat_data[sid]) for sid, _, _, _ in categories)
print('Done! '+str(total_cards)+' skins across '+str(len(categories))+' categories')
for sid, title, _, _ in categories:
    print('  '+title+': '+str(len(cat_data[sid]))+' (showing 10)')
