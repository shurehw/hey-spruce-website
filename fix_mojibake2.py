from pathlib import Path

files = [
  'commercial-kitchen-cleaning.html',
  'nightly-cleaning.html',
  'preventive-maintenance.html',
  'hood-exhaust-cleaning.html',
  'foh-cleaning.html',
  'floor-scrubbing.html',
]

# Common mojibake sequences we want to eliminate
repls = {
  'Ã¢â‚¬â€': ' - ',
  'Ã¢â‚¬â€œ': ' - ',
  'Ã¢â‚¬"': ' - ',
  'Ã¢â‚¬Å“': '"',
  'Ã¢â‚¬3': '"',
  'Ã¢â‚¬4': '"',
  'Ã¢â‚¬5': '"',
  'Ã¢â‚¬6': '"',
  'Ã¢â‚¬7': '"',
  'Ã¢â‚¬8': '"',
  'Ã¢â‚¬9': '"',
  'Ã¢â‚¬a': '"',
  'Ã¢â‚¬b': '"',
  'Ã¢â‚¬c': '"',
  'Ã¢â‚¬d': '"',
  'Ã¢â‚¬e': '"',
  'Ã¢â‚¬f': '"',
  'Ã¢â‚¬f': '"',
  'Ã¢â‚¬': '"',
  'Ã¢â‚¬': '"',
  'Ã¢â‚¬': '"',
  'Ã¢â‚¬â„¢': "'",
  'Ã¢â‚¬': "'",
  'Ã¢â‚¬': "'",
  'Ã¢â‚¬': "'",
  'Ã¢â‚¬': "'",
  'Ã¢â‚¬': "'",
  'Ã¢â‚¬\x9d': '"',
  'Ã¢â‚¬\x9c': '"',
  'Ã¢â‚¬\x99': "'",
  'Ã¢â‚¬\x98': "'",
  'Ã¢â‚¬\x9d': '"',
  'Ã¢â‚¬\x9c': '"',
  'Ã¢â‚¬\x93': ' - ',
  'Ã¢â‚¬\x94': ' - ',
  # literal sequences seen in some files
  'Ã¢â‚¬': '',
}

changed = []
for f in files:
    p = Path(f)
    if not p.exists():
        continue
    s = p.read_text(encoding='utf-8', errors='ignore')
    s2 = s
    for k,v in repls.items():
        s2 = s2.replace(k, v)
    # specific known pattern
    s2 = s2.replace('Ã¢â‚¬', '"')
    if s2 != s:
        p.write_text(s2, encoding='utf-8')
        changed.append(f)

print('mojibake fixed:', len(changed))
for f in changed:
    print('-', f)
