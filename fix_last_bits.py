from pathlib import Path
import re

def fix_file(path, subs):
    p = Path(path)
    if not p.exists():
        return
    s = p.read_text(encoding='utf-8', errors='ignore')
    orig = s
    for pat, rep, flags in subs:
        s = re.sub(pat, rep, s, flags=flags)
    # fix mojibake variants commonly produced by editor decoding
    s = s.replace('Ã¢â‚¬â€', ' - ').replace('Ã¢â‚¬â€œ', ' - ').replace('Ã¢â‚¬"', ' - ').replace('Ã¢â‚¬â€', ' - ')
    if s != orig:
        p.write_text(s, encoding='utf-8')

fix_file('downtown-la-restaurant-cleaning.html', [
    (r'>\s*ðŸ¢\s*[^<]*500\+[^<]*<', '><span>ðŸ“· Checklists + photo evidence</span><', re.I),
    (r'500\+\s*DTLA\s*Restaurants\s*Cleaned', 'QA documented per visit', re.I),
    (r'over\s*500\s*DTLA\s*establishments', 'DTLA establishments', re.I),
    (r'within\s*30\s*minutes', 'per SLA', re.I),
    (r'30\s*minutes\s*of\s*calling', 'per SLA', re.I),
    (r'24/7', 'priority escalation', re.I),
    (r'We\s+your restaurant will pass inspection[^<]*</p>', 'We document cleaning-related corrective actions and close them with evidence so your ops team can audit what changed.</p>', re.I),
    (r'Join\s+hundreds[^<]*trust[^<]*', 'Standardized execution with documented QA and reporting.', re.I),
])

fix_file('restaurant-cleaning-los-angeles.html', [
    (r'Restaurant cleaning execution across LA locations[^<]*', 'Restaurant cleaning execution across LA locations - with QA and reporting. Each visit is a work order with a checklist, photo evidence, and exceptions logged as corrective actions.', re.I),
    (r'<div class="stat-number">\s*24/7\s*</div>\s*<div class="stat-label">\s*Service Availability\s*</div>', '<div class="stat-number">Ops</div> <div class="stat-label">Issue escalation</div>', re.I),
    (r'pass health inspections with flying colors', 'reduce inspection risk with documented standards', re.I),
])

print('done')
