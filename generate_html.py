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

ra_info = {
    'Covert': '#eb4b4b', 'Classified': '#d32ce6',
    'Restricted': '#8847ff', 'Mil-Spec Grade': '#4b69ff',
    'Industrial Grade': '#5e98d9', 'Consumer Grade': '#b0b0b0',
    'Extraordinary': '#ffd700',
}
r_order = {'Covert':0,'Classified':1,'Restricted':2,'Mil-Spec Grade':3,'Industrial Grade':4,'Consumer Grade':5,'Extraordinary':0}

categories = [
    ('rifles','Rifles','🔫',['ak-47','m4a4','m4a1-s','awp','ssg 08','sg 553','aug','famas','galil ar','scar-20','g3sg1']),
    ('pistols','Pistols','🔫',['desert eagle','usp-s','glock-18','p2000','p250','cz75-auto','five-seven','tec-9','dual berettas','r8 revolver']),
    ('smgs','SMGs','⚡',['mac-10','mp9','mp5-sd','mp7','ump-45','p90','pp-bizon']),
    ('heavies','Heavy','💥',['mag-7','nova','xm1014','sawed-off','m249','negev']),
    ('knives','Knives','★',['karambit','butterfly knife','m9 bayonet','talon knife','bayonet','flip knife','shadow daggers','bowie knife','stiletto knife','ursus knife','nomad knife','skeleton knife','classic knife','gut knife','huntsman knife','falchion knife','navaja knife','paracord knife','survival knife','kukri knife']),
    ('gloves','Gloves','🧤',['hand wraps','sport gloves','moto gloves','driver gloves','specialist gloves','bloodhound gloves','broken fang gloves','hydra gloves']),
]

weapon_display = {'ak-47':'AK-47','m4a4':'M4A4','m4a1-s':'M4A1-S','awp':'AWP','ssg 08':'SSG 08','sg 553':'SG 553','aug':'AUG','famas':'FAMAS','galil ar':'Galil AR','scar-20':'SCAR-20','g3sg1':'G3SG1','desert eagle':'Deagle','usp-s':'USP-S','glock-18':'Glock','p2000':'P2000','p250':'P250','cz75-auto':'CZ75','five-seven':'Five-SeveN','tec-9':'Tec-9','dual berettas':'Dualies','r8 revolver':'R8','mac-10':'MAC-10','mp9':'MP9','mp5-sd':'MP5-SD','mp7':'MP7','ump-45':'UMP-45','p90':'P90','pp-bizon':'PP-Bizon','mag-7':'MAG-7','nova':'Nova','xm1014':'XM1014','sawed-off':'Sawed-Off','m249':'M249','negev':'Negev','karambit':'Karambit','butterfly knife':'Butterfly','m9 bayonet':'M9 Bayonet','talon knife':'Talon','bayonet':'Bayonet','flip knife':'Flip','shadow daggers':'Shadow D.','bowie knife':'Bowie','stiletto knife':'Stiletto','ursus knife':'Ursus','nomad knife':'Nomad','skeleton knife':'Skeleton','classic knife':'Classic','gut knife':'Gut','huntsman knife':'Huntsman','falchion knife':'Falchion','navaja knife':'Navaja','paracord knife':'Paracord','survival knife':'Survival','kukri knife':'Kukri','hand wraps':'Hand Wraps','sport gloves':'Sport','moto gloves':'Moto','driver gloves':'Driver','specialist gloves':'Specialist','bloodhound gloves':'Bloodhound','broken fang gloves':'Broken Fang','hydra gloves':'Hydra'}

cat_data = {}
for sid,title,icon,wp_list in categories:
    group = []
    for wl in wp_list:
        g = []
        for wn,sn,url,r in all_skins:
            if wn.lower() == wl:
                g.append((wn,sn,url,r))
        g.sort(key=lambda x: (r_order.get(x[3],99), x[1]))
        group.extend(g)
    cat_data[sid] = group

total = len(all_skins)
cols = {'rifles':'#eb4b4b','pistols':'#4b69ff','smgs':'#8847ff','heavies':'#5e98d9','knives':'#ffd700','gloves':'#b8860b'}
t = str(total)

