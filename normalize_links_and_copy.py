from __future__ import annotations

from pathlib import Path
import re

ROOT = Path('.')

# include nested HTML (case-studies/, blog/, etc.)
html_files = [p for p in ROOT.rglob('*.html') if 'node_modules' not in p.parts and '.git' not in p.parts]

SKIP_PREFIXES = ('http://', 'https://', '//', 'mailto:', 'tel:')

href_pat = re.compile(r'''\bhref\s*=\s*(?P<q>["'])(?P<url>[^"']+?)(?P=q)''', re.IGNORECASE)

# common mojibake sequences for smart punctuation
MOJIBAKE_REPLACEMENTS = {
    'Ã¢â‚¬Å“': '"',
    'Ã¢â‚¬\x9d': '"',
    'Ã¢â‚¬\x98': "'",
    'Ã¢â‚¬\x99': "'",
    'Ã¢â‚¬\x9c': '"',
    'Ã¢â‚¬\x9d': '"',
    'Ã¢â‚¬â„¢': "'",
    'Ã¢â‚¬Ëœ': "'",
    'Ã¢â‚¬â€': 'â€”',
    'Ã¢â‚¬â€œ': 'â€”',
    'Ã¢â‚¬"': 'â€”',
}

# also handle raw unicode sequences sometimes present after bad decode
RAW_SEQ_REPLACEMENTS = {
    "\u00e2\u20ac\u0153": '"',  # Ã¢â‚¬Å“
    "\u00e2\u20ac\u009d": '"',  # Ã¢â‚¬
    "\u00e2\u20ac\u0098": "'",  # Ã¢â‚¬
    "\u00e2\u20ac\u0099": "'",  # Ã¢â‚¬
}


def normalize_href(url: str, current_file: Path) -> str:
    u = url.strip()

    if not u or u.startswith('#') or u.startswith(SKIP_PREFIXES):
        return url

    # preserve query/fragment
    m = re.match(r'^(?P<path>[^?#]+)(?P<suffix>[?#].*)?$', u)
    if not m:
        return url

    path = m.group('path')
    suffix = m.group('suffix') or ''

    # Only normalize .html paths
    if not path.endswith('.html'):
        # special case: index.html#... sometimes appears as full path in href value
        return url

    # Strip .html
    path_no_ext = path[:-5]

    # If it's exactly index.html => /
    if path == 'index.html':
        return '/' + suffix if suffix.startswith('#') or suffix.startswith('?') else '/'

    # If it's index.html#section => /#section
    if path == 'index.html' and suffix.startswith('#'):
        return '/'+suffix

    # If path already starts with /, keep absolute
    if path_no_ext.startswith('/'):
        return path_no_ext + suffix

    # Determine if this was a relative link within blog/ or case-studies/
    parent_dir = current_file.parent.as_posix().lower()

    # if link includes a directory already (blog/foo.html)
    if '/' in path_no_ext:
        return '/' + path_no_ext + suffix

    # if current file is in /blog and link is relative slug.html, keep it within /blog
    if parent_dir.endswith('/blog'):
        return '/blog/' + path_no_ext + suffix

    # if current file is in /case-studies and link is relative, keep it within /case-studies
    if parent_dir.endswith('/case-studies'):
        return '/case-studies/' + path_no_ext + suffix

    # default: root-level page
    return '/' + path_no_ext + suffix


changed_files = []

for p in html_files:
    try:
        s = p.read_text(encoding='utf-8', errors='ignore')
    except Exception:
        continue

    s2 = s

    # Mojibake fixes
    for bad, good in MOJIBAKE_REPLACEMENTS.items():
        s2 = s2.replace(bad, good)
    for bad, good in RAW_SEQ_REPLACEMENTS.items():
        s2 = s2.replace(bad, good)

    # Copy artifact: "Preferred result" wording
    s2 = s2.replace('You get the Preferred result', 'You get the best result')

    # Link normalization
    def _href_sub(m: re.Match) -> str:
        q = m.group('q')
        url = m.group('url')

        # also normalize index.html#... and index.html anchors even if not ending in .html
        if url.startswith('index.html#'):
            return f'href={q}/#{url.split("#",1)[1]}{q}'
        if url == 'index.html':
            return f'href={q}/{q}'

        new_url = normalize_href(url, p)
        if new_url != url:
            return f'href={q}{new_url}{q}'
        return m.group(0)

    s2 = href_pat.sub(_href_sub, s2)

    if s2 != s:
        p.write_text(s2, encoding='utf-8')
        changed_files.append(p.as_posix())

print('updated files:', len(changed_files))
for f in changed_files[:50]:
    print('-', f)
if len(changed_files) > 50:
    print('...')
