import re
p='blog/emergency-cleaning-failed-inspections.html'
t=open(p,'r',encoding='utf-8',errors='ignore').read()
m=re.search(r'(<h3>\s*ðŸš¨[^<]*</h3>)', t)
print(m.group(1) if m else 'NO_H3_FOUND')
