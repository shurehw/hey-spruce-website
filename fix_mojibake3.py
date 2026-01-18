from pathlib import Path

files = [
  'commercial-kitchen-cleaning.html',
  'nightly-cleaning.html',
  'preventive-maintenance.html',
  'hood-exhaust-cleaning.html',
  'foh-cleaning.html',
  'floor-scrubbing.html',
]

# Fix common mojibake sequences produced by mis-decoding UTF-8 smart quotes
# Seen patterns: Ã¢â‚¬Å“ (\u00e2 \u20ac \u0153) and Ã¢â‚¬\x9d (\u00e2 \u20ac \x9d)
OPEN_DQ = "\u00e2\u20ac\u0153"   # Ã¢â‚¬Å“
CLOSE_DQ = "\u00e2\u20ac\u009d"  # Ã¢â‚¬\x9d
OPEN_SQ = "\u00e2\u20ac\u0098"   # Ã¢â‚¬\x98
CLOSE_SQ = "\u00e2\u20ac\u0099"  # Ã¢â‚¬\x99
EM_DASH = "\u00e2\u20ac\u201d"   # sometimes appears, safe to normalize

changed = []
for f in files:
    p = Path(f)
    if not p.exists():
        continue
    s = p.read_text(encoding='utf-8', errors='ignore')
    s2 = s
    s2 = s2.replace(OPEN_DQ, '"').replace(CLOSE_DQ, '"')
    s2 = s2.replace(OPEN_SQ, "'").replace(CLOSE_SQ, "'")
    # also normalize any leftover known sequences
    s2 = s2.replace('Ã¢â‚¬â€', ' - ').replace('Ã¢â‚¬â€œ', ' - ').replace('Ã¢â‚¬"', ' - ')

    if f == 'nightly-cleaning.html':
        # Remove leftover unverifiable stat claims on nightly page
        s2 = s2.replace('<div class="stat-number">500+</div> <div class="stat-label">Locations Served</div>',
                        '<div class="stat-number">SLA</div> <div class="stat-label">Defined standards</div>')
        s2 = s2.replace('<div class="stat-number">100%</div> <div class="stat-label">Photo Verified</div>',
                        '<div class="stat-number">QA</div> <div class="stat-label">Evidence per visit</div>')

    if s2 != s:
        p.write_text(s2, encoding='utf-8')
        changed.append(f)

print('fixed:', len(changed))
for f in changed:
    print('-', f)
