from pathlib import Path
import re

def scan(path, patterns):
    p=Path(path)
    t=p.read_text(encoding='utf-8',errors='ignore')
    hits=[pat for pat in patterns if re.search(pat,t,re.I)]
    print(path, 'HITS' if hits else 'OK', hits)

patterns=[r'100%',r'\b98%\b',r'500\+',r'guarantee',r'2-hour',r'24/7',r'EMERGENCY HOTLINE']
scan('blog/emergency-cleaning-failed-inspections.html', patterns)
scan('blog/restaurant-cleaning-checklist.html', patterns)
scan('blog/nfpa-96-requirements-la-restaurants.html', patterns)
scan('blog/2024-la-county-health-code-changes-restaurants.html', patterns)
