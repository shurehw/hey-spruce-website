from pathlib import Path
p = Path('index.html')
s = p.read_text(encoding='utf-8', errors='ignore')
old = '<li><a href="#case-studies">Case Studies</a></li>'
new = '<li><a href="/case-studies">Case Studies</a></li>'
if old in s:
    s = s.replace(old, new)
p.write_text(s, encoding='utf-8')
print('patched')
