from pathlib import Path

moji_files = [
  'commercial-kitchen-cleaning.html',
  'nightly-cleaning.html',
  'preventive-maintenance.html',
  'hood-exhaust-cleaning.html',
  'foh-cleaning.html',
  'floor-scrubbing.html',
]

repl = {
  'Ã¢â‚¬â€': ' - ',
  'Ã¢â‚¬â€œ': ' - ',
  'Ã¢â‚¬"': ' - ',
  'Ã¢â‚¬Å“': '"',
  'Ã¢â‚¬ï¿½': '"',
  'Ã¢â‚¬â„¢': "'",
}

changed = 0
for f in moji_files:
    p = Path(f)
    if not p.exists():
        continue
    s = p.read_text(encoding='utf-8', errors='ignore')
    s2 = s
    for k,v in repl.items():
        s2 = s2.replace(k, v)
    if s2 != s:
        p.write_text(s2, encoding='utf-8')
        changed += 1
print('fixed mojibake in files:', changed)
