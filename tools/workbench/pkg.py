import json,sys,re,shutil;sys.path.insert(0,'/tmp')
shutil.copy('/tmp/idx_base.html','/tmp/gh/index.html');shutil.copy('/tmp/ruc_base.json','/tmp/gh/ru-cases.json')
from st import *
V=sys.argv[1] if len(sys.argv)>1 else 'B'
K='\u2064'
HW=('Utility Hardware','A signature metal fastening element presented in its own accessory box.','Фирменный металлический элемент крепления в отдельной коробочке.')
PM=('Printed Matter','Edition card, collection booklet, hang tag and branded stickers.','Карточка выпуска, буклет коллекции, бирка и фирменные стикеры.')
PX=('Pouch & Extras','A reusable pouch, spare drawcords and additional hardware.','Многоразовый мешочек, дополнительные шнурки и фурнитура.')
IMG={'hw-file':('hd-hardware.webp','1400/1875'),'hw-crop':('hd-set-hardware.webp','324/376'),
     'pm-crop':('hd-set-printed.webp','1230/350'),'px-file':('hd-pouch.webp','1536/1024')}
VAR={'A':[('hw-file',HW),('px-file',PX)],
     'B':[('hw-file',HW),('pm-crop',PM),('px-file',PX)],
     'C':[('hw-crop',HW),('pm-crop',PM),('px-file',PX)],
     'D':[('hw-crop',HW),('pm-crop',PM),('px-file',PX)]}[V]
SQ=V=='D'
LEAD=('Beyond the garment.','Больше, чем одежда.')
INTRO=('A limited-edition collector set extends THE HOOD identity through functional accessories, custom hardware, printed materials and individually numbered packaging.',
       'Лимитированный коллекционный набор продолжает айдентику THE HOOD через функциональные аксессуары, фирменную фурнитуру, печатные материалы и индивидуальную нумерацию.')
BOX=('Presentation Box','A black box with burgundy accents and the edition number 01 / 10.','Чёрная коробка с бордовыми акцентами и номером выпуска 01 / 10.')
MAIN=('Full Collector Set','The complete limited-edition experience.','Полная композиция лимитированного набора.')
s,m,st=load()
p=[y for y in st['projects'] if y['slug']=='the-hood'][0];sp=p['subs'][0]
c=[x for x in sp['chapters'] if x['title'].startswith('Packaging Experience')][0]
c.update({'text':INTRO[0],'lead':LEAD[0],'vert':True,'media':[{'type':'image','src':'hd-box.webp','ratio':'2000/1493'},{'type':'image','src':'hd-collector-set.webp','ratio':'1448/1086'}],
 'pkg':{'main':[{'title':BOX[0],'text':BOX[1]},{'title':MAIN[0],'text':MAIN[1]}],'sq':SQ,'tiles':[{'src':IMG[k][0],'ratio':IMG[k][1],'title':t[0],'text':t[1]} for k,t in VAR]}})
c.pop('wide',None)
save(s,m,st)
h=open('/tmp/gh/index.html').read()
def rep(a,b,cnt=1):
    global h; assert h.count(a)==cnt,(a,h.count(a)); h=h.replace(a,b)
# 1) chapter -> row: lead line, vertical flag, packaging layout
rep("return [c.title,'<p>'+esc(c.text||'')+'</p>'+(c.stats",
    "return [c.title,(c.lead?'<p class=\"pkx-lead\">'+esc(c.lead)+'</p>':'')+'<p>'+esc(c.text||'')+'</p>'+(c.stats")
