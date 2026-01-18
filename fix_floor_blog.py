from pathlib import Path
import re

p = Path('blog/commercial-kitchen-floor-cleaning-best-practices.html')
s = p.read_text(encoding='utf-8', errors='ignore')
orig = s

# Fix canonical slug
s = s.replace(
    'https://www.groundops.com/blog/commercial-kitchen-floor-cleaning-Preferred-practices',
    'https://www.groundops.com/blog/commercial-kitchen-floor-cleaning-best-practices'
)

# Fix title/h1/headline wording
s = re.sub(r'Commercial Kitchen Floor Cleaning\s+Preferred\s+Practices', 'Commercial Kitchen Floor Cleaning Best Practices', s, flags=re.I)

# Fix keywords phrase
s = re.sub(r'restaurant floor cleaning\s+Preferred\s+practices', 'restaurant floor cleaning best practices', s, flags=re.I)

# Ensure canonical has no trailing slash (Vercel trailingSlash=false)
s = re.sub(
    r'(<link\s+rel="canonical"\s+href="https://www\.groundops\.com/blog/[^\"]+?)/("\s*/?>)',
    r'\1\2',
    s,
    flags=re.I
)

if s != orig:
    p.write_text(s, encoding='utf-8')
    print('patched')
else:
    print('no changes')
