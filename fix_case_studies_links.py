from pathlib import Path

# Update top-level pages to use /case-studies instead of index.html#case-studies
files = list(Path('.').glob('*.html')) + [Path('vendor-management.html'), Path('platform.html')]
changed = 0
for p in files:
    if not p.exists():
        continue
    s = p.read_text(encoding='utf-8', errors='ignore')
    s2 = s.replace('href="index.html#case-studies"', 'href="/case-studies"')
    if s2 != s:
        p.write_text(s2, encoding='utf-8')
        changed += 1
print('updated files:', changed)
