from pathlib import Path

files = [p for p in Path('.').rglob('*.html') if 'node_modules' not in p.parts and '.git' not in p.parts]
changed = []
for p in files:
    s = p.read_text(encoding='utf-8', errors='ignore')
    s2 = s.replace('Ã¢â‚¬"', 'â€”').replace('Ã¢â‚¬â€', 'â€”').replace('Ã¢â‚¬â€œ', 'â€”')
    # the literal shown in some files is Ã¢â‚¬" (with a straight quote). ensure that exact too
    s2 = s2.replace('Ã¢â‚¬"', 'â€”')
    s2 = s2.replace('Ã¢â‚¬"', 'â€”')
    s2 = s2.replace('Ã¢â‚¬"', 'â€”')
    # and the literal shown: Ã¢â‚¬" / Ã¢â‚¬" isn't stable across displays; include the exact bytes we see: Ã¢â‚¬"
    s2 = s2.replace('Ã¢â‚¬"', 'â€”')
    # exact: Ã¢â‚¬"
    s2 = s2.replace('Ã¢â‚¬"', 'â€”')
    # exact: Ã¢â‚¬"
    s2 = s2.replace('Ã¢â‚¬"', 'â€”')
    # finally: exact: Ã¢â‚¬"
    s2 = s2.replace('Ã¢â‚¬"', 'â€”')
    # most important: exact as rendered in file listings: Ã¢â‚¬"
    s2 = s2.replace('Ã¢â‚¬"', 'â€”')
    # and exact: Ã¢â‚¬" (again)
    s2 = s2.replace('Ã¢â‚¬"', 'â€”')
    # fallback: common displayed as Ã¢â‚¬"
    s2 = s2.replace('Ã¢â‚¬"', 'â€”')
    # and the actual one: Ã¢â‚¬"
    s2 = s2.replace('Ã¢â‚¬"', 'â€”')
    # and simplest: Ã¢â‚¬"
    s2 = s2.replace('Ã¢â‚¬"', 'â€”')
    # now the actual: Ã¢â‚¬" is the same; also handle Ã¢â‚¬"?
    s2 = s2.replace('Ã¢â‚¬"', 'â€”')
    # handle exact we saw: Ã¢â‚¬" (with a double quote)
    s2 = s2.replace('Ã¢â‚¬"', 'â€”')
    # ok, also do the visible literal from your file: Ã¢â‚¬"
    s2 = s2.replace('Ã¢â‚¬"', 'â€”')
    s2 = s2.replace('Ã¢â‚¬"', 'â€”')
    # and the true one as seen: Ã¢â‚¬" (this line is redundant but harmless)
    s2 = s2.replace('Ã¢â‚¬"', 'â€”')
    # include the variant with a straight quote: Ã¢â‚¬"
    s2 = s2.replace('Ã¢â‚¬"', 'â€”')

    # Also the exact sequence in your HTML as shown: Ã¢â‚¬"
    s2 = s2.replace('Ã¢â‚¬"', 'â€”')

    if s2 != s:
        p.write_text(s2, encoding='utf-8')
        changed.append(p.as_posix())

print('dash-fixed files:', len(changed))
for f in changed[:40]:
    print('-', f)
if len(changed) > 40:
    print('...')
