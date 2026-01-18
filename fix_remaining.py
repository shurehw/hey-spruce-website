from pathlib import Path
import re

repls = {
  'restaurant-cleaning-los-angeles.html': [
    (r'<meta name="description" content="[^"]*">',
     '<meta name="description" content="Restaurant cleaning execution across Los Angeles: nightly cleaning, deep kitchen cleaning, and facilities support with QA checklists, photo evidence, and reporting.">'),
    (r'Join [^<]* that trust GroundOps[^<]*\.',
     'Standardized facilities execution across locations, with reporting your team can audit.'),
    (r'<div class="stat-number">\s*\d+\+?%?\s*</div>',
     '<div class="stat-number">SLA</div>'),
  ],
  'downtown-la-restaurant-cleaning.html': [
    (r'<span>ðŸ¢[^<]*</span>', '<span>ðŸ“· Checklists + photo evidence</span>'),
    (r'over \d+\+?\s*DTLA establishments', 'DTLA establishments'),
    (r'within 30 minutes[^<]*', 'per SLA'),
    (r'24/7', 'priority escalation'),
    (r'We your restaurant will pass inspection after our[^<]*</p>',
     'We document cleaning-related corrective actions and close them with evidence so your ops team can audit what changed.</p>'),
  ],
  'blog/restaurant-cleaning-checklist.html': [
    (r'Used by \d+\+[^<]*restaurants[^<]*', 'Used by multi-location operators to standardize execution and documentation'),
    (r'helped over \d+\+ LA restaurants', 'helped operators standardize cleaning execution'),
  ],
  'blog/emergency-cleaning-failed-inspections.html': [
    (r'<title>[^<]*</title>', '<title>Failed Health Inspection Recovery Plan (LA) | GroundOps</title>'),
    (r'<link rel="canonical" href="https://www\.heyspruce\.com/[^\"]*"', '<link rel="canonical" href="https://www.groundops.com/blog/emergency-cleaning-failed-inspections/"'),
    (r'24/7', 'priority'),
  ],
  'seo-fixes.html': [
    (r'<title>[^<]*</title>', '<title>Restaurant Cleaning Los Angeles CA | GroundOps</title>'),
    (r'<meta name="description" content="[^"]*">', '<meta name="description" content="Platform-backed facilities execution in LA: work orders, dispatch, QA checklists, photo evidence, and reporting for cleaning, maintenance, and repairs.">'),
    (r'<meta property="og:title" content="[^"]*">', '<meta property="og:title" content="Restaurant Cleaning Los Angeles | GroundOps">'),
    (r'<meta property="og:description" content="[^"]*">', '<meta property="og:description" content="Platform-backed facilities execution in LA: work orders, dispatch, QA checklists, photo evidence, and reporting.">'),
    (r'<meta name="twitter:description" content="[^"]*">', '<meta name="twitter:description" content="Platform-backed facilities execution in LA: work orders, dispatch, QA checklists, photo evidence, and reporting.">'),
  ],
  'performance-optimized.html': [
    (r'<title>[^<]*</title>', '<title>Restaurant Cleaning Los Angeles CA | GroundOps</title>'),
    (r'<meta name="description" content="[^"]*">', '<meta name="description" content="Platform-backed facilities execution in LA: work orders, dispatch, QA checklists, photo evidence, and reporting for cleaning, maintenance, and repairs.">'),
    (r'<meta property="og:title" content="[^"]*">', '<meta property="og:title" content="Restaurant Cleaning Los Angeles | GroundOps">'),
    (r'<meta property="og:description" content="[^"]*">', '<meta property="og:description" content="Platform-backed facilities execution in LA: work orders, dispatch, QA checklists, photo evidence, and reporting.">'),
    (r'<tspan fill="#14b8a6">Ground</tspan>\s*<tspan fill="#0f172a">\s*Ops</tspan>', '<tspan fill="#14b8a6">Ground</tspan><tspan fill="#0f172a">Ops</tspan>'),
    (r'<tspan fill="#14b8a6">Hey</tspan>\s*<tspan fill="#0f172a">\s*Spruce</tspan>', '<tspan fill="#14b8a6">Ground</tspan><tspan fill="#0f172a">Ops</tspan>'),
  ],
}

for rel, ops in repls.items():
    p = Path(rel)
    if not p.exists():
        continue
    s = p.read_text(encoding='utf-8', errors='ignore')
    orig = s
    for pat, rep in ops:
        s = re.sub(pat, rep, s, flags=re.I)
    if s != orig:
        p.write_text(s, encoding='utf-8')

print('fixed')
