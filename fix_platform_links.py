from pathlib import Path

# Update top-level pages to use /platform (not index.html#platform)
# and to link vendor-management as /vendor-management (already done on many pages)
files = list(Path('.').glob('*.html'))
changed = 0
for p in files:
    s = p.read_text(encoding='utf-8', errors='ignore')
    s2 = s.replace('href="index.html#platform"', 'href="/platform"')
    s2 = s2.replace('href="index.html#platform">Platform', 'href="/platform">Platform')
    if s2 != s:
        p.write_text(s2, encoding='utf-8')
        changed += 1
print('updated files:', changed)
