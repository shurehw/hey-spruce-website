import re
p='blog/emergency-cleaning-failed-inspections.html'
t=open(p,'r',encoding='utf-8',errors='ignore').read()
# Extract the <ul> block after "Our Emergency Services Include" up to </ul>
m=re.search(r'(Our Emergency Services Include:[\s\S]*?<ul>[\s\S]*?</ul>)', t, re.I)
if not m:
    raise SystemExit('not found')
block=m.group(1)
open('tmp_emergency_ul.txt','w',encoding='utf-8').write(block)
print('WROTE tmp_emergency_ul.txt')

m2=re.search(r'(<h3>\s*ðŸš¨[\s\S]{0,80}</h3>)', t)
if m2:
    open('tmp_emergency_h3.txt','w',encoding='utf-8').write(m2.group(1))
    print('WROTE tmp_emergency_h3.txt')
