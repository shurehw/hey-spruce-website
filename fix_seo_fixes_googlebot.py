from pathlib import Path
p=Path('seo-fixes.html')
s=p.read_text(encoding='utf-8',errors='ignore')
s=s.replace('meta name="googlebot" content="index, follow"','meta name="googlebot" content="noindex, nofollow"')
p.write_text(s,encoding='utf-8')
print('ok')