rep(",c.prods&&(c.media||[]).length?pjProds(c):",",c.pkg&&M.length?pjPkg(c):c.prods&&(c.media||[]).length?pjProds(c):")
rep(",!!c.wide,!!c.tight];});",",!!c.wide,!!c.tight,'',!!c.vert];});")
rep("(x[4]?' pj-tight':'')+'\" id=\"pj-'","(x[4]?' pj-tight':'')+(x[6]?' pj-vert':'')+'\" id=\"pj-'")
# 2) renderer + full-screen on click (only for this layout)
JS=r"""function pjPkg(c){var P=c.pkg||{},MM=c.media,PM=[].concat(P.main||[]),T=P.tiles||[],f=function(m,n,t,cls,ar){return '<figure class="pkx-f '+cls+'" data-r="'+esc(m.ratio)+'" tabindex="0" role="button" aria-label="'+esc(t.title)+'"><div class="pkx-im" style="aspect-ratio:'+esc(ar||m.ratio)+'"><img src="'+esc(m.src)+'" alt="'+esc(t.title)+'" loading="lazy" decoding="async"></div><figcaption><em>'+pad(n)+'</em><b>'+esc(t.title)+'</b><span>'+esc(t.text)+'</span></figcaption></figure>';};
 return '<div class="pkx"><div class="pkx-pair" style="--n:'+PM.length+'">'+PM.map(function(t,k){return f(MM[k],k+1,t,'pkx-main',PM.length>1?'4/3':'');}).join('')+'</div><div class="pkx-row" style="--n:'+T.length+'">'+T.map(function(t,k){return f(t,k+1+PM.length,t,'pkx-tile',P.sq?'1/1':'4/3');}).join('')+'</div></div>';}
document.addEventListener('click',function(e){var f=e.target.closest&&e.target.closest('.pkx-f');if(f)cfFull(f);});
document.addEventListener('keydown',function(e){var f=document.activeElement;if((e.key==='Enter'||e.key===' ')&&f&&f.classList&&f.classList.contains('pkx-f')){e.preventDefault();cfFull(f);}});
"""
rep("function pjParts(P){",JS+"function pjParts(P){")
# 3) CSS, scoped to the vertical chapter
CSS=(" .pj-sec.pj-vert{grid-template-columns:1fr!important;gap:0}"
 " .pj-sec.pj-vert .pj-txt{position:static;opacity:1;max-width:none}"
 " .pj-sec.pj-vert .pj-txt h2{white-space:nowrap}"
 " .pj-sec.pj-vert .pj-txt p{max-width:62ch}"
 " .pj-sec.pj-vert .pj-txt .pkx-lead{font-size:clamp(1.6rem,3vw,2.6rem);font-weight:600;letter-spacing:-.015em;line-height:1.15;color:var(--ink);margin:4px 0 16px;max-width:none}"
 " .pkx{margin-top:clamp(28px,3.5vw,48px)}"
 " .pkx-f{margin:0;cursor:zoom-in;outline:none}"
 " .pkx-f:focus-visible .pkx-im{box-shadow:0 0 0 2px #7fc4ff}"
 " .pkx-im{position:relative;border-radius:14px;overflow:hidden;background:#0b0b0d}"
 " .pkx-im img{position:absolute;inset:0;width:100%;height:100%;object-fit:contain;display:block;transition:transform .6s ease}"
 " .pkx-main .pkx-im img{object-fit:cover}"
 " @media (hover:hover){.pkx-f:hover .pkx-im img{transform:scale(1.015)}}"
 " .pkx-f figcaption{display:grid;grid-template-columns:auto 1fr;column-gap:12px;row-gap:2px;margin-top:12px}"
 " .pkx-f figcaption em{grid-row:span 2;font:500 .72rem ui-monospace,SFMono-Regular,Menlo,monospace;letter-spacing:.1em;color:#7fc4ff;font-style:normal;padding-top:4px}"
 " .pkx-f figcaption b{font-weight:600;font-size:.95rem;color:#fff}"
 " .pkx-f figcaption span{font-size:.86rem;line-height:1.45;color:#a9b4c6}"
 " .pkx-pair{display:grid;grid-template-columns:repeat(var(--n),1fr);gap:16px;align-items:start}"
 " .pkx-row{display:grid;grid-template-columns:repeat(var(--n),1fr);gap:16px;margin-top:clamp(36px,4vw,56px);align-items:start}"
 " @media (max-width:1100px) and (min-width:601px){.pkx-row{grid-template-columns:repeat(2,1fr)}.pkx-row .pkx-tile:nth-child(3):last-child{grid-column:1/-1;width:calc(50% - 8px)}}"
 " @media (max-width:900px){.pkx-pair{grid-template-columns:1fr;gap:28px}}"
 " @media (max-width:600px){.pkx-row{grid-template-columns:1fr;gap:28px;margin-top:28px}.pj-sec.pj-vert .pj-txt h2{white-space:normal}}")
k=h.find(" .mk-sec{display:block!important;");assert k>0
h=h[:k]+CSS+h[k:]
# old pouch rule no longer used in this chapter
h=h.replace(' .pj-sec figure:has(img[src$="hd-pouch.webp"]){max-width:62%;margin-left:auto}','')
# 4) phones: lighter main image
h=h.replace('<script type="application/json" id="smallmap">{','<script type="application/json" id="smallmap">{"hd-collector-set.webp":1,',1)
# 5) Russian
RU={BOX[1]:BOX[2],LEAD[0]:LEAD[1],INTRO[0]:INTRO[1],MAIN[1]:MAIN[2],HW[1]:HW[2],PM[1]:PM[2],PX[1]:PX[2]}
mm=re.search(r"var LANG='en',TITLE_EN='',RU=\{",h);i=mm.end()-1;j=h.find('};',i)
h=h[:j]+''.join(','+json.dumps(a,ensure_ascii=False)+':'+json.dumps(b,ensure_ascii=False) for a,b in RU.items())+h[j:]
open('/tmp/gh/index.html','w').write(h)
ruc=json.load(open('/tmp/gh/ru-cases.json'));ruc.update(RU)
json.dump(ruc,open('/tmp/gh/ru-cases.json','w'),ensure_ascii=False,separators=(',',':'))
print('ok',V)
