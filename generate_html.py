import json

with open('C:\\Users\\Student\\Desktop\\summer-school\\skins_data.json') as f:
    raw = json.load(f)
all_skins = raw['all']

fixed = []
for wn, sn, url, r in all_skins:
    if 'raw.githubusercontent' in url:
        url = url.replace('/330x192', '')
    fixed.append((wn, sn, url, r))
all_skins = fixed

ra_hex = {'Covert':'#eb4b4b','Classified':'#d32ce6','Restricted':'#8847ff','Mil-Spec Grade':'#4b69ff','Industrial Grade':'#5e98d9','Consumer Grade':'#b0b0b0','Extraordinary':'#ffd700'}
r_order = {'Covert':0,'Classified':1,'Restricted':2,'Mil-Spec Grade':3,'Industrial Grade':4,'Consumer Grade':5,'Extraordinary':0}

categories = [
    ('rifles','Rifles','🔫',['ak-47','m4a4','m4a1-s','awp','ssg 08','sg 553','aug','famas','galil ar','scar-20','g3sg1']),
    ('pistols','Pistols','🔫',['desert eagle','usp-s','glock-18','p2000','p250','cz75-auto','five-seven','tec-9','dual berettas','r8 revolver']),
    ('smgs','SMGs','⚡',['mac-10','mp9','mp5-sd','mp7','ump-45','p90','pp-bizon']),
    ('heavies','Heavy','💥',['mag-7','nova','xm1014','sawed-off','m249','negev']),
    ('knives','Knives','★',['karambit','butterfly knife','m9 bayonet','talon knife','bayonet','flip knife','shadow daggers','bowie knife','stiletto knife','ursus knife','nomad knife','skeleton knife','classic knife','gut knife','huntsman knife','falchion knife','navaja knife','paracord knife','survival knife','kukri knife']),
    ('gloves','Gloves','🧤',['hand wraps','sport gloves','moto gloves','driver gloves','specialist gloves','bloodhound gloves','broken fang gloves','hydra gloves']),
]

wpn_disp = {'ak-47':'AK-47','m4a4':'M4A4','m4a1-s':'M4A1-S','awp':'AWP','ssg 08':'SSG 08','sg 553':'SG 553','aug':'AUG','famas':'FAMAS','galil ar':'Galil AR','scar-20':'SCAR-20','g3sg1':'G3SG1','desert eagle':'Deagle','usp-s':'USP-S','glock-18':'Glock','p2000':'P2000','p250':'P250','cz75-auto':'CZ75','five-seven':'Five-SeveN','tec-9':'Tec-9','dual berettas':'Dualies','r8 revolver':'R8','mac-10':'MAC-10','mp9':'MP9','mp5-sd':'MP5-SD','mp7':'MP7','ump-45':'UMP-45','p90':'P90','pp-bizon':'PP-Bizon','mag-7':'MAG-7','nova':'Nova','xm1014':'XM1014','sawed-off':'Sawed-Off','m249':'M249','negev':'Negev','karambit':'Karambit','butterfly knife':'Butterfly','m9 bayonet':'M9','talon knife':'Talon','bayonet':'Bayonet','flip knife':'Flip','shadow daggers':'Shadow','bowie knife':'Bowie','stiletto knife':'Stiletto','ursus knife':'Ursus','nomad knife':'Nomad','skeleton knife':'Skeleton','classic knife':'Classic','gut knife':'Gut','huntsman knife':'Huntsman','falchion knife':'Falchion','navaja knife':'Navaja','paracord knife':'Paracord','survival knife':'Survival','kukri knife':'Kukri','hand wraps':'Hand Wraps','sport gloves':'Sport','moto gloves':'Moto','driver gloves':'Driver','specialist gloves':'Specialist','bloodhound gloves':'Bloodhound','broken fang gloves':'Broken Fang','hydra gloves':'Hydra'}

cat_data = {}
for sid,title,icon,wp_list in categories:
    group = []
    for wl in wp_list:
        g = []
        for wn,sn,url,r in all_skins:
            if wn.lower() == wl: g.append((wn,sn,url,r))
        g.sort(key=lambda x: (r_order.get(x[3],99), x[1]))
        group.extend(g)
    cat_data[sid] = group

total = len(all_skins); t = str(total)
cols = {'rifles':'#eb4b4b','pistols':'#4b69ff','smgs':'#8847ff','heavies':'#5e98d9','knives':'#ffd700','gloves':'#b8860b'}

