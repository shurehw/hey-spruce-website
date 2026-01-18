from pathlib import Path
import re
from datetime import date

ROOT = Path('.')

EXCLUDE = {
    'performance-optimized.html',
    'seo-fixes.html',
    'supplier-portal.html',
}

pages = []
for p in sorted(ROOT.glob('*.html')):
    if p.name in EXCLUDE:
        continue
    pages.append(p)
for p in sorted((ROOT/'blog').glob('*.html')):
    pages.append(p)

for p in sorted((ROOT/'case-studies').glob('*.html')):
    pages.append(p)

canon_re = re.compile(r'<link\s+rel="canonical"\s+href="([^"]+)"\s*/?>', re.I)

urls = []
for p in pages:
    s = p.read_text(encoding='utf-8', errors='ignore')
    m = canon_re.search(s)
    if m:
        urls.append(m.group(1))
    else:
        if p.parent.name == 'blog':
            urls.append(f'https://www.groundops.com/blog/{p.stem}')
        else:
            urls.append('https://www.groundops.com/' if p.stem == 'index' else f'https://www.groundops.com/{p.stem}')

seen = set()
dedup = []
for u in urls:
    if u in seen:
        continue
    seen.add(u)
    dedup.append(u)

lastmod = date.today().isoformat()

xml_lines = [
    '<?xml version="1.0" encoding="UTF-8"?>',
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
]
for u in dedup:
    if '#' in u:
        continue
    xml_lines.append('  <url>')
    xml_lines.append(f'    <loc>{u}</loc>')
    xml_lines.append(f'    <lastmod>{lastmod}</lastmod>')
    xml_lines.append('  </url>')
xml_lines.append('</urlset>')

Path('sitemap.xml').write_text('\n'.join(xml_lines) + '\n', encoding='utf-8')
print('sitemap urls:', len(dedup))
