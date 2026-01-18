import re

p='nightly-cleaning.html'
t=open(p,'r',encoding='utf-8',errors='ignore').read()
# Find all substrings around any 'Ã¢'
idxs=[m.start() for m in re.finditer('Ã¢', t)]
print('count Ã¢:', len(idxs))
for i in idxs[:20]:
    snippet=t[i:i+12]
    print('snippet:', snippet, ' | codepoints:', [hex(ord(c)) for c in snippet])

# Print the hero-lead line slice around it
j=t.find('hero-lead')
print('\nhero-lead slice:', t[j:j+200])