lines = []
lines.append('<!DOCTYPE html><html lang=en><head><meta charset=UTF-8><meta name=viewport content="width=device-width,initial-scale=1.0"><title>CS2 Skin Vault</title>')
lines.append('<link rel=preconnect href="https://fonts.googleapis.com"><link rel=preconnect href="https://fonts.gstatic.com" crossorigin>')
lines.append('<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Orbitron:wght@400;500;600;700;800;900&display=swap" rel=stylesheet>')
lines.append('<style>*{box-sizing:border-box;margin:0;padding:0}html{scroll-behavior:smooth}body{font-family:Inter,sans-serif;background:#07070d;color:#ddd;line-height:1.5;-webkit-font-smoothing:antialiased}.f{font-family:Orbitron,sans-serif}:root{--r1:#eb4b4b;--r2:#d32ce6;--r3:#8847ff;--r4:#4b69ff;--r5:#5e98d9;--r6:#b0b0b0;--r7:#ffd700}.nv{position:fixed;top:0;left:0;width:100%;height:60px;z-index:100;background:rgba(7,7,13,.92);backdrop-filter:blur(16px);border-bottom:1px solid rgba(255,255,255,.04)}.nvi{max-width:1200px;margin:0 auto;padding:0 20px;height:100%;display:flex;align-items:center;justify-content:space-between}.nvl{display:flex;align-items:center;gap:10px}.nvg{width:30px;height:30px;border-radius:6px;background:var(--r1);display:flex;align-items:center;justify-content:center;color:#fff;font-size:11px;font-weight:900;font-family:Orbitron,sans-serif}.nvt{font-family:Orbitron,sans-serif;font-size:14px;font-weight:700;color:#fff}.nvb{padding:2px 7px;border-radius:4px;background:rgba(255,255,255,.04);font-size:9px;color:#555;border:1px solid rgba(255,255,255,.04)}.nvr{display:none;gap:20px}@media(min-width:768px){.nvr{display:flex}}.nvr a{color:#555;font-size:13px;text-decoration:none;transition:color .2s}.nvr a:hover{color:#eee}.hr{background:linear-gradient(160deg,#07070d,#0c0c18,#121225);position:relative;overflow:hidden;padding:100px 0 60px}.hr::before{content:"";position:absolute;inset:0;background:radial-gradient(ellipse at 30% 50%,rgba(235,75,75,.07) 0%,transparent 70%),radial-gradient(ellipse at 70% 50%,rgba(136,71,255,.05) 0%,transparent 60%);pointer-events:none}.hri{max-width:1200px;margin:0 auto;padding:0 20px;position:relative;z-index:1}.hrt{display:inline-flex;align-items:center;gap:6px;padding:5px 14px;border-radius:20px;background:rgba(235,75,75,.08);border:1px solid rgba(235,75,75,.15);margin-bottom:16px;font-size:11px;color:var(--r1);font-weight:600}.hrh{font-size:34px;font-weight:900;color:#fff;line-height:1.15;margin-bottom:12px}.hrp{color:#555;font-size:14px;max-width:450px;line-height:1.6}.st{background:#0c0c18;border-bottom:1px solid rgba(255,255,255,.04);padding:12px 0}.sti{max-width:1200px;margin:0 auto;padding:0 20px;display:grid;grid-template-columns:repeat(4,1fr);gap:8px;text-align:center}.stn{font-size:18px;font-weight:800;color:#fff;font-family:Orbitron,sans-serif}.stl{font-size:10px;color:#555;margin-top:2px}.mn{max-width:1200px;margin:0 auto;padding:24px 20px}.sc{margin-bottom:36px}.sch{display:flex;align-items:center;justify-content:space-between;margin-bottom:16px;padding-bottom:12px;border-bottom:1px solid rgba(255,255,255,.04)}.schl{display:flex;align-items:center;gap:8px}.sci{width:26px;height:26px;border-radius:6px;display:flex;align-items:center;justify-content:center;font-size:13px}.sct{font-size:16px;font-weight:700;color:#fff;font-family:Orbitron,sans-serif}.scc{font-size:11px;color:#555}.scv{padding:8px 18px;border-radius:8px;border:1px solid var(--r1);color:var(--r1);font-size:12px;cursor:pointer;background:transparent;transition:all .25s;font-weight:600}.scv:hover{background:rgba(235,75,75,.08)}.gd{display:grid;grid-template-columns:repeat(2,1fr);gap:10px}@media(min-width:500px){.gd{grid-template-columns:repeat(3,1fr)}}@media(min-width:700px){.gd{grid-template-columns:repeat(4,1fr)}}@media(min-width:900px){.gd{grid-template-columns:repeat(5,1fr)}}.c{background:#0c0c18;border-radius:8px;overflow:hidden;border:1px solid rgba(255,255,255,.04);transition:all .3s;cursor:pointer}.c:hover{transform:translateY(-3px);border-color:rgba(255,255,255,.08);box-shadow:0 8px 30px rgba(0,0,0,.4)}.c.hide{display:none!important}.ci{background:linear-gradient(180deg,rgba(255,255,255,.02),transparent);display:flex;align-items:center;justify-content:center;padding:8px;aspect-ratio:16/10}.ci img{width:100%;height:100%;object-fit:contain;transition:transform .35s;filter:drop-shadow(0 3px 10px rgba(0,0,0,.5))}.c:hover .ci img{transform:scale(1.05)}.cb{padding:8px 10px 10px}.cr{font-size:8px;font-weight:700;letter-spacing:.5px;text-transform:uppercase}.cn{color:#fff;font-size:11px;font-weight:600;line-height:1.35;margin-top:3px}.cato{position:fixed;inset:0;background:#07070d;z-index:200;overflow-y:auto;display:none}.cato.show{display:block}.cath{position:sticky;top:0;z-index:10;background:#0c0c18;border-bottom:1px solid rgba(255,255,255,.06);display:flex;align-items:center;justify-content:space-between;padding:12px 20px}.cathl{display:flex;align-items:center;gap:10px}.catb{display:flex;align-items:center;gap:6px;padding:8px 16px;border-radius:8px;border:1px solid rgba(255,255,255,.08);color:#aaa;font-size:12px;cursor:pointer;background:transparent;transition:all .2s}.catb:hover{border-color:var(--r1);color:var(--r1)}.catt{font-family:Orbitron,sans-serif;font-size:15px;font-weight:700;color:#fff}.catf{background:#0c0c18;border-bottom:1px solid rgba(255,255,255,.04);padding:12px 20px}.sw{position:relative}.sw svg{position:absolute;left:14px;top:50%;transform:translateY(-50%);color:#444}.sw input{width:100%;padding:13px 16px 13px 44px;border-radius:10px;border:1px solid rgba(255,255,255,.06);background:rgba(255,255,255,.03);color:#fff;font-size:15px;outline:none;transition:border .25s}.sw input:focus{border-color:var(--r1)}.sw input::placeholder{color:#444}.ftr{display:flex;flex-wrap:wrap;align-items:center;gap:6px}.ftl{color:#444;font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.5px;margin-right:6px;min-width:42px}.fb{padding:5px 14px;border-radius:20px;border:1px solid rgba(255,255,255,.06);background:transparent;font-size:11px;cursor:pointer;transition:all .2s;color:#999}.fb:hover{border-color:rgba(255,255,255,.15);color:#ddd}.fb.off{opacity:.15;text-decoration:line-through}.fbr{color:var(--r1);border-color:rgba(235,75,75,.3);font-weight:600}.fbr:hover{background:rgba(235,75,75,.08)}.cato .gd{gap:10px}@media(min-width:500px){.cato .gd{grid-template-columns:repeat(3,1fr)}}@media(min-width:700px){.cato .gd{grid-template-columns:repeat(4,1fr)}}@media(min-width:1000px){.cato .gd{grid-template-columns:repeat(5,1fr)}}@media(min-width:1200px){.cato .gd{grid-template-columns:repeat(6,1fr)}}.catg{padding:20px}.catc{font-size:11px;color:#555;margin-top:12px;text-align:center}.ftr2{background:#0c0c18;border-top:1px solid rgba(255,255,255,.04);padding:28px 20px;text-align:center}.ftr2 p{color:#444;font-size:11px;max-width:400px;margin:0 auto;line-height:1.6}</style></head><body>')

