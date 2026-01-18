from pathlib import Path

root = Path('.')
files = list(root.glob('*.html'))
changed_files = []
for p in files:
    s = p.read_text(encoding='utf-8', errors='ignore')
    s2 = s.replace('href="vendor-management.html"', 'href="/vendor-management"')
    if s2 != s:
        p.write_text(s2, encoding='utf-8')
        changed_files.append(str(p))

print('updated files:', len(changed_files))
for f in changed_files:
    print('-', f)
