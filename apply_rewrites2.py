import re
from pathlib import Path

root = Path('.')
html_files = list(root.glob('*.html')) + list((root/'blog').glob('*.html'))

# Replace brand variants everywhere
brand_pairs = [
    (re.compile(r'\bHey\s+Spruce\b', re.I), 'GroundOps'),
    (re.compile(r'(?<![\w/\-])Spruce(?![\w/\-])'), 'GroundOps'),
]

# Remove/soften red-flag claims
claim_patterns = [
    (re.compile(r'\b#1\b', re.I), ''),
    (re.compile(r'\b100%\b', re.I), ''),
    (re.compile(r'\b98%\b', re.I), ''),
    (re.compile(r'\b500\+\b', re.I), ''),
    (re.compile(r'\bguarantee\b', re.I), ''),
    (re.compile(r'\bguaranteed\b', re.I), ''),
    (re.compile(r'\b2-hour\b', re.I), 'SLA-based'),
    (re.compile(r'\b30-minute\b', re.I), 'SLA-based'),
    (re.compile(r'\bwithin\s+2\s+hours\b', re.I), 'per SLA'),
    (re.compile(r'\bTrusted by\b', re.I), 'Used by'),
    (re.compile(r'\bBest\b', re.I), 'Preferred'),
]

# Replace common nav logo block
logo_old = '<a href="index.html"><span style="color: #14b8a6; font-weight: 700;">Hey</span> <span style="color: #0f172a; font-weight: 500;">Spruce</span></a>'
logo_new = '<a href="index.html"><span style="color: #14b8a6; font-weight: 700;">Ground</span><span style="color: #0f172a; font-weight: 500;">Ops</span></a>'

# Replace problematic unicode punctuation with ASCII
unicode_map = {
    '\u2014': ' - ',
    '\u2013': ' - ',
    '\u2019': "'",
    '\u201c': '"',
    '\u201d': '"',
}

# Fix specific broken downtown line introduced earlier
fixes = {
    'downtown-la-restaurant-cleaning.html': [
        (re.compile(r'We\s+your restaurant will pass inspection[^<]*</p>', re.I),
         'We document cleaning-related corrective actions and close them with evidence so your ops team can audit what changed.</p>'),
        (re.compile(r'<span>ðŸ¢\s*[^<]*</span>', re.I), '<span>ðŸ“· Checklists + photo evidence</span>'),
        (re.compile(r'<span>âš¡\s*[^<]*</span>', re.I), '<span>ðŸ§¾ Work orders + audit trail</span>'),
    ]
}

# Noindex the legacy pages if present
noindex_files = {'performance-optimized.html','seo-fixes.html','heyspruce_rendered.html'}

def ensure_noindex(s: str) -> str:
    if re.search(r'<meta\s+name=["\"]robots["\"]', s, re.I):
        return re.sub(r'<meta\s+name=["\"]robots["\"][^>]*>', '<meta name="robots" content="noindex, nofollow">', s, flags=re.I)
    return re.sub(r'(<head[^>]*>)', r'\1\n    <meta name="robots" content="noindex, nofollow">', s, flags=re.I)

changed = 0
for p in html_files:
    s = p.read_text(encoding='utf-8', errors='ignore')

    # logo
    s = s.replace(logo_old, logo_new)

    # unicode normalize
    for u, a in unicode_map.items():
        s = s.replace(u, a)

    # brand
    for pat, rep in brand_pairs:
        s = pat.sub(rep, s)

    # claims
    for pat, rep in claim_patterns:
        s = pat.sub(rep, s)

    # cleanup double spaces from removals
    s = re.sub(r'\s{2,}', ' ', s)

    # file-specific fixes
    if p.name in fixes:
        for pat, rep in fixes[p.name]:
            s = pat.sub(rep, s)

    # ensure noindex on legacy pages
    if p.name in noindex_files:
        s = ensure_noindex(s)

    p.write_text(s, encoding='utf-8')
    changed += 1

print('Processed', changed, 'HTML files')