# Navbar
lines.append('<nav class=nv><div class=nvi><div class=nvl><span class=nvg>CS</span><span class=nvt>Skin Vault</span><span class=nvb>v2.0</span></div><div class=nvr><a href=#s-rifles>Rifles</a><a href=#s-pistols>Pistols</a><a href=#s-smgs>SMGs</a><a href=#s-heavies>Heavy</a><a href=#s-knives>Knives</a><a href=#s-gloves>Gloves</a></div></nav>')
lines.append('<div class=hr><div class=hri><div class=hrt>Complete Armory &bull; '+t+' finishes</div><h1 class=hrh>CS2 <span style="background:linear-gradient(135deg,var(--r1),#ff8c00);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text">Skin Vault</span></h1><p class=hrp>10 skins per category. Click View All to explore with search and filters.</p></div></div>')
lines.append('<div class=st><div class=sti><div><div class=stn>'+t+'+</div><div class=stl>Total Skins</div></div><div><div class=stn>7</div><div class=stl>Rarity Tiers</div></div><div><div class=stn>5</div><div class=stl>Wear Levels</div></div><div><div class=stn>10</div><div class=stl>Per Category</div></div></div></div>')

lines.append('<div class=mn>')

def card(wn,sn,url,r):
    h = ra_info.get(r,'#fff')
    return '<div class=c data-w="'+wn.lower()+'" data-r="'+r+'" data-n="'+(wn+' | '+sn).lower()+'"><div class=ci><img src="'+url+'" alt="'+wn+' '+sn+'" loading=lazy></div><div class=cb><span class=cr style=color:'+h+'>'+r.upper()+'</span><h3 class=cn>'+wn+'<br>'+sn+'</h3></div></div>'

