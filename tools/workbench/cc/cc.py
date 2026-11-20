import numpy as np,json,os
from PIL import Image
def rgb2hsv(a):
    r,g,b=a[...,0],a[...,1],a[...,2];mx=np.max(a,axis=-1);mn=np.min(a,axis=-1);d=mx-mn
    h=np.zeros_like(mx);m=d>1e-6
    rr=(mx==r)&m;gg=(mx==g)&m&~rr;bb=m&~rr&~gg
    h[rr]=((g-b)[rr]/d[rr])%6;h[gg]=((b-r)[gg]/d[gg])+2;h[bb]=((r-g)[bb]/d[bb])+4
    s=np.where(mx>0,d/np.maximum(mx,1e-6),0);return h*60,s,mx
def hsv2rgb(h,s,v):
    h=(h%360)/60;i=np.floor(h).astype(int)%6;f=h-np.floor(h);p=v*(1-s);q=v*(1-s*f);t=v*(1-s*(1-f))
    out=np.zeros(h.shape+(3,))
    for k,(R,G,B) in enumerate([(v,t,p),(q,v,p),(p,v,t),(p,q,v),(t,p,v),(v,p,q)]):
        m=i==k;out[...,0][m]=R[m];out[...,1][m]=G[m];out[...,2][m]=B[m]
    return out
def hv(c):
    a=np.array(c,float)[None,None,:]/255;h,s,v=rgb2hsv(a);return h[0,0],s[0,0],v[0,0]
TP=hv((0x5a,0x0a,0x6e));TG=hv((0x3b,0x92,0x11));TB=np.array((0xfb,0xf8,0xf6),float)/255
def fix(src,dst,flat):
    im=Image.open(src).convert('RGBA');A=np.array(im).astype(float)/255;rgb=A[...,:3];al=A[...,3]
    H,S,V=rgb2hsv(rgb)
    def band(lo,hi,soft=18):
        w=np.clip((H-lo)/soft,0,1)*np.clip((hi-H)/soft,0,1);return w*np.clip((S-.18)/.2,0,1)
    out=rgb.copy()
    for (lo,hi,T) in [(245,325,TP),(65,170,TG)]:
        w=band(lo,hi)*(al>.5)
        sel=(w>.5)&(V>.15)
        if sel.sum()<300: continue
        mh=np.median(H[sel]);ms=np.median(S[sel]);mv=np.median(V[sel])
        nh=H+(T[0]-mh);ns=np.clip(S*(T[1]/max(ms,1e-3)),0,1);nv=np.clip(V*(T[2]/max(mv,1e-3)),0,1)
        new=hsv2rgb(nh,ns,nv);out=out*(1-w[...,None])+new*w[...,None]
    if flat:
        wb=np.clip((V-.80)/.08,0,1)*np.clip((.12-S)/.06,0,1)*(al>.5)
        sel=wb>.5
        if sel.sum()>500:
            mb=np.median(rgb[sel],axis=0);out=np.clip(out+(TB-mb)[None,None,:]*wb[...,None],0,1)
    res=np.concatenate([np.clip(out,0,1),al[...,None]],axis=-1)
    Image.fromarray((res*255+.5).astype('uint8'),'RGBA').save(dst,'WEBP',quality=90,method=6)
F=[('mk2-label-milk.webp',1),('mk2-label-kefir.webp',1),('mk2-label-jogurt.webp',1),('mk2-label-smietana.webp',1),('mk2-label-jogurt-lid.webp',0),('mk2-label-twarog-back.webp',0),
   ('mk2-prod-milk.webp',0),('mk2-prod-kefir.webp',0),('mk2-prod-jogurt.webp',0),('mk2-prod-smietana.webp',0),('mk2-prod-maslo.webp',0),('mk2-prod-twarog.webp',0)]
os.makedirs('/tmp/cc/out',exist_ok=True)
for f,flat in F: fix('/tmp/gh/'+f,'/tmp/cc/out/'+f,flat)
print('done')