def card(wn,sn,url,r):
    h = ra_hex.get(r,'#fff')
    slug = (wn+' '+sn).lower().replace('|','').replace('&','').replace('  ',' ').strip().replace(' ','-')
    slug = ''.join(c for c in slug if c.isalnum() or c == '-')
    return f'<div class="c" data-w="{wn.lower()}" data-r="{r}" data-n="{(wn+" | "+sn).lower()}" onclick="window.location=\'detail.html?skin={slug}\'" style="cursor:pointer"><div class="ci"><img src="{url}" alt="{wn} {sn}" loading="lazy"><div class="ch"></div></div><div class="cb"><span style="color:{h}">{r.upper()}</span><b>{wn}</b><span>{sn}</span></div></div>'

# --- BUILD CSS ---
css = '''<style>@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&display=swap');*{margin:0;padding:0;box-sizing:border-box}html{scroll-behavior:smooth}body{font-family:system-ui,-apple-system,BlinkMacSystemFont,Segoe UI,sans-serif;background:#05050a;color:#c8c8d4;min-height:100vh;line-height:1.5;overflow-x:hidden}:root{--bg:#05050a;--bg2:#0b0b14;--bg3:#10101c;--bg4:#161628;--fg:#c8c8d4;--fg2:#7777a0;--r1:#ff3b3b;--r2:#d32ce6;--r3:#8847ff;--r4:#4b69ff;--r5:#5e98d9;--r6:#b0b0c0;--r7:#ffd700}body::before,body::after{content:;position:fixed;border-radius:50%;pointer-events:none;z-index:0;animation:orb 8s ease-in-out infinite}body::before{width:500px;height:500px;background:radial-gradient(circle,rgba(235,75,75,.04) 0%,transparent 70%);top:-100px;left:-100px;animation-delay:0s}body::after{width:600px;height:600px;background:radial-gradient(circle,rgba(136,71,255,.04) 0%,transparent 70%);bottom:-150px;right:-150px;animation-delay:3s}@keyframes orb{0%,100%{transform:translate(0,0) scale(1)}33%{transform:translate(60px,-40px) scale(1.1)}66%{transform:translate(-30px,50px) scale(.9)}}.nv{height:56px;background:rgba(5,5,10,.92);backdrop-filter:blur(20px);border-bottom:1px solid rgba(255,255,255,.04);position:sticky;top:0;z-index:100}.nv>div{max-width:1280px;margin:0 auto;padding:0 24px;height:100%;display:flex;align-items:center;justify-content:space-between}.nvl{display:flex;gap:10px;align-items:center}.nvg{width:30px;height:30px;border-radius:8px;background:linear-gradient(135deg,var(--r1),#ff8c00);color:#fff;font-weight:900;font-size:12px;display:flex;align-items:center;justify-content:center;font-family:Orbitron,sans-serif}.nvt{font-weight:800;color:#fff;font-size:15px;letter-spacing:-.3px;font-family:Orbitron,sans-serif}.nvb{font-size:8px;color:var(--fg2);background:var(--bg3);border:1px solid rgba(255,255,255,.04);padding:2px 7px;border-radius:4px;font-weight:700;letter-spacing:.8px;text-transform:uppercase}.nvr{display:none;gap:20px}@media(min-width:768px){.nvr{display:flex}}.nvr a{color:var(--fg2);font-size:12px;text-decoration:none;transition:.2s;font-weight:600;letter-spacing:.3px;text-transform:uppercase}.nvr a:hover{color:#fff;text-shadow:0 0 20px rgba(255,255,255,.1)}.hr{position:relative;overflow:hidden;padding:90px 0 50px;z-index:1}.hr::before{content:;position:absolute;inset:0;background:radial-gradient(ellipse at 30% 40%,rgba(235,75,75,.08) 0%,transparent 60%),radial-gradient(ellipse at 70% 60%,rgba(136,71,255,.06) 0%,transparent 60%),radial-gradient(ellipse at 50% 80%,rgba(255,215,0,.04) 0%,transparent 50%);pointer-events:none;z-index:-1}.hr::after{content:;position:absolute;top:0;left:0;width:100%;height:2px;background:linear-gradient(90deg,transparent,var(--r1),var(--r3),var(--r7),transparent);opacity:.5;animation:scan 3s linear infinite;pointer-events:none}@keyframes scan{0%{transform:translateX(-100%)}100%{transform:translateX(100%)}}.hri{max-width:1280px;margin:0 auto;padding:0 24px;position:relative;z-index:1}.hrt{display:inline-flex;align-items:center;gap:8px;padding:5px 14px;border-radius:24px;background:rgba(235,75,75,.08);border:1px solid rgba(235,75,75,.15);font-size:10px;color:var(--r1);font-weight:700;letter-spacing:.5px;text-transform:uppercase;margin-bottom:16px;animation:fadeIn .6s}.hrt span{width:6px;height:6px;border-radius:50%;background:var(--r1);animation:pulse 2s infinite}@keyframes pulse{0%,100%{opacity:1;transform:scale(1)}50%{opacity:.3;transform:scale(.7)}}.hrh{font-size:42px;font-weight:900;color:#fff;line-height:1.05;margin-bottom:10px;letter-spacing:-.5px;font-family:Orbitron,sans-serif;text-transform:uppercase;animation:fadeIn .8s}.hrh em{font-style:normal;background:linear-gradient(135deg,var(--r1),#ff8c00,var(--r7));-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;background-size:200% 200%;animation:grad 3s ease infinite}@keyframes grad{0%,100%{background-position:0% 50%}50%{background-position:100% 50%}}.hrp{color:var(--fg2);font-size:14px;max-width:460px;animation:fadeIn 1s}@keyframes fadeIn{from{opacity:0;transform:translateY(16px)}to{opacity:1;transform:translateY(0)}}.st{position:relative;z-index:1;background:var(--bg2);border-top:1px solid rgba(255,255,255,.02);border-bottom:1px solid rgba(255,255,255,.04)}.st>div{max-width:1280px;margin:0 auto;padding:16px 24px;display:grid;grid-template-columns:repeat(4,1fr);gap:12px;text-align:center}.stn{font-size:24px;font-weight:900;color:#fff;font-family:Orbitron,sans-serif}.stl{font-size:10px;color:var(--fg2);text-transform:uppercase;letter-spacing:.5px;margin-top:2px}.gs{position:relative;z-index:1;padding:16px 24px;background:var(--bg2);border-bottom:1px solid rgba(255,255,255,.04)}.gs>div{max-width:1280px;margin:0 auto;position:relative}.gs svg{position:absolute;left:14px;top:50%;transform:translateY(-50%);color:#555}.gs input{width:100%;padding:12px 14px 12px 42px;border-radius:12px;border:1px solid rgba(255,255,255,.06);background:var(--bg3);color:#fff;font-size:14px;outline:none;transition:.25s;font-weight:400}.gs input:focus{border-color:var(--r1);box-shadow:0 0 0 3px rgba(235,75,75,.08)}.gs input::placeholder{color:#555}.gsc{text-align:center;padding:6px 0;font-size:11px;color:var(--fg2);font-weight:500}.mn{max-width:1280px;margin:0 auto;padding:32px 24px 48px;position:relative;z-index:1}.sc{margin-bottom:44px;animation:fadeIn .5s ease-out both}.sc:nth-child(1){animation-delay:.1s}.sc:nth-child(2){animation-delay:.2s}.sc:nth-child(3){animation-delay:.3s}.sc:nth-child(4){animation-delay:.4s}.sc:nth-child(5){animation-delay:.5s}.sc:nth-child(6){animation-delay:.6s}.sch{display:flex;align-items:center;justify-content:space-between;margin-bottom:16px}.sch-l{display:flex;align-items:center;gap:10px}.sch-i{width:32px;height:32px;border-radius:10px;display:flex;align-items:center;justify-content:center;font-size:15px;animation:bounce 2s ease-in-out infinite}@keyframes bounce{0%,100%{transform:translateY(0)}50%{transform:translateY(-4px)}}.sch-t{font-size:18px;font-weight:800;color:#fff;letter-spacing:-.2px;font-family:Orbitron,sans-serif}.sch-n{font-size:11px;color:var(--fg2);font-weight:600;background:var(--bg3);padding:2px 9px;border-radius:6px}.sch-b{padding:8px 18px;border-radius:10px;background:transparent;border:1px solid rgba(235,75,75,.2);color:var(--r1);font-size:11px;font-weight:700;cursor:pointer;transition:.3s;text-transform:uppercase;letter-spacing:.3px}.sch-b:hover{background:rgba(235,75,75,.08);border-color:var(--r1);box-shadow:0 0 20px rgba(235,75,75,.1)}.gd{display:grid;grid-template-columns:repeat(2,1fr);gap:12px}@media(min-width:500px){.gd{grid-template-columns:repeat(3,1fr)}}@media(min-width:700px){.gd{grid-template-columns:repeat(4,1fr)}}@media(min-width:900px){.gd{grid-template-columns:repeat(5,1fr)}}.c{background:var(--bg2);border:1px solid rgba(255,255,255,.04);border-radius:12px;overflow:hidden;transition:all .35s cubic-bezier(.34,1.56,.64,1);cursor:pointer;position:relative;animation:cardIn .4s ease-out both}.c:nth-child(1){animation-delay:.05s}.c:nth-child(2){animation-delay:.1s}.c:nth-child(3){animation-delay:.15s}.c:nth-child(4){animation-delay:.2s}.c:nth-child(5){animation-delay:.25s}.c:nth-child(6){animation-delay:.3s}.c:nth-child(7){animation-delay:.35s}.c:nth-child(8){animation-delay:.4s}.c:nth-child(9){animation-delay:.45s}.c:nth-child(10){animation-delay:.5s}@keyframes cardIn{from{opacity:0;transform:translateY(20px) scale(.95)}to{opacity:1;transform:translateY(0) scale(1)}}.c:hover{transform:translateY(-6px) scale(1.02);border-color:rgba(255,255,255,.08);box-shadow:0 16px 48px rgba(0,0,0,.4),0 0 30px rgba(235,75,75,.05)}.c.hide{display:none!important}.ci{position:relative;aspect-ratio:4/3;background:linear-gradient(180deg,rgba(255,255,255,.015),transparent);display:flex;align-items:center;justify-content:center;padding:12px}.ci img{width:100%;height:100%;object-fit:contain;transition:transform .5s cubic-bezier(.34,1.56,.64,1);filter:drop-shadow(0 4px 16px rgba(0,0,0,.5))}.c:hover .ci img{transform:scale(1.08) rotate(-1deg)}.ch{position:absolute;inset:0;opacity:0;transition:.5s;background:linear-gradient(45deg,transparent 20%,rgba(255,255,255,.015) 40%,transparent 60%);pointer-events:none}.c:hover .ch{opacity:1}.cb{padding:10px 12px 12px;position:relative}.cb::after{content:;position:absolute;top:0;left:12px;right:12px;height:1px;background:rgba(255,255,255,.04)}.cb span{display:block;font-size:8px;font-weight:700;letter-spacing:.4px;text-transform:uppercase;margin-bottom:3px}.cb b{display:block;color:#fff;font-size:11px;font-weight:600;line-height:1.3}.cb span:last-child{color:var(--fg2);font-size:10px;font-weight:400;text-transform:none;letter-spacing:0;margin-top:1px;margin-bottom:0}.ov{position:fixed;inset:0;background:rgba(5,5,10,.95);z-index:200;overflow-y:auto;display:none;backdrop-filter:blur(4px)}.ov.s{display:block;animation:fadeIn .2s}.ovt{position:sticky;top:0;z-index:10;background:rgba(11,11,20,.95);backdrop-filter:blur(20px);border-bottom:1px solid rgba(255,255,255,.04);display:flex;align-items:center;justify-content:space-between;padding:12px 24px}.ovtl{display:flex;align-items:center;gap:12px}.ovb{padding:7px 14px;border-radius:8px;background:var(--bg3);border:1px solid rgba(255,255,255,.06);color:var(--fg2);font-size:12px;cursor:pointer;transition:.2s;display:flex;align-items:center;gap:5px;font-weight:500}.ovb:hover{color:#fff;border-color:var(--r1);background:rgba(235,75,75,.06)}.ovbt{font-weight:700;color:#fff;font-size:15px;font-family:Orbitron,sans-serif}.ovbc{font-size:11px;color:var(--fg2)}.ovf{background:var(--bg2);border-bottom:1px solid rgba(255,255,255,.04);padding:20px 24px;display:flex;flex-direction:column;gap:14px}.ovf .ovfs,.ovf .ovfg,.ovf .ovff{max-width:640px;margin-left:auto;margin-right:auto;width:100%}.ovfs{position:relative}.ovfs svg{position:absolute;left:14px;top:50%;transform:translateY(-50%);color:#555}.ovfs input{width:100%;padding:11px 14px 11px 40px;border-radius:10px;border:1px solid rgba(255,255,255,.06);background:var(--bg3);color:#fff;font-size:14px;outline:none;transition:.2s}.ovfs input:focus{border-color:var(--r1);box-shadow:0 0 0 3px rgba(235,75,75,.06)}.ovfs input::placeholder{color:#555}.ovfg{display:flex;flex-direction:column;gap:8px}.ovfl{font-size:9px;font-weight:700;color:#666;text-transform:uppercase;letter-spacing:1px;margin-bottom:2px}.ovfr{display:flex;flex-wrap:wrap;gap:4px}.fb{padding:4px 12px;border-radius:16px;border:1px solid rgba(255,255,255,.04);background:rgba(255,255,255,.02);font-size:10.5px;cursor:pointer;transition:all .25s;font-weight:500;color:#999;letter-spacing:.2px}.fb:hover{border-color:rgba(255,255,255,.12);background:rgba(255,255,255,.05);color:#ddd;transform:translateY(-1px)}.fb.off{opacity:.15;text-decoration:none;transform:scale(.95)}.fbl{border-color:rgba(235,75,75,.15);color:var(--r1);font-weight:700;background:rgba(235,75,75,.04);font-size:10px}.fbl:hover{background:rgba(235,75,75,.1);color:#fff;border-color:var(--r1)}.ovff{display:flex;align-items:center;justify-content:space-between;padding-top:4px;border-top:1px solid rgba(255,255,255,.03)}.ovrc{font-size:11px;color:var(--fg2);font-weight:500}.ovg{padding:24px}.ftr2{background:var(--bg2);border-top:1px solid rgba(255,255,255,.04);padding:28px 24px;text-align:center;position:relative;z-index:1}.ftr2 p{color:#555;font-size:11px;max-width:400px;margin:0 auto;line-height:1.6}</style>'''
# --- END CSS ---

