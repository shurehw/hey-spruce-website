import re
p='blog/emergency-cleaning-failed-inspections.html'
t=open(p,'r',encoding='utf-8',errors='ignore').read()
for needle in ['Our Emergency Services Include','2-hour response time','EMERGENCY HOTLINE','Our Guarantee:','24/7/365']:
    print(needle, 'FOUND' if needle.lower() in t.lower() else 'NOT_FOUND')

m=re.search(r'(Our Emergency Services Include[\s\S]{0,1200})', t, re.I)
if m:
    snip=m.group(1)[:900]
    snip=snip.replace('âœ“','[ok]')
    print('\nSNIP:\n', snip)
