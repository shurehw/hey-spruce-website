import re
from pathlib import Path

ROOT = Path('.')

# Pages we treat as public marketing pages
TOP_LEVEL_PAGES = [
  'index.html','restaurant-cleaning-los-angeles.html','commercial-kitchen-cleaning.html','nightly-cleaning.html',
  'preventive-maintenance.html','hood-exhaust-cleaning.html','multi-location-cleaning.html','boh-cleaning.html',
  'foh-cleaning.html','restroom-cleaning.html','floor-scrubbing.html','downtown-la-restaurant-cleaning.html'
]

# Pages we don't want indexed (legacy/seo scratch/perf variants)
NOINDEX_PAGES = ['performance-optimized.html','seo-fixes.html','heyspruce_rendered.html']

BLOG_PAGES = [
  'blog/emergency-cleaning-failed-inspections.html',
  'blog/restaurant-cleaning-checklist.html',
]

ALL_EDIT = [p for p in TOP_LEVEL_PAGES + NOINDEX_PAGES + BLOG_PAGES if (ROOT/p).exists()]


def read(p: Path) -> str:
    return p.read_text(encoding='utf-8', errors='ignore')

def write(p: Path, s: str):
    p.write_text(s, encoding='utf-8')


def ensure_noindex(html: str) -> str:
    if re.search(r'<meta\s+name=["\"]robots["\"]', html, re.I):
        # normalize to noindex
        html = re.sub(r'<meta\s+name=["\"]robots["\"][^>]*>', '<meta name="robots" content="noindex, nofollow">', html, flags=re.I)
        return html
    # insert after <head>
    return re.sub(r'(<head[^>]*>)', r'\1\n    <meta name="robots" content="noindex, nofollow">', html, flags=re.I)


def replace_logo(html: str) -> str:
    # common nav logo block in service pages
    html = html.replace(
        '<a href="index.html"><span style="color: #14b8a6; font-weight: 700;">Hey</span> <span style="color: #0f172a; font-weight: 500;">Spruce</span></a>',
        '<a href="index.html"><span style="color: #14b8a6; font-weight: 700;">Ground</span><span style="color: #0f172a; font-weight: 500;">Ops</span></a>'
    )
    # some pages might still have "Hey" + space
    html = html.replace(
        '<a href="index.html"><span style="color: #14b8a6; font-weight: 700;">Hey</span><span style="color: #0f172a; font-weight: 500;">Spruce</span></a>',
        '<a href="index.html"><span style="color: #14b8a6; font-weight: 700;">Ground</span><span style="color: #0f172a; font-weight: 500;">Ops</span></a>'
    )
    # blog back links already fine
    return html


def scrub_redflag_claims(text: str) -> str:
    # Remove / soften obvious overclaims in titles/descriptions/body
    replacements = [
        (r'\b#1\b', ''),
        (r'\b100%\b', ''),
        (r'\bguarantee\b', ''),
        (r'\bguaranteed\b', ''),
        (r'\bwithin\s+2\s+hours\b', 'per SLA'),
        (r'\b2-hour\b', 'SLA-based'),
        (r'\b30-minute\b', 'SLA-based'),
        (r'\b500\+\b', ''),
        (r'\bTrusted by\b', 'Used by'),
        (r'\bmost competitive\b', 'scoped'),
    ]
    for pat, rep in replacements:
        text = re.sub(pat, rep, text, flags=re.I)
    # clean up doubled spaces from removals
    text = re.sub(r'\s{2,}', ' ', text)
    text = re.sub(r'\s+([|,])', r'\1', text)
    return text


def normalize_brand(text: str) -> str:
    # Make sure GroundOps is the only brand name
    text = re.sub(r'\bHey\s+Spruce\b', 'GroundOps', text, flags=re.I)
    # Standalone Spruce (avoid touching URLs / file names)
    text = re.sub(r'(?<![\w/\-])Spruce(?![\w/\-])', 'GroundOps', text)
    return text


def rewrite_service_page_hero(html: str, kind: str) -> str:
    # Rewrite the first hero lead paragraph on service pages (simple, deterministic)
    # We target: <p class="hero-lead"> ... </p>
    mapping = {
        'restaurant': 'Restaurant cleaning execution across LA locations â€” with QA and reporting.',
        'kitchen': 'Commercial kitchen deep cleaning â€” scoped, documented, and repeatable.',
        'nightly': 'Nightly cleaning managed like operations, not â€œa crew.â€',
        'pm': 'Preventive maintenance across locations â€” scheduled, tracked, closed.',
        'hood': 'Hood/exhaust compliance coordination â€” scheduled, documented, auditable.',
        'multi': 'Multi-location cleaning through one queue and one reporting layer.',
        'boh': 'BOH cleaning run to a standard, documented per shift.',
        'foh': 'FOH standards across locations â€” consistent execution, documented.',
        'restroom': 'Restroom cleaning that holds up to inspection and brand standards.',
        'floor': 'Floor scrubbing/degreasing â€” scoped, measured, repeatable.',
    }
    lead = mapping.get(kind, '')
    if not lead:
        return html

    new_p = (
        f'<p class="hero-lead">{lead} Each visit is a work order with a checklist, photo evidence, and exceptions logged as corrective actions.</p>'
    )

    html = re.sub(r'<p\s+class=["\"]hero-lead["\"][^>]*>.*?</p>', new_p, html, count=1, flags=re.I|re.S)
    return html