lines = []
lines.append('<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0"><title>CS2 Skin Vault</title>')
lines.append(css)
lines.append('</head><body>')

# NAV
lines.append('<nav class="nv"><div><div class="nvl"><div class="nvg">CS</div><div class="nvt">Skin Vault</div><div class="nvb">COMPLETE</div></div><div class="nvr"><a href="#s-rifles">Rifles</a><a href="#s-pistols">Pistols</a><a href="#s-smgs">SMGs</a><a href="#s-heavies">Heavy</a><a href="#s-knives">Knives</a><a href="#s-gloves">Gloves</a></div></div></nav>')

# HERO
lines.append(f'<div class="hr"><div class="hri"><div class="hrt"><span></span>Complete Armory &bull; {t} finishes</div><h1 class="hrh">CS2 <em>Skin Vault</em></h1><p class="hrp">Browse 10 featured skins per category, or dive into the full catalog with search and filters.</p></div></div>')

# STATS
lines.append(f'<div class="st"><div><div><div class="stn">{t}+</div><div class="stl">Total Skins</div></div><div><div class="stn">7</div><div class="stl">Rarity Tiers</div></div><div><div class="stn">5</div><div class="stl">Wear Levels</div></div><div><div class="stn" id="gc">10</div><div class="stl">Showing</div></div></div></div>')

