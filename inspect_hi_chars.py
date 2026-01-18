import re
p='nightly-cleaning.html'
t=open(p,'r',encoding='utf-8',errors='ignore').read()
# Extract the 12 chars starting at 'not '
start=t.find('not ')
frag=t[start:start+30]
print('frag:', frag)
print('codepoints:', [(c, hex(ord(c))) for c in frag])

# Find any characters with ord>127 in the whole file and show top few unique
hi=set([c for c in t if ord(c)>127])
print('unique high chars:', len(hi))
print([(c, hex(ord(c))) for c in sorted(hi, key=lambda x: ord(x))][:30])