for sid,title,icon,wp_list in categories:
    group = cat_data[sid]
    total_cat = len(group)
    preview = group[:10]
    pc = ''.join(card(*s) for s in preview)
    ac = ''.join(card(*s) for s in group)
    
    lines.append('<div class=sc id=s-'+sid+'><div class=sch><div class=schl><div class=sci style=background:'+cols[sid]+'15;color:'+cols[sid]+'>'+icon+'</div><span class=sct>'+title+'</span><span class=scc>'+str(total_cat)+'</span></div><button class=scv onclick="openCat(\''+sid+'\')">View All '+str(total_cat)+' &rarr;</button></div><div class=gd>'+pc+'</div></div>')
    
    # Catalog - No inline onclick for filter toggles! Uses event delegation instead
    lines.append('<div class=cato id=cato-'+sid+'><div class=cath><div class=cathl><button class=catb onclick="closeCat(\''+sid+'\')">&larr; Back</button><span class=catt>'+icon+' '+title+'</span></div><span style=color:#555;font-size:12px>'+str(total_cat)+' skins</span></div>')
    lines.append('<div class=catf><div class=sw><svg width=16 height=16 fill=none stroke=currentColor viewBox="0 0 24 24"><path stroke-linecap=round stroke-linejoin=round stroke-width=2 d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg><input type=text class=cgi data-cat='+sid+' placeholder="Search in '+title+'..." oninput=cf(this)></div>')
    lines.append('<div class=ftr><span class=ftl>Rarity</span>')
    for rn in ['Covert','Classified','Restricted','Mil-Spec Grade','Industrial Grade','Consumer Grade']:
        c = {'Covert':'#eb4b4b','Classified':'#d32ce6','Restricted':'#8847ff','Mil-Spec Grade':'#4b69ff','Industrial Grade':'#5e98d9','Consumer Grade':'#b0b0b0'}[rn]
        ln = rn.replace('Mil-Spec Grade','Mil-Spec').replace('Industrial Grade','Industrial').replace('Consumer Grade','Consumer')
        lines.append('<button class="fb cfr" data-cat='+sid+' data-r="'+rn+'" style=color:'+c+'>'+ln+'</button>')
    lines.append('</div><div class=ftr style=margin-top:6px><span class=ftl>Weapon</span>')
    for wl in wp_list:
        dn = weapon_display.get(wl, wl.title())
        lines.append('<button class="fb cfw" data-cat='+sid+' data-w="'+wl+'">'+dn+'</button>')
    lines.append('</div><div class=ftr style=margin-top:8px><span class=crc id=crc-'+sid+' style=color:#555;font-size:11px;margin-right:12px>'+str(total_cat)+' matching</span><button class="fb fbr" onclick="resetCat(\''+sid+'\')">Reset</button></div></div>')
    lines.append('<div class=catg><div class=gd id=cg-'+sid+'>'+ac+'</div><div class=catc id=cem-'+sid+'></div></div></div>')

