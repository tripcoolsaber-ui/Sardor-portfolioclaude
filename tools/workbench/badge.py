import sys
C,T=sys.argv[1],sys.argv[2]
h=open('/tmp/fix_base.html').read()
for a,b in [("border:1px solid color-mix(in srgb,#ffb547 55%,transparent);background:color-mix(in srgb,#ffb547 12%,transparent);color:#ffd08a;",f"border:1px solid color-mix(in srgb,{C} 55%,transparent);background:color-mix(in srgb,{C} 12%,transparent);color:{T};"),
            ('.pj-selfi:before{content:"";width:6px;height:6px;border-radius:50%;background:#ffb547}',f'.pj-selfi:before{{content:"";width:6px;height:6px;border-radius:50%;background:{C}}}')]:
    assert h.count(a)==1,a;h=h.replace(a,b)
open('/tmp/gh/index.html','w').write(h)
