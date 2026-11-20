import json,sys,html as H;sys.path.insert(0,'/tmp');from st import *
RU={}
import re as _re
_src=open('/tmp/gh/index.html').read();_m=_re.search(r"var LANG='en',TITLE_EN='',RU=\{",_src);_i=_m.end()-1;_j=_src.find('};',_i);RU_OLD=json.loads(_src[_i:_j+1])
def T(en,ru=None):
    RU[en]=en if ru is None else ru
    return H.escape(en,quote=False)
def img(src,ratio,alt=''):
    return f'<figure class="pj-im mk2-im" style="aspect-ratio:{ratio}"><img src="{src}" alt="{H.escape(alt)}" loading="lazy" decoding="async"></figure>'
def bx(src,W,Hh,box,alt):
    x0,y0,x1,y1=box;w=x1-x0;h=y1-y0;ar=(W*w)/(Hh*h)
    px=0 if w>=1 else x0/(1-w)*100;py=0 if h>=1 else y0/(1-h)*100
    return f'<div class="mk2-bx" role="img" aria-label="{H.escape(alt)}" style="aspect-ratio:{ar:.4f};background-image:url({src});background-size:{100/w:.3f}% auto;background-position:{px:.2f}% {py:.2f}%"></div>'
def det(sum_en,sum_ru,items,note=None,cls=''):
    s='<div class="mk2-rat '+cls+'"><span class="mk2-rat-h">'+T(sum_en,sum_ru)+'</span><ul>'+''.join('<li>'+T(e,r)+'</li>' for e,r in items)+'</ul>'
    if note: s+='<p class="mk2-cap">'+T(*note)+'</p>'
    return s+'</div>'
def eb(n,en,ru): return f'<div class="mk2-eb"><span>{n}</span>{T(en,ru)}</div>'
def pair(items,cap):
    q=lambda r:(lambda a,b:a/b)(*map(float,r.split('/')))
    return '<div class="mk2-pair">'+''.join(f'<figure class="mk2-pi" style="--q:{q(r):.4f}">'+img(s,r,n)+'<figcaption>'+T(n)+'</figcaption></figure>' for s,r,n in items)+'</div>'
S=[];FULL={}
CAR=[{'type':'image','src':f'mk2-poster-{k}.webp','ratio':'1300/1741','title':t} for k,t in [('kefir','Kefir — Lightness & Balance'),('milk','Milk — Pure Goodness'),('jogurt','Jogurt — Berry Delicacy'),('smietana','Śmietana — Smooth Indulgence'),('maslo','Masło — Creamy Perfection'),('twarog','Twaróg — Everyday Goodness')]]
# 01 Concept
L=eb('01','Concept\u2060','Концепция')+'<h3 class="mk2-h">'+T("Looks premium. Feels close.","Выглядит дорого. Ощущается близко.")+'</h3><p class="mk2-p">'+T("The concept explores how a new dairy brand could stand out through a distinctive visual identity without losing the warmth and familiarity of everyday products.","Концепция исследует, как новый молочный бренд может выделиться благодаря узнаваемой айдентике, сохраняя тепло и близость повседневных продуктов.")+'</p>'
L+='<ul class="mk2-pr">'+''.join('<li>'+T(e,r)+'</li>' for e,r in [('Recognition','Узнаваемость'),('Clarity','Понятность'),('Trust\u2060','Доверие')])+'</ul>'
RAT=det('Strategy & Rationale','Стратегия и обоснование',[
 ("Market context: established Polish dairy brands create a competitive environment for a new entrant.","Рыночный контекст: известные польские молочные бренды создают конкурентную среду для новой марки."),
 ("Audience hypothesis: families and urban consumers who value quality, clear information and everyday care.","Гипотеза аудитории: семьи и городские покупатели, для которых важны качество, понятная информация и повседневная забота."),
 ("Positioning: approachable premium, not price-led mass market or distant luxury.","Позиционирование: доступный премиум — не ценовой массовый сегмент и не дистанцированный люкс."),
 ("Design implication: recognizable color, friendly identity and clear product hierarchy.","Вывод для дизайна: узнаваемый цвет, дружелюбная айдентика и понятная иерархия продукта.")],
 ("Market context and audience are hypotheses of a concept project, not verified research.","Рыночный контекст и аудитория — гипотезы концептуального проекта, а не подтверждённые исследования."),'mk2-rat-row mk2-rat-4')
