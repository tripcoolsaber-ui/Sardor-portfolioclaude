import json,sys,re;sys.path.insert(0,'/tmp');from st import *
K='\u2064'
TT=[('Brand Concept','Концепция бренда'),('Visual Identity','Айдентика'),('Campaign','Рекламная кампания'),('Garment Design','Дизайн худи'),('Materials & Details','Материалы и детали'),('Packaging Experience','Упаковка')]
T={t:(t+K,r) for t,r in TT}
TX={
'Brand Concept':("THE HOOD explores the idea of clothing as a personal statement.\n\nI approached the project as a connected identity, where the silhouette, graphic artwork and functional elements work together to create a distinctive visual character.",
 "THE HOOD исследует идею одежды как формы личного самовыражения.\n\nЯ рассматривал проект как единую систему, в которой силуэт, авторская графика и функциональные элементы формируют узнаваемый характер бренда."),
'Visual Identity':("The emblem depicts a hooded figure with a concealed face — a visual symbol of anonymity and personal freedom.\n\nThe wordmark combines lighter and heavier lettering, creating a recognizable contrast between restraint and strength.",
 "Фирменный знак изображает фигуру в капюшоне со скрытым лицом — визуальный символ анонимности и личной свободы.\n\nЛоготип сочетает лёгкое и акцентное начертания, формируя контраст между сдержанностью и силой."),
'Campaign':("The campaign places a solitary figure against expansive urban and natural environments.\n\nThe contrast in scale emphasizes the brand's independent character, while the garment and its artwork remain the central visual subjects.",
 "Рекламная концепция строится на контрасте одинокой фигуры и масштабного городского или природного окружения.\n\nЭтот приём подчёркивает независимый характер бренда, сохраняя одежду и авторскую графику главными объектами композиции."),
'Garment Design':("The garment concept combines an oversized silhouette, utilitarian detailing and a prominent back-panel artwork.\n\nThe graphics work with the garment's construction rather than functioning as a separate logo placement.",
 "Концепция худи объединяет объёмный силуэт, утилитарные детали и крупную художественную композицию на спине.\n\nГрафика взаимодействует с конструкцией изделия, а не используется как отдельное размещение логотипа."),
'Materials & Details':("The garment's character extends into fabric, stitching, labels and industrial-inspired hardware.\n\nThese elements introduce a consistent material language, with the emblem used as a discreet signature rather than a dominant graphic.",
 "Характер изделия раскрывается через ткань, швы, ярлыки и фурнитуру с индустриальным характером.\n\nЭти элементы формируют единый материальный язык, в котором фирменный символ используется как деликатная деталь, а не доминирующая графика."),
'Packaging Experience':("The packaging extends the collection beyond the garment.\n\nA black presentation box, burgundy accents and an individually numbered edition concept establish a collectible unboxing experience. A reusable pouch completes the system through understated branding and functional design.",
 "Упаковка продолжает концепцию коллекции за пределами самой одежды.\n\nЧёрная подарочная коробка, бордовые акценты и идея индивидуальной нумерации создают коллекционный опыт распаковки. Многоразовый мешочек завершает систему благодаря сдержанному брендингу и функциональности."),
}
DESC=("THE HOOD is a self-initiated streetwear concept built around distinctive silhouettes, expressive artwork and considered functional details.\n\nRather than relying on prominent logos, the brand develops its character through the garment itself and extends it into a collectible packaging experience.",
 "THE HOOD — авторская концепция streetwear-бренда, основанная на выразительных силуэтах, оригинальной графике и продуманных функциональных деталях.\n\nВместо крупных логотипов характер бренда раскрывается через саму одежду и продолжается в коллекционной упаковке.")