# GLOBAL SEARCH BAR
lines.append('<div class="gs"><div><svg width="14" height="14" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg><input type="text" id="gsi" placeholder="Search all 1,974 skins..." oninput="globalFilter()"></div><div class="gsc" id="gsc"></div></div>')

# MAIN
lines.append('<div class="mn">')
for sid,title,icon,wp_list in categories:
    group = cat_data[sid]; tc = len(group)
    p10 = group[:10]
    pc = ''.join(card(*s) for s in p10)
    ac = ''.join(card(*s) for s in group)
    
    lines.append(f'<div class="sc" id="s-{sid}">')
    lines.append(f'<div class="sch"><div class="sch-l"><div class="sch-i" style="background:{cols[sid]}15;color:{cols[sid]}">{icon}</div><div class="sch-t">{title}</div><div class="sch-n">{tc}</div></div><button class="sch-b" onclick="openCat(\'{sid}\')">View All {tc} &rarr;</button></div>')
    lines.append(f'<div class="gd">{pc}</div></div>')
    
    # CATALOG OVERLAY
    lines.append(f'<div class="ov" id="o-{sid}">')
    lines.append(f'<div class="ovt"><div class="ovtl"><button class="ovb" onclick="closeCat(\'{sid}\')"><svg width="14" height="14" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 12H5m7-7l-7 7 7 7"/></svg> Back</button><div class="ovbt">{icon} {title}</div></div><div class="ovbc">{tc} skins</div></div>')
    lines.append(f'<div class="ovf"><div class="ovfs"><svg width="14" height="14" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg><input type="text" class="cgi" data-cat="{sid}" placeholder="Filter {title}..." oninput="cf(this)"></div>')
    
    # Rarity toggles
    lines.append('<div class="ovfg"><div class="ovfl">Rarity</div><div class="ovfr">')
    for rn in ['Covert','Classified','Restricted','Mil-Spec Grade','Industrial Grade','Consumer Grade']:
        ln = rn.replace('Mil-Spec Grade','Mil-Spec').replace('Industrial Grade','Industrial').replace('Consumer Grade','Consumer')
        lines.append(f'<button class="fb ocfr" data-cat="{sid}" data-r="{rn}" style="color:{ra_hex[rn]}">{ln}</button>')
    lines.append('</div></div>')
    
    # Weapon toggles
    lines.append('<div class="ovfg"><div class="ovfl">Weapon</div><div class="ovfr">')
    for wl in wp_list:
        lines.append(f'<button class="fb ocfw" data-cat="{sid}" data-w="{wl}" style="font-size:10px">{wpn_disp.get(wl,wl.title())}</button>')
    lines.append('</div></div>')
    
    # Count + Reset
    lines.append(f'<div class="ovff"><div class="ovrc" id="rc-{sid}">{tc} matching</div><button class="fb fbl" onclick="resetCat(\'{sid}\')">Reset</button></div></div>')
    
    lines.append(f'<div class="ovg"><div class="gd" id="g-{sid}">{ac}</div><div style="text-align:center;color:var(--fg2);font-size:12px;margin-top:16px" id="em-{sid}"></div></div>')
    lines.append('</div>')