R='<div class="mk2-wp mk2-bod">Warm<br>Premium.</div>'+RAT
S.append(('Concept\u2060',L,R,''))
# 02 Identity
OLD=json.load(open('/tmp/mk_old.json'))
L=eb('02','Brand Identity\u2060','Айдентика')+'<h3 class="mk2-h">'+T('The Logo','Логотип')+'</h3><p class="mk2-p">'+T(OLD['logo']['text'],None if False else RU_OLD.get(OLD['logo']['text'],OLD['logo']['text']))+'</p>'
R='<!--ANNO-->'
CB='<div class="mk2-idrow"><span class="mk2-rat-h">'+T('Color','Цвет')+'</span><div class="mk2-sw">'+''.join(f'<figure><i style="background:{c}"></i><figcaption>{T(n)}</figcaption></figure>' for c,n in [('#5a0a6e','Primary Purple'),('#b27ebf','Lilac'),('#ede4e3','Cream'),('#3b9211','Nature Accents')])+'</div></div>'
TS=[('Display','Display','Pure Goodness','mk2-ts-d','Poster headlines','Заголовки постеров','Bold 700'),
    ('Product','Название продукта','Jogurt','mk2-ts-p','Product names on packs','Названия продуктов на упаковке','Semibold 600'),
    ('Accent','Акцент','Lightness & Balance','mk2-ts-a','Secondary lines and taglines','Подзаголовки и слоганы','Italic 400')]
TB='<div class="mk2-idrow"><span class="mk2-rat-h">'+T('Typography','Типографика')+' · Bodoni Moda</span><ul class="mk2-ts">'+''.join(f'<li><span class="mk2-ts-l">{T(l,lr)}</span><span class="mk2-ts-s mk2-bod {c}">{H.escape(smp)}</span><span class="mk2-ts-u">{T(u,ur)}</span><span class="mk2-ts-m">{H.escape(meta)}</span></li>' for l,lr,smp,c,u,ur,meta in TS)+'<li><span class="mk2-ts-l">'+T('Logo','Логотип')+'</span><span class="mk2-ts-s"><img src="mk-part-word.webp" alt="MilkKalina wordmark" loading="lazy" decoding="async"></span><span class="mk2-ts-u">'+T('Custom lettering, used in the logo only','Авторский леттеринг, только в логотипе')+'</span><span class="mk2-ts-m">'+T('Custom','Авторский')+'</span></li></ul></div>'
FULL['Brand Identity\u2060']='<div class="mk2-full mk2-idgrid"><div class="mk2-idparts"><!--PARTS--></div><div class="mk2-idcolor">'+CB+'</div></div><div class="mk2-full">'+TB+'</div>'
S.append(('Brand Identity\u2060',L,R,'logo'))
# 03 Packaging
L=eb('03','Packaging System\u2060','Упаковочная система')+'<h3 class="mk2-h">'+T("One identity. Six products.","Одна айдентика. Шесть продуктов.")+'</h3><p class="mk2-p">'+T("A flexible visual system connects six dairy products across different packaging formats through consistent branding, product naming and graphic elements.","Гибкая визуальная система объединяет шесть молочных продуктов с разными форматами упаковки через единый фирменный знак, названия и графические элементы.")+'</p>'
R=det('Packaging Rationale','Обоснование упаковки',[
 ("What remains consistent: logo, typography, color and product identification.","Что остаётся неизменным: логотип, типографика, цвет и идентификация продукта."),
 ("What changes: proportions, label composition, package construction and product-specific imagery.","Что меняется: пропорции, композиция этикетки, конструкция упаковки и изображения конкретного продукта."),
 ("What this demonstrates: the same identity can adapt to different physical formats.","Что это показывает: одна айдентика адаптируется к разным физическим форматам.")],None,'mk2-rat-row mk2-rat-3')
