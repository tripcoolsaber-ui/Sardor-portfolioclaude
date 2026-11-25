import sys,json,re;sys.path.insert(0,'/tmp');from st import *
s,m,st=load();sp=st['projects'][4]['subs'][0]
MAP={'mk-milk.webp':'mk2-poster-milk.webp','mk-kefir-2.webp':'mk2-poster-kefir.webp','mk-yogurt.webp':'mk2-poster-jogurt.webp','mk-sourcream-2.webp':'mk2-poster-smietana.webp','mk-butter-2.webp':'mk2-poster-maslo.webp','mk-cottage.webp':'mk2-poster-twarog.webp'}
n=0
for c in sp['chapters']:
    for x in c.get('media',[]):
        if x.get('src') in MAP: x['src']=MAP[x['src']];x['ratio']='1300/1741';n+=1
assert n==6;save(s,m,st)
h=open('/tmp/gh/index.html').read()
def rep(a,b,f=None):
    global h;assert h.count(a)==1,(a,h.count(a));h=h.replace(a,b)
rep("gt(\\'Lead Designer / Art Director based in Tashkent,<br>with 15+","gt(\\'Lead Designer / Art Director<br>with 15+") if False else None
a="Lead Designer / Art Director based in Tashkent,<br>with 15+";assert h.count(a)==1;h=h.replace(a,"Lead Designer / Art Director<br>with 15+")
a="Ведущий дизайнер / арт-директор из Ташкента,<br>с опытом";assert h.count(a)==1;h=h.replace(a,"Ведущий дизайнер / арт-директор<br>с опытом")
mm=re.search(r"var LANG='en',TITLE_EN='',RU=\{",h);i=mm.end()-1;j=h.find('};',i)
h=h[:j]+',"Self-initiated\\u200b":"Авторский проект"'+h[j:]
open('/tmp/gh/index.html','w').write(h)
C=json.load(open('/tmp/gh/ru-cases.json'))
for k,v in list(C.items()):
    if v=='Личный проект': C[k]='Авторский проект';print('ruc',repr(k))
C['Self-initiated\u200b']='Авторский проект'
json.dump(C,open('/tmp/gh/ru-cases.json','w'),ensure_ascii=False,separators=(',',':'))
g=open('/tmp/gh/tools/seo_build.py').read()
for a,b in [("'Lead Designer / Art Director based in Tashkent, with 15+","'Lead Designer / Art Director with 15+"),("'Ведущий дизайнер / арт-директор из Ташкента, с опытом","'Ведущий дизайнер / арт-директор с опытом")]:
    assert g.count(a)==1,a;g=g.replace(a,b)
open('/tmp/gh/tools/seo_build.py','w').write(g)
print('ok',n)
