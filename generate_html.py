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
    return f'<div class="c" data-w="{wn.lower()}" data-r="{r}" data-n="{(wn+" | "+sn).lower()}"><div class="ci"><img src="{url}" alt="{wn} {sn}" loading="lazy"><div class="ch"></div></div><div class="cb"><span style="color:{h}">{r.upper()}</span><b>{wn}</b><span>{sn}</span></div></div>'

# --- BUILD CSS ---
css = '''<style>
*{margin:0;padding:0;box-sizing:border-box}html{scroll-behavior:smooth;background:#06060b}
body{font-family:system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;background:#06060b;color:#c0c0cc;min-height:100vh;line-height:1.5}
:root{--bg:#06060b;--bg2:#0c0c14;--bg3:#12121c;--bg4:#181824;--fg:#c0c0cc;--fg2:#888;--r1:#eb4b4b;--r2:#d32ce6;--r3:#8847ff;--r4:#4b69ff;--r5:#5e98d9;--r6:#b0b0b0;--r7:#ffd700;--bw:1px solid rgba(255,255,255,.04)}
.nv{height:56px;background:var(--bg);border-bottom:var(--bw);position:sticky;top:0;z-index:100}
.nv>div{max-width:1280px;margin:0 auto;padding:0 24px;height:100%;display:flex;align-items:center;justify-content:space-between}
.nvl{display:flex;gap:10px;align-items:center}
.nvg{width:30px;height:30px;border-radius:8px;background:var(--r1);color:#fff;font-weight:900;font-size:12px;display:flex;align-items:center;justify-content:center}
.nvt{font-weight:800;color:#fff;font-size:15px;letter-spacing:-.3px}
.nvb{font-size:9px;color:var(--fg2);background:var(--bg3);border:var(--bw);padding:2px 7px;border-radius:4px;font-weight:600;letter-spacing:.5px}
.nvr{display:none;gap:24px}@media(min-width:768px){.nvr{display:flex}}
.nvr a{color:var(--fg2);font-size:13px;text-decoration:none;transition:.2s;font-weight:500}
.nvr a:hover,.nvr a.sel{color:#fff}
.hr{background:linear-gradient(170deg,var(--bg) 0%,#0e0e1a 40%,#131326 100%);border-bottom:var(--bw);padding:80px 0 48px;position:relative;overflow:hidden}
.hr::after{content:"";position:absolute;top:-200px;left:50%;transform:translateX(-50%);width:600px;height:600px;border-radius:50%;background:radial-gradient(circle,rgba(235,75,75,.03) 0%,transparent 70%);pointer-events:none}
.hri{max-width:1280px;margin:0 auto;padding:0 24px;position:relative;z-index:1}
.hrt{display:inline-flex;align-items:center;gap:8px;padding:5px 14px;border-radius:24px;background:rgba(235,75,75,.06);border:1px solid rgba(235,75,75,.12);font-size:11px;color:var(--r1);font-weight:600;margin-bottom:16px}
.hrt span{width:6px;height:6px;border-radius:50%;background:var(--r1);animation:p 2s infinite}@keyframes p{50%{opacity:.3}}
.hrh{font-size:38px;font-weight:900;color:#fff;line-height:1.1;margin-bottom:10px;letter-spacing:-.5px}
.hrh em{font-style:normal;background:linear-gradient(135deg,var(--r1),#ff8c00);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}
.hrp{color:var(--fg2);font-size:14px;max-width:460px}
.st{background:var(--bg2);border-bottom:var(--bw)}
.st>div{max-width:1280px;margin:0 auto;padding:14px 24px;display:grid;grid-template-columns:repeat(4,1fr);gap:12px;text-align:center}
.stn{font-size:22px;font-weight:800;color:#fff}
.stl{font-size:10px;color:var(--fg2);text-transform:uppercase;letter-spacing:.5px;margin-top:2px}
.mn{max-width:1280px;margin:0 auto;padding:32px 24px 48px}
.sc{margin-bottom:40px}
.sch{display:flex;align-items:center;justify-content:space-between;margin-bottom:16px}
.sch-l{display:flex;align-items:center;gap:10px}
.sch-i{width:28px;height:28px;border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:14px}
.sch-t{font-size:17px;font-weight:800;color:#fff;letter-spacing:-.2px}
.sch-n{font-size:12px;color:var(--fg2);font-weight:500;background:var(--bg3);padding:2px 8px;border-radius:6px}
.sch-b{padding:8px 18px;border-radius:8px;background:transparent;border:1px solid rgba(235,75,75,.25);color:var(--r1);font-size:12px;font-weight:600;cursor:pointer;transition:.2s}
.sch-b:hover{background:rgba(235,75,75,.08);border-color:var(--r1)}
.gd{display:grid;grid-template-columns:repeat(auto-fill,minmax(180px,1fr));gap:12px}
.c{background:var(--bg2);border:var(--bw);border-radius:10px;overflow:hidden;transition:.25s;cursor:pointer}.c:hover{transform:translateY(-3px);border-color:rgba(255,255,255,.08);box-shadow:0 12px 40px rgba(0,0,0,.5)}.c.hide{display:none!important}
.ci{position:relative;aspect-ratio:4/3;background:linear-gradient(180deg,rgba(255,255,255,.015),transparent);display:flex;align-items:center;justify-content:center;padding:12px}
.ci img{width:100%;height:100%;object-fit:contain;transition:.35s;filter:drop-shadow(0 4px 12px rgba(0,0,0,.6))}.c:hover .ci img{transform:scale(1.06)}
.ch{position:absolute;inset:0;opacity:0;transition:.4s;background:linear-gradient(45deg,transparent 30%,rgba(255,255,255,.02) 50%,transparent 70%);pointer-events:none}.c:hover .ch{opacity:1}
.cb{padding:10px 12px 12px}
.cb span{display:block;font-size:9px;font-weight:700;letter-spacing:.4px;text-transform:uppercase;margin-bottom:4px}
.cb b{display:block;color:#fff;font-size:11px;font-weight:600;line-height:1.3}
.cb span:last-child{color:var(--fg2);font-size:10px;font-weight:500;text-transform:none;letter-spacing:0;margin-top:2px;margin-bottom:0}
.ov{position:fixed;inset:0;background:var(--bg);z-index:200;overflow-y:auto;display:none}.ov.s{display:block}
.ovt{position:sticky;top:0;z-index:10;background:var(--bg2);border-bottom:var(--bw);display:flex;align-items:center;justify-content:space-between;padding:12px 24px}
.ovtl{display:flex;align-items:center;gap:12px}
.ovb{padding:7px 14px;border-radius:8px;background:var(--bg3);border:1px solid rgba(255,255,255,.06);color:var(--fg2);font-size:12px;cursor:pointer;transition:.2s;display:flex;align-items:center;gap:5px}.ovb:hover{color:#fff;border-color:rgba(255,255,255,.15)}
.ovbt{font-weight:700;color:#fff;font-size:15px}
.ovbc{font-size:11px;color:var(--fg2)}
.ovf{background:var(--bg2);border-bottom:var(--bw);padding:20px 24px;display:flex;flex-direction:column;gap:14px}
.ovf>div{max-width:640px;margin:0 auto;width:100%}
.ovfs{position:relative}
.ovfs svg{position:absolute;left:14px;top:50%;transform:translateY(-50%);color:#444}
.ovfs input{width:100%;padding:11px 14px 11px 40px;border-radius:8px;border:1px solid rgba(255,255,255,.06);background:var(--bg3);color:#fff;font-size:14px;outline:none;transition:.2s}.ovfs input:focus{border-color:var(--r1)}.ovfs input::placeholder{color:#444}
.ovfg{display:flex;flex-direction:column;gap:8px}
.ovfl{font-size:9px;font-weight:700;color:#666;text-transform:uppercase;letter-spacing:1px;margin-bottom:2px}
.ovfr{display:flex;flex-wrap:wrap;gap:4px}
.fb{padding:4px 12px;border-radius:14px;border:1px solid rgba(255,255,255,.05);background:rgba(255,255,255,.02);font-size:10.5px;cursor:pointer;transition:all .2s;font-weight:500;color:#999;letter-spacing:.2px}
.fb:hover{border-color:rgba(255,255,255,.12);background:rgba(255,255,255,.04);color:#ccc}
.fb.off{opacity:.2;text-decoration:line-through;transform:scale(.96)}
.fbl{border-color:rgba(235,75,75,.2);color:var(--r1);font-weight:600;background:rgba(235,75,75,.04)}.fbl:hover{background:rgba(235,75,75,.1);color:#fff}
.ovff{display:flex;align-items:center;justify-content:space-between;padding-top:4px;border-top:1px solid rgba(255,255,255,.03)}
.ovrc{font-size:11px;color:var(--fg2)}
.ovg{padding:24px}
</style>'''
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
lines.append(f'<div class="st"><div><div><div class="stn">{t}+</div><div class="stl">Total Skins</div></div><div><div class="stn">7</div><div class="stl">Rarity Tiers</div></div><div><div class="stn">5</div><div class="stl">Wear Levels</div></div><div><div class="stn">10</div><div class="stl">Per Category</div></div></div></div>')

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

# JS
js = '''<script>
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
  if(e.key==="Escape"){document.querySelectorAll(".ov.s").forEach(function(o){o.classList.remove("s");document.body.style.overflow=""})}
});
</script>'''
lines.append(js)
lines.append('</body></html>')

out = '\n'.join(lines)
with open('C:\\Users\\Student\\Desktop\\summer-school\\index.html', 'w', encoding='utf-8') as f:
    f.write(out)
print(f'Written {len(out)} bytes — {t} skins')