G=[('Glass Bottles','Стеклянные бутылки',"A shared glass-bottle format: milk keeps the label restrained, kefir adds its own name and 2.5% fat marking.","Общая стеклянная бутылка: у молока сдержанная этикетка, у кефира — своё название и маркировка жирности 2,5%.",[('mk-milk.webp','1086/1448','Milk'),('mk-kefir-2.webp','1400/1875','Kefir')]),
 ('Dairy Cups','Стаканчики',"Cups give room for expressive milk-splash graphics: blueberries mark the yogurt flavor, sour cream focuses on texture.","Стаканчики дают место выразительной графике всплесков: черника обозначает вкус йогурта, у сметаны акцент на текстуре.",[('mk-yogurt.webp','1122/1402','Yogurt'),('mk-sourcream-2.webp','1086/1448','Sour Cream')]),
 ('Alternative Formats','Альтернативные форматы',"The identity adapts to a wrapped block and a stand-up pouch, with the logo and typography placed for each surface.","Айдентика адаптирована к обёртке бруска и стоячему пакету: логотип и типографика размещены с учётом каждой поверхности.",[('mk-butter-2.webp','1086/1448','Butter'),('mk-cottage.webp','1122/1402','Cottage Cheese\u2060')])]
SC={'milk':1.0,'kefir':1.0,'jogurt':.44,'smietana':.42,'twarog':.64,'maslo':.27}
NM={'milk':'Milk','kefir':'Kefir','jogurt':'Jogurt','smietana':'Śmietana','twarog':'Twaróg','maslo':'Masło'}
GK=[['milk','kefir'],['jogurt','smietana'],['maslo','twarog']]
def can(k,h): return f'<div class="po-can" style="--h:{h:.4f}"><img src="mk2-prod-{k}.webp" alt="{NM[k]} pack" loading="lazy" decoding="async"><img class="po-r" src="mk2-prod-{k}.webp" alt="" aria-hidden="true" loading="lazy" decoding="async"></div>'
HERO=[]
for gi,ks in enumerate(GK):
    if gi: HERO.append('<span class="po-sep" aria-hidden="true"></span>')
    HERO+=[can(k,SC[k]) for k in ks]
CAPS=''.join('<div><span class="po-lbl">'+T(a,b)+'</span><p class="po-cap">'+T(e,r)+'</p></div>' for a,b,e,r,it in G)
LB=[('mk2-label-milk-2.webp','2000/667',"Milk — wrap-around label · 1 l","Молоко — круговая этикетка · 1 л"),
    ('mk2-label-kefir.webp','2000/772',"Kefir — wrap-around label · 1 l","Кефир — круговая этикетка · 1 л")]
