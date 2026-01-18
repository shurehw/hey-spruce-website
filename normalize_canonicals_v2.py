from pathlib import Path
import re

ROOT = Path('.')
html_files = list(ROOT.glob('*.html')) + list((ROOT/'blog').glob('*.html'))

# Normalize canonical URLs for Vercel trailingSlash=false:
# - Only homepage keeps trailing slash
# - Force domain to www.groundops.com
canon_re = re.compile(r'(<link\s+rel="canonical"\s+href=")([^"]+)("\s*/?>)', re.I)

def normalize(url: str) -> str:
    # force domain if it is heyspruce
    url = url.replace('https://www.heyspruce.com/', 'https://www.groundops.com/')
    url = url.replace('http://www.heyspruce.com/', 'https://www.groundops.com/')

    if url == 'https://www.groundops.com/':
        return url

    # strip trailing slash for all other groundops URLs
    if url.startswith('https://www.groundops.com/') and url.endswith('/'):
        return url[:-1]

    return url

changed = 0
for p in html_files:
    s = p.read_text(encoding='utf-8', errors='ignore')

    def _sub(m):
        return m.group(1) + normalize(m.group(2)) + m.group(3)

    s2 = canon_re.sub(_sub, s)
    if s2 != s:
        p.write_text(s2, encoding='utf-8')
        changed += 1

print('canonicals normalized:', changed)
