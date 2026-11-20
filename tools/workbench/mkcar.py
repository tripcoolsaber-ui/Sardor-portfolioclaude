import sys
B=sys.argv[1]
h=open('/tmp/mk_base.html').read()
def rep(a,b):
    global h; assert h.count(a)==1,a; h=h.replace(a,b)
rep("soft=!!st.closest('.case-cre,.mk2-auto')||app;","soft=!!st.closest('.case-cre,.mk2-auto')||app,mk3=!!st.closest('.mk2-auto');")
rep("if(ad>(app?.98:soft?2.25:1.25))","if(ad>(app?.98:mk3?1.6:soft?2.25:1.25))")
rep("op=app?Math.max(0,1-ad*1.1):soft?","op=app?Math.max(0,1-ad*1.1):mk3?(ad<=1?1-.3*ad:Math.max(0,.7*(1.6-ad)/.6)):soft?")
rep("el.style.filter=e>.004?((narrow||soft)?","el.style.filter=e>.004?(mk3?'blur('+(e*"+B+").toFixed(2)+'px) brightness('+(1-e*.45).toFixed(3)+')':(narrow||soft)?")
open('/tmp/mk/index.html','w').write(h)