def lab(src,r,en,ru,cls=''): return '<figure class="lb-it '+cls+'"><div class="lb-im" style="aspect-ratio:'+r+'"><img src="'+src+'" alt="" loading="lazy" decoding="async"></div><figcaption>'+T(en,ru)+'</figcaption></figure>'
LBL=''.join(lab(*x) for x in LB)
LBL+='<div class="lb-pair">'+lab('mk2-label-jogurt.webp','1983/793',"Jogurt — cup sleeve · 150 g","Йогурт — этикетка стаканчика · 150 г")+lab('mk2-label-jogurt-lid.webp','1254/1254',"Jogurt — lid","Йогурт — крышка",'lb-sq')+'</div>'
LBL+=lab('mk2-label-smietana.webp','2000/810',"Śmietana — tub label · 200 g","Сметана — этикетка тубы · 200 г")
LBL+=lab('mk2-label-maslo.webp','1536/1140',"Masło — butter wrap · 200 g","Сливочное масло — обёртка брикета · 200 г",'lb-wrap')
LBL+='<div class="lb-pair lb-pouch">'+lab('mk2-prod-twarog.webp','1015/1306',"Twaróg — pouch, front","Творог — пакет, лицевая сторона",'lb-tall')+lab('mk2-label-twarog-back.webp','1145/1374',"Twaróg — pouch, back","Творог — пакет, тыльная сторона",'lb-tall')+'</div>'
FULL['Packaging System\u2060']='<div class="mk2-full po po-d"><div class="po-hero">'+''.join(HERO)+'</div><div class="po-caps">'+CAPS+'</div></div>'+'<div class="mk2-full mk2-grow lb"><div class="mk2-gl2"><b>'+T('Label Layouts','Макеты этикеток')+'</b><p class="mk2-cap">'+T("Flat label artwork for each format: wrap-around labels for the bottles, a sleeve and a lid for the cup, a tub label, a butter wrap and both sides of the pouch.","Развёртки этикеток для каждого формата: круговые этикетки бутылок, этикетка и крышка стаканчика, этикетка баночки, обёртка масла и обе стороны дой-пака.")+'</p></div><div class="mk2-gr lb-list">'+LBL+'</div></div>'
S.append(('Packaging System\u2060',L,R,''))
# 04 Art Direction & Communication
L=eb('04','Art Direction & Communication','Арт-дирекшн и коммуникация')+'<h3 class="mk2-h">'+T("Trust begins at home.","Доверие начинается дома.")+'</h3><p class="mk2-p">'+T("Soft daylight, natural textures and product-focused compositions shape a warm visual atmosphere. Short, direct headlines extend this identity into advertising communication.","Мягкий дневной свет, натуральные текстуры и акцент на продукте создают тёплую визуальную атмосферу. Короткие, понятные заголовки развивают этот язык в рекламной коммуникации.")+'</p>'
L+=det('Communication Rationale','Обоснование коммуникации',[
 ("Product First — packaging is the visual hero.","Product First — упаковка остаётся главным героем кадра."),
 ("Short Headline — communicate the emotional or product benefit quickly.","Short Headline — быстро передать эмоциональную или продуктовую выгоду."),
 ("Controlled Styling — supporting elements reinforce, not compete.","Controlled Styling — реквизит поддерживает продукт, а не спорит с ним."),
 ("Consistent Branding — do not duplicate the logo outside the product when unnecessary.","Consistent Branding — не дублировать логотип вне упаковки без необходимости.")])
