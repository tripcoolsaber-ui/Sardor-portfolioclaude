# SEO for beyondform.me

## How it works
- The site is still one app (`index.html`). `tools/seo_build.py` copies it into a real folder for every page and language:
  `/work/wog/motor-oils/index.html`, `/ru/work/wog/motor-oils/index.html`, and so on.
- Each copy gets, between `<!--seo:head-->` and `<!--/seo:head-->`: its own title, description, canonical, hreflang (en, ru, x-default), Open Graph, Twitter and JSON-LD.
- Between `<!--seo:body-->` and `<!--/seo:body-->` it gets the page text as plain HTML with real links. The app removes this block on start and draws the page exactly as before; browsers with JavaScript never show it.
- The app uses normal URLs (History API). Old links like `beyondform.me/#/work/wog/motor-oils` are rewritten in the browser to `/work/wog/motor-oils/`.
- Language comes from the URL: `/...` is English, `/ru/...` is Russian. The EN/RU switch keeps the current page.
- Also generated: `sitemap.xml` (with hreflang alternates; `lastmod` changes only when a page's content changes), `robots.txt`, `404.html`, and 1200×630 share images in `/og/`.

## Build and publish
1. Edit `index.html` / `ru-cases.json` as usual (the root `index.html` is the template).
2. Run `python3 tools/seo_build.py` (needs Python 3 and Pillow: `pip install pillow`).
3. Commit everything, including the generated folders, `og/`, `sitemap.xml` and `tools/*.json`, and push to `main`. GitHub Pages publishes it; `CNAME` stays as is.

If `index.html` is edited without running the script, the other pages keep the old app until the next run. Always run it before pushing.

## Adding a new case
Add the project to the state data in `index.html` as before and run the script. Its pages (EN and RU), meta tags, share image and sitemap entries are created automatically.
Optional, per project or sub-project: `"seo": {"title": "...", "title_ru": "...", "desc": "...", "desc_ru": "...", "image": "file.webp"}`.
Hand-written titles for existing pages live in `TITLE` at the top of `tools/seo_build.py`.

## Google Search Console
1. https://search.google.com/search-console → Add property → Domain `beyondform.me` (DNS TXT record at the registrar) or URL prefix `https://beyondform.me/` (HTML tag or file).
2. Sitemaps → submit `sitemap.xml`.
3. URL Inspection → test `https://beyondform.me/` and a case, e.g. `/work/wog/motor-oils/`; request indexing for the most important pages.
4. Check Pages (indexing report) after 1–3 weeks.

## Yandex Webmaster
1. https://webmaster.yandex.ru → add `https://beyondform.me/` and confirm (meta tag or HTML file).
2. Indexing → Sitemap files → add `https://beyondform.me/sitemap.xml`.
3. Indexing → Reindex pages → add the main pages.
4. Settings → Regional settings: Tashkent / Uzbekistan if wanted.
