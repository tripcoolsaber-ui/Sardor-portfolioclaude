import asyncio
from playwright.async_api import async_playwright
U='/work/the-hood/'
async def main():
  async with async_playwright() as p:
    b=await p.chromium.launch()
    for l,w,h in [('',1440,900),('/ru',1440,900),('',1920,1080),('',768,1024),('',390,844),('',360,740)]:
      c=await b.new_context(viewport={'width':w,'height':h},is_mobile=w<600,has_touch=w<600);pg=await c.new_page();errs=[];bad=[]
      pg.on('pageerror',lambda e:errs.append(str(e)[:150]))
      pg.on('response',lambda r:bad.append(r.url[-40:]) if r.status>=400 else None)
      await pg.goto('http://localhost:8790'+l+U);await pg.wait_for_timeout(4500)
      H=await pg.evaluate('document.documentElement.scrollHeight');y=0
      while y<H: await pg.evaluate(f'window.scrollTo(0,{y})');await pg.wait_for_timeout(100);y+=800
      await pg.wait_for_timeout(800)
      t=(l.strip('/') or 'en')+str(w)
      info=await pg.evaluate("""()=>({nav:[...document.querySelectorAll('.pj-idx button')].map(b=>b.innerText.replace(/\\n/g,' ').replace(/\\u2064/g,'')),
        hs:document.documentElement.scrollWidth>document.documentElement.clientWidth,
        poster:[...document.querySelectorAll('img')].filter(i=>/hd-cover/.test(i.currentSrc||i.src)).map(i=>(i.currentSrc||i.src).split('/').pop()+':'+i.naturalWidth),
        callouts:document.querySelectorAll('#pj-1 .an-pt, #pj-1 [class*="anno"] b').length,
        parts:[...document.querySelectorAll('#pj-1 .pj-part b, #pj-1 .pj-parts b')].map(e=>e.innerText),
        myrole:!![...document.querySelectorAll('.pj-sec h2')].find(h=>/My role|Моя роль/.test(h.innerText)),
        contrib:(document.querySelector('.pj-facts .pf-v')||{innerText:''}).innerText.replace(/\\n/g,' · '),
        pouchW:(()=>{const a=document.querySelector('img[src$="hd-pouch.webp"]'),b2=document.querySelector('img[src$="hd-box.webp"]');return a&&b2?[Math.round(b2.getBoundingClientRect().width),Math.round(a.getBoundingClientRect().width)]:null})()})""")
      print(t,errs,bad[:3],'H',H,info)
      if w in (1440,390) and not l:
        tag='d' if w==1440 else 'm'
        await pg.evaluate("window.scrollTo(0,0)");await pg.wait_for_timeout(500);await pg.screenshot(path=f'/tmp/hd{tag}_0.png')
        for n in range(6):
          await pg.evaluate(f"document.querySelector('#pj-{n}').scrollIntoView({{block:'start'}});window.scrollBy(0,-30)");await pg.wait_for_timeout(700);await pg.screenshot(path=f'/tmp/hd{tag}_{n+1}.png')
      if w==1440:
        html=await pg.evaluate("""()=>{const d=document.documentElement.cloneNode(true);d.querySelectorAll('script').forEach(s=>s.remove());const b=d.querySelector('base');if(b)b.setAttribute('href','https://beyondform.me/');return '<!DOCTYPE html>\\n'+d.outerHTML}""")
        open(f'/tmp/thehood-{l.strip("/") or "en"}.html','w').write(html)
      await c.close()
    await b.close()
asyncio.run(main())