lines.append('</div>')
lines.append('<footer style="background:var(--bg2);border-top:var(--bw);padding:28px 24px;text-align:center"><p style="color:var(--fg2);font-size:11px;max-width:400px;margin:0 auto">CS2 Skin Vault &bull; Not affiliated with Valve Corporation</p></footer>')

# DETAIL MODAL
lines.append('<div class="dm" id="dm"><div class="dmc"><div class="dmh"><div class="dmht">Skin Details</div><button class="dmx" onclick="closeDetail()">&times;</button></div><div class="dmi" id="dmi"></div><div class="dmd" id="dmd"></div><div class="dmb"><a href="#" target="_blank" id="dml" class="dmb2">View on CSGOSkins.gg &nearr;</a><a href="#" target="_blank" id="dms">Steam Market &nearr;</a></div></div></div>')

# JS
js = '''<script>
function globalFilter(){
  var s=document.getElementById("gsi").value.toLowerCase().trim();
  var cards=document.querySelectorAll(".mn .c"),v=0;
  cards.forEach(function(cd){
    if(!s||cd.dataset.n.indexOf(s)!==-1){cd.classList.remove("hide");v++}
    else{cd.classList.add("hide")}
  });
  document.getElementById("gc").textContent=v;
  document.getElementById("gsc").textContent=v===0?"No skins match":v+" skins shown";
  // Hide empty sections
  document.querySelectorAll(".sc").forEach(function(sec){
    var vis=sec.querySelector(".c:not(.hide)");
    sec.style.display=vis?"":"none"
  })
}
function openCat(cid){
  document.querySelectorAll(".ov").forEach(function(o){o.classList.remove("s")});
  document.getElementById("o-"+cid).classList.add("s");document.body.style.overflow="hidden";
  var inp=document.querySelector(".cgi[data-cat="+JSON.stringify(cid)+"]");if(inp)cf(inp)
}
function closeCat(cid){document.getElementById("o-"+cid).classList.remove("s");document.body.style.overflow=""}
function cf(inp){
  var cid=inp.dataset.cat,s=inp.value.toLowerCase().trim();
  var rbs=document.querySelectorAll("#o-"+cid+" .ocfr"),wbs=document.querySelectorAll("#o-"+cid+" .ocfw");
  var ar=new Set();rbs.forEach(function(b){if(!b.classList.contains("off"))ar.add(b.dataset.r)});
  var aw=new Set();wbs.forEach(function(b){if(!b.classList.contains("off"))aw.add(b.dataset.w)});
  var cards=document.querySelectorAll("#g-"+cid+" .c"),v=0;
  cards.forEach(function(cd){
    if((!s||cd.dataset.n.indexOf(s)!==-1)&&(ar.size===0||ar.has(cd.dataset.r))&&(aw.size===0||aw.has(cd.dataset.w))){cd.classList.remove("hide");v++}
    else{cd.classList.add("hide")}
  });
  var el=document.getElementById("rc-"+cid);if(el)el.textContent=v+" matching";
  var em=document.getElementById("em-"+cid);if(em)em.textContent=v===0?"No skins match your filters":""
}
function resetCat(cid){
  var inp=document.querySelector(".cgi[data-cat="+JSON.stringify(cid)+"]");if(inp)inp.value="";
  document.querySelectorAll("#o-"+cid+" .ocfr.off, #o-"+cid+" .ocfw.off").forEach(function(b){b.classList.remove("off")});
  var inp2=document.querySelector(".cgi[data-cat="+JSON.stringify(cid)+"]");if(inp2)cf(inp2)
}
document.addEventListener("click",function(e){
  var btn=e.target;
  if(btn.classList.contains("ocfr")||btn.classList.contains("ocfw")){
    btn.classList.toggle("off");var cid=btn.dataset.cat;
    var inp=document.querySelector(".cgi[data-cat="+JSON.stringify(cid)+"]");if(inp)cf(inp)
  }
});
document.addEventListener("keydown",function(e){
  if(e.key==="Escape"){
    document.querySelectorAll(".ov.s").forEach(function(o){o.classList.remove("s");document.body.style.overflow=""});
    closeDetail()
  }
});
function showDetail(el){
  var wn=el.querySelector(".cb b").textContent;
  var sn=el.querySelector(".cb span:last-child").textContent;
  var r=el.dataset.r;
  var img=el.querySelector("img").src;
  var hex={'Covert':'#eb4b4b','Classified':'#d32ce6','Restricted':'#8847ff','Mil-Spec Grade':'#4b69ff','Industrial Grade':'#5e98d9','Consumer Grade':'#b0b0b0','Extraordinary':'#ffd700'}[r]||'#fff';
  document.getElementById("dmi").innerHTML='<img src="'+img+'" alt="'+wn+' '+sn+'">';
  document.getElementById("dmd").innerHTML='<b>'+wn+'</b><h2>'+sn+'</h2><div class="dmdc"><div class="dmdl"><span>Weapon</span><strong>'+wn+'</strong></div><div class="dmdl"><span>Rarity</span><strong style="color:'+hex+'">'+r+'</strong></div></div><p style="color:var(--fg2);font-size:12px;line-height:1.6">Click below to view full market details, collection info, and more on CSGOSkins.gg</p>';
  var slug=(wn+' '+sn).toLowerCase().replace(/[|&]/g,'').replace(/\s+/g,'-').replace(/[^a-z0-9-]/g,'');
  document.getElementById("dml").href='https://csgoskins.gg/items/'+slug;
  document.getElementById("dms").href='https://steamcommunity.com/market/listings/730/'+encodeURIComponent(wn+' | '+sn);
  document.getElementById("dm").classList.add("s");document.body.style.overflow="hidden"
}
function closeDetail(){document.getElementById("dm").classList.remove("s");document.body.style.overflow=""}
document.getElementById("dm").addEventListener("click",function(e){if(e.target===this)closeDetail()});
document.addEventListener("click",function(e){
  var c=e.target.closest(".c");
  if(c&&!e.target.closest(".ov")&&!e.target.closest(".dmc")){e.preventDefault();showDetail(c)}
});
</script>'''
lines.append(js)
lines.append('</body></html>')

out = '\n'.join(lines)
with open('C:\\Users\\Student\\Desktop\\summer-school\\index.html', 'w', encoding='utf-8') as f:
    f.write(out)
print(f'Written {len(out)} bytes — {t} skins')
