from pathlib import Path
import re

p = Path('generate_sitemap.py')
code = p.read_text(encoding='utf-8', errors='ignore')

# Insert case studies pages into the sitemap collection after blog pages
needle = "for p in sorted((ROOT/'blog').glob('*.html')):\n    pages.append(p)"
if needle in code and "case-studies" not in code:
    code = code.replace(
        needle,
        needle + "\n\nfor p in sorted((ROOT/'case-studies').glob('*.html')):\n    pages.append(p)"
    )

p.write_text(code, encoding='utf-8')
print('updated generate_sitemap.py')