def remove_only_partner_language(html: str) -> str:
    html = re.sub(r"We're the only facilities partner[^<]*\.",
                  "We run facilities execution through one system with documented outputs.",
                  html, flags=re.I)
    html = re.sub(r"only facilities partner", "facilities partner", html, flags=re.I)
    return html


def fix_downtown_page(html: str) -> str:
    # Remove the worst claims and rewrite the hero badges + emergency/inspection sections.
    html = re.sub(r'<title>[^<]*</title>',
                  '<title>Downtown LA Restaurant Cleaning | QA + Reporting | GroundOps</title>',
                  html, flags=re.I)

    html = re.sub(r'<meta\s+name=["\"]description["\"][^>]*>',
                  '<meta name="description" content="Downtown Los Angeles restaurant cleaning execution with documented QA, checklists, photo evidence, and reporting. Response targets are defined in the SLA.">',
                  html, flags=re.I)

    # hero badges: drop 30-minute + 500+
    html = re.sub(r'<span>âš¡[^<]*</span>', '<span>ðŸ§¾ Work orders + audit trail</span>', html, flags=re.I)
    html = re.sub(r'<span>ðŸ¢[^<]*</span>', '<span>ðŸ“· Checklists + photo evidence</span>', html, flags=re.I)

    # remove guarantee paragraph about passing inspection
    html = re.sub(r'We guarantee your restaurant will pass inspection[^<]*</p>',
                  'We document cleaning-related corrective actions and close them with evidence so your ops team can audit what changed.</p>',
                  html, flags=re.I)

    # remove 30 minute response section header + paragraph
    html = re.sub(r'<h3>Emergency Restaurant Cleaning Downtown Los Angeles[^<]*</h3>\s*<p>.*?</p>',
                  '<h3>Issue escalation</h3><p>Priority work orders are available. Response targets depend on trade, time window, and coverage and are defined in the SLA.</p>',
                  html, flags=re.I|re.S)

    return html


def fix_blog_emergency(html: str) -> str:
    # Remove hard promises in meta + hero alert
    html = re.sub(r'<meta\s+name=["\"]description["\"][^>]*>',
                  '<meta name="description" content="Failed health inspection? Use this recovery plan to remediate, document corrective actions, and prepare for re-inspection. Priority response targets are defined in the SLA.">',
                  html, flags=re.I)

    html = re.sub(r"We've helped 300\+ LA restaurants pass re-inspection\.",
                  "We use a documented corrective-action workflow to prepare for re-inspection.",
                  html, flags=re.I)

    html = re.sub(r'2-hour emergency response[^<]*',
                  'Priority response (per SLA) â€¢ Documentation included',
                  html, flags=re.I)

    # soften the 98% claim (keep as guidance, not promise)
    html = re.sub(r'98% pass their re-inspection',
                  'most restaurants pass re-inspection when issues are remediated and documented',
                  html, flags=re.I)

    return html


def fix_blog_checklist(html: str) -> str:
    html = re.sub(r'<meta\s+name=["\"]description["\"][^>]*>',
                  '<meta name="description" content="Restaurant cleaning checklist template for daily/weekly/monthly tasks. Use it to standardize execution and document completion across locations.">',
                  html, flags=re.I)
    return html


def process_file(rel: str):
    p = ROOT / rel
    html = read(p)

    if rel in NOINDEX_PAGES:
        html = ensure_noindex(html)

    html = replace_logo(html)
    html = normalize_brand(html)

    if rel == 'downtown-la-restaurant-cleaning.html':
        html = fix_downtown_page(html)

    if rel == 'blog/emergency-cleaning-failed-inspections.html':
        html = fix_blog_emergency(html)

    if rel == 'blog/restaurant-cleaning-checklist.html':
        html = fix_blog_checklist(html)

    # service page hero rewrites
    kind_map = {
        'restaurant-cleaning-los-angeles.html':'restaurant',
        'commercial-kitchen-cleaning.html':'kitchen',
        'nightly-cleaning.html':'nightly',
        'preventive-maintenance.html':'pm',
        'hood-exhaust-cleaning.html':'hood',
        'multi-location-cleaning.html':'multi',
        'boh-cleaning.html':'boh',
        'foh-cleaning.html':'foh',
        'restroom-cleaning.html':'restroom',
        'floor-scrubbing.html':'floor',
    }
    if rel in kind_map:
        html = rewrite_service_page_hero(html, kind_map[rel])
        html = remove_only_partner_language(html)

    html = scrub_redflag_claims(html)

    write(p, html)


for rel in ALL_EDIT:
    process_file(rel)

print('Updated files:', len(ALL_EDIT))