R='<div class="mk2-auto" aria-roledescription="carousel"><!--CAR--></div>'
FULL['Art Direction & Communication']='<div class="mk2-full"><ul class="mk2-heads">'+''.join(f'<li><span>{T(a)}</span><b>{T(b)}</b></li>' for a,b in [('Milk','Pure Goodness'),('Kefir','Lightness & Balance'),('Yogurt','Berry Delicacy'),('Sour Cream','Smooth Indulgence'),('Butter','Creamy Perfection'),('Cottage Cheese\u2060','Everyday Goodness')])+'</ul>'+'</div>'
IO_F=lambda src,alt,en,ru:'<figure class="io-f"><div class="io-im"><img src="'+src+'" alt="'+alt+'" loading="lazy" decoding="async"></div><figcaption>'+T(en,ru)+'</figcaption></figure>'
FULL['Art Direction & Communication']+='<div class="mk2-full io io-a"><div class="io-h"><span class="io-lbl">'+T('In-store & Out-of-home','В магазине и на улице')+'</span><p class="io-cap">'+T('The same headline system and product line-up move from the pack to the shelf and the street: one recognisable brand at every touchpoint.','Та же система заголовков и та же линейка продуктов переходят с упаковки на полку и на улицу: один узнаваемый бренд в каждой точке контакта.')+'</p></div><div class="io-big">'+IO_F('mk2-pos.webp','MilkKalina point-of-sale materials','In-store: counter display, hanging sign, wobblers, shelf talker, shelf strip, price tags','В магазине: настольный дисплей, подвес, воблеры, шелфтокер, полочная лента, ценники')+'</div><div class="io-two">'+IO_F('mk2-ooh-busstop.webp','MilkKalina city-light at a bus stop','Out-of-home: city-light at a bus stop','Наружная реклама: ситилайт на остановке')+IO_F('mk2-ooh-metro.webp','MilkKalina posters in the metro','Out-of-home: metro posters','Наружная реклама: постеры в метро')+'</div></div>'
S.append(('Art Direction & Communication',L,R,'car'))
# 05 Conclusion
L=eb('05','Conclusion','Итог')+'<h3 class="mk2-h">'+T("One brand. One connected story.","Один бренд. Одна цельная история.")+'</h3><p class="mk2-p">'+T("From positioning to identity, packaging and communication, MilkKalina demonstrates a connected approach to building a brand concept.","От позиционирования до айдентики, упаковки и коммуникации MilkKalina демонстрирует целостный подход к созданию концепции бренда.")+'</p><p class="mk2-cap mk2-sig">'+T("Self-Initiated Concept · Not Commercially Launched","Авторский концепт · Не запущен в продажу")+'</p>'
R=det('Concept Validation','Проверка концепции',[("Recognition\u2060","Узнаваемость"),("Product Information Clarity","Понятность информации о продукте"),("Perceived Quality","Восприятие качества"),("Purchase Consideration","Готовность рассмотреть покупку")],("Criteria for potential testing, not research that has been carried out.","Критерии возможной проверки, а не проведённые исследования."),'mk2-rat-row mk2-rat-4')
S.append(('Conclusion',L,R,''))
RU['Cottage Cheese\u2060']='Cottage Cheese'
D=("A self-initiated dairy brand concept for Poland, built around Warm Premium — a balance of visual quality, warmth and everyday familiarity.","Авторская концепция молочного бренда для Польши, основанная на Warm Premium — сочетании визуального качества, тепла и повседневной близости.")
RU[D[0]]=D[1];RU["Brand Identity & Packaging Concept"]="Brand Identity & Packaging Concept";RU["Self-Initiated · Poland · Dairy / FMCG"]="Авторский концепт · Польша · Молочные продукты / FMCG"
C=["Brand Concept","Art Direction\u2063","Visual Identity\u2063","Packaging\u2063","Communication\u2063"]
for k in C: RU[k]=k.replace('\u2060','')
s,m,st=load()
sp=[y for y in st['projects'] if y['slug']=='milkkalina'][0]['subs'][0]
sp['img']={'hero':{'src':'mk2-collection.webp','ratio':'2200/1228'}};sp['heroSide']=False
sp['contribLabel']='My Contribution\u2063'
sp.update({'sub':OLD['sub'],'subSmall':False,'desc':OLD['desc'],'metaLine':None,'selfInit':True,'metaExtra':[['Deliverables',OLD['deliverables']]],'industry':OLD['industry'],'role':None,'deliverables':None,'contrib':'\n'.join(C),
 'story':[dict({'t':t,'html':'<div class="mk2-sec"><div class="mk2-l">'+l+'</div><div class="mk2-r">'+r+'</div>'+FULL.get(t,'')+'</div>'},**({'anno':OLD['logo']['anno'],'parts':OLD['logo'].get('parts')} if k=='logo' else {'car':CAR} if k=='car' else {})) for t,l,r,k in S],'storyEnd':''})
save(s,m,st)
for t,_,_,_ in S:
    RU.setdefault(t,{'Concept\u2060':'Концепция','Brand Identity\u2060':'Brand Identity','Packaging System\u2060':'Packaging System'}.get(t,t))
RU['Conclusion']='Итог';RU['Concept\u2060']='Концепция';RU['Brand Identity\u2060']='Айдентика';RU['Packaging System\u2060']='Упаковочная система';RU['Art Direction & Communication']='Арт-дирекшн и коммуникация'
json.dump(RU,open('/tmp/mk_ru5.json','w'),ensure_ascii=False);print(len(S),len(RU))