SUB=("Limited Edition Streetwear Concept","Концепция лимитированной streetwear-коллекции")
ROLE=("Art Direction · Brand Identity · Garment Graphics · Packaging Design","Арт-дирекшн · Айдентика · Графика для одежды · Дизайн упаковки")
IND=("Fashion / Streetwear","Мода / Streetwear")
DEL=("Brand Identity · Key Visuals · Garment Design · Hardware · Packaging","Айдентика · Ключевые визуалы · Дизайн одежды · Фурнитура · Упаковка")
C=["Art Direction","Brand Identity","Garment Graphics","Key Visuals","Hardware & Packaging Concept"]
PARTS=[("hd-part-hood.webp","634/709","The Symbol","Символ","A hooded figure creates a recognizable visual signature.","Фигура в капюшоне формирует узнаваемый фирменный символ."),
       ("hd-part-word.webp","1666/456","The Wordmark","Название","Contrasting letterforms give the name its visual character.","Контраст начертаний придаёт названию характер."),
       ("hd-part-line.webp","931/100","The Tagline","Слоган","A concise reference to the limited-edition concept.","Краткое отражение идеи лимитированной коллекции.")]
s,m,st=load()
p=[y for y in st['projects'] if y['slug']=='the-hood'][0];sp=p['subs'][0]
by={c['title']:c for c in sp['chapters']}
logo=by['The Logo']
med=lambda t:by[t]['media']
NEW=[{'title':T['Brand Concept'][0],'text':TX['Brand Concept'][0],'media':med('Overview'),'gal':True},
     {'title':T['Visual Identity'][0],'text':TX['Visual Identity'][0],'media':[],'anno':dict(logo['anno'],pts=[],symbols=''),'parts':[{'src':a,'ratio':b,'title':c,'text':e} for a,b,c,d,e,f in PARTS]},
     {'title':T['Campaign'][0],'text':TX['Campaign'][0],'media':[{'type':'image','src':'hd-cover-2.webp','ratio':'1679/937'}],'gal':True,'wide':True},
     {'title':T['Garment Design'][0],'text':TX['Garment Design'][0],'media':med('Lookbook'),'gal':True},
     {'title':T['Materials & Details'][0],'text':TX['Materials & Details'][0],'media':med('Details')+med('Utility Hardware'),'gal':True,'wide':True},
     {'title':T['Packaging Experience'][0],'text':TX['Packaging Experience'][0],'media':med('Packaging')+med('Pouch'),'gal':True,'wide':True}]
sp['chaptersHidden']=(sp.get('chaptersHidden') or [])+sp['chapters']
sp['chapters']=NEW
sp.update({'sub':SUB[0],'subSmall':True,'desc':DESC[0],'role':ROLE[0],'industry':IND[0],'deliverables':DEL[0],'contrib':'\n'.join(C),'keepRole':True,'selfInit':True,'cardDesc':DESC[0].split('\n\n')[0]})
save(s,m,st)
RU={}
for t,(k,r) in T.items(): RU[k]=r
for t,(e,r) in TX.items(): RU[e]=r
for e,r in [DESC,SUB,ROLE,IND,DEL,(DESC[0].split('\n\n')[0],DESC[1].split('\n\n')[0])]: RU[e]=r
for a,b,c,d,e,f in PARTS: RU[c]=d;RU[e]=f
h=open('/tmp/gh/index.html').read()
mm=re.search(r"var LANG='en',TITLE_EN='',RU=\{",h);i=mm.end()-1;j=h.find('};',i);json.loads(h[i:j+1])
h=h[:j]+''.join(','+json.dumps(k,ensure_ascii=False)+':'+json.dumps(v,ensure_ascii=False) for k,v in RU.items())+h[j:]
# pouch is an accessory: smaller than the box, aligned right
css=" .pj-sec figure:has(img[src$=\"hd-pouch.webp\"]){max-width:62%;margin-left:auto}"
k=h.find(" .mk-sec{display:block!important;");assert k>0
if css not in h: h=h[:k]+css+h[k:]
open('/tmp/gh/index.html','w').write(h)
ruc=json.load(open('/tmp/gh/ru-cases.json'));over=[k for k in RU if k in ruc]
for k in over: ruc[k]=RU[k]
json.dump(ruc,open('/tmp/gh/ru-cases.json','w'),ensure_ascii=False,separators=(',',':'))
print('chapters',len(NEW),'| RU entries',len(RU),'| ru-cases overrides',len(over))