lines.append('</div>')
lines.append('<div class=ftr2><p>CS2 Skin Vault &bull; Not affiliated with Valve Corporation</p></div>')

# JS with event delegation - NO inline onclick on filter toggles
js = '''<script>
function openCat(cid){
  document.querySelectorAll(".cato").forEach(function(o){o.classList.remove("show")});
  document.getElementById("cato-"+cid).classList.add("show");
  document.body.style.overflow="hidden";
  var inp=document.querySelector(".cgi[data-cat="+JSON.stringify(cid)+"]");
  if(inp)cf(inp)
}
function closeCat(cid){
  document.getElementById("cato-"+cid).classList.remove("show");
  document.body.style.overflow=""
}
function cf(inp){
  var cid=inp.dataset.cat;
  var s=inp.value.toLowerCase().trim();
  var rbs=document.querySelectorAll("#cato-"+cid+" .cfr");
  var wbs=document.querySelectorAll("#cato-"+cid+" .cfw");
  var ar=new Set();rbs.forEach(function(b){if(!b.classList.contains("off"))ar.add(b.dataset.r)});
  var aw=new Set();wbs.forEach(function(b){if(!b.classList.contains("off"))aw.add(b.dataset.w)});
  var cards=document.querySelectorAll("#cg-"+cid+" .c");
  var v=0;
  cards.forEach(function(cd){
    var w=cd.dataset.w;var r=cd.dataset.r;var n=cd.dataset.n;
    if((!s||n.indexOf(s)!==-1)&&(ar.size===0||ar.has(r))&&(aw.size===0||aw.has(w))){cd.classList.remove("hide");v++}
    else{cd.classList.add("hide")}
  });
  var el=document.getElementById("crc-"+cid);
  if(el)el.textContent=v+" matching";
  var em=document.getElementById("cem-"+cid);
  if(em)em.textContent=v===0?"No skins match your filters":""
}
function resetCat(cid){
  var inp=document.querySelector(".cgi[data-cat="+JSON.stringify(cid)+"]");
  if(inp)inp.value="";
  document.querySelectorAll("#cato-"+cid+" .cfr.off, #cato-"+cid+" .cfw.off").forEach(function(b){b.classList.remove("off")});
  var inp2=document.querySelector(".cgi[data-cat="+JSON.stringify(cid)+"]");
  if(inp2)cf(inp2)
}
document.addEventListener("click",function(e){
  var btn=e.target;
  if(btn.classList.contains("cfr")||btn.classList.contains("cfw")){
    btn.classList.toggle("off");
    var cid=btn.dataset.cat;
    var inp=document.querySelector(".cgi[data-cat="+JSON.stringify(cid)+"]");
    if(inp)cf(inp);
  }
});
document.addEventListener("keydown",function(e){
  if(e.key==="Escape"){
    document.querySelectorAll(".cato.show").forEach(function(o){o.classList.remove("show");document.body.style.overflow=""})
  }
});
</script>'''
lines.append(js)
lines.append('</body></html>')

with open('C:\\Users\\Student\\Desktop\\summer-school\\index.html', 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))

print('Written: ' + str(len('\n'.join(lines))) + ' bytes, ' + t + ' skins')
