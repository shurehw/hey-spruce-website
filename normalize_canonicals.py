from pathlib import Path
import re

ROOT = Path('.')
html_files = list(ROOT.glob('*.html')) + list((ROOT/'blog').glob('*.html'))

# Normalize canonical URLs for trailingSlash=false:
# - Keep homepage canonical as https://www.groundops.com/
# - Remove trailing slash for all other canonicals under groundops.com
canon_pat = re.compile(r'(<link\s+rel="canonical"\s+href=")(?P<url>https://www\.groundops\.com/[^\"]+)("\s*/?>)', re.I)

def normalize(url: str) -> str:
    if url == 'https://www.groundops.com/':
        return url
    # remove a single trailing slash
    if url.endswith('/'):
        return url[:-1]
    return url

changed = 0
for p in html_files:
    s = p.read_text(encoding='utf-8', errors='ignore')

    def _sub(m):
        url = m.group('url')
        return m.group(1) + normalize(url) + m.group(3)

    s2 = canon_pat.sub(_sub, s)
    if s2 != s:
        p.write_text(s2, encoding='utf-8')
        changed += 1

print('canonical-normalized files:', changed)
