import asyncio
from playwright.async_api import async_playwright
async def main():
  async with async_playwright() as p:
    b=await p.chromium.launch()
    for l,w,h in [('',1440,900),('/ru',1440,900),('',1920,1080),('',768,1024),('',390,844),('',360,740)]:
      c=await b.new_context(viewport={'width':w,'height':h},is_mobile=w<600,has_touch=w<600);pg=await c.new_page();errs=[];bad=[]
      pg.on('pageerror',lambda e:errs.append(str(e)[:200]))
      pg.on('response',lambda r:bad.append(r.url[-40:]) if r.status>=400 else None)
      await pg.goto('http://localhost:8790'+l+'/work/milkkalina/');await pg.wait_for_timeout(4500)
      H=await pg.evaluate('document.documentElement.scrollHeight');y=0
      while y<H: await pg.evaluate(f'window.scrollTo(0,{y})');await pg.wait_for_timeout(120);y+=700
      await pg.wait_for_timeout(900)
      t=(l.strip('/') or 'en')+str(w)
      lefts=await pg.evaluate("[...document.querySelectorAll('.mk2-h')].map(e=>Math.round(e.getBoundingClientRect().left))")
      eng=await pg.evaluate("""()=>{document.querySelectorAll('details').forEach(d=>d.open=true);const out=[];const w=document.createTreeWalker(document.querySelector('.pj'),NodeFilter.SHOW_TEXT);let n;while(n=w.nextNode()){const t=n.nodeValue.trim();if(t.length>25&&/[a-z]{4,} [a-z]{3,} [a-z]{3,}/.test(t)&&!/[а-я]/i.test(t))out.push(t.slice(0,60))}return out.slice(0,8)}""") if l else []
      print(t,errs,bad[:3],'H',H,'h3 lefts',lefts,await pg.evaluate("document.documentElement.scrollWidth>document.documentElement.clientWidth"),await pg.evaluate("[...document.querySelectorAll('.pj-idx button')].map(b=>b.innerText.replace('\\n',' '))"),eng)
      await pg.evaluate("document.querySelectorAll('details').forEach(d=>d.open=false)")
      if w in (1440,390) and not l:
        tag='d' if w==1440 else 'm'
        await pg.evaluate("window.scrollTo(0,0)");await pg.wait_for_timeout(600);await pg.screenshot(path=f'/tmp/k3{tag}_0.png')
        for n in range(5):
          await pg.evaluate(f"document.querySelector('#pj-{n}').scrollIntoView({{block:'start'}});window.scrollBy(0,-30)");await pg.wait_for_timeout(700);await pg.screenshot(path=f'/tmp/k3{tag}_{n+1}.png')
        if w==1440:
          html=await pg.evaluate("""()=>{const d=document.documentElement.cloneNode(true);d.querySelectorAll('script').forEach(s=>s.remove());const b=d.querySelector('base');if(b)b.setAttribute('href','https://beyondform.me/');return '<!DOCTYPE html>\\n'+d.outerHTML}""")
          open('/mnt/user-data/outputs/milkkalina-case-preview-en.html','w').write(html)
      if l=='/ru':
        html=await pg.evaluate("""()=>{const d=document.documentElement.cloneNode(true);d.querySelectorAll('script').forEach(s=>s.remove());const b=d.querySelector('base');if(b)b.setAttribute('href','https://beyondform.me/');return '<!DOCTYPE html>\\n'+d.outerHTML}""")
        open('/mnt/user-data/outputs/milkkalina-case-preview-ru.html','w').write(html)
      await c.close()
    await b.close()
asyncio.run(main())
