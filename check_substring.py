t=open('blog/emergency-cleaning-failed-inspections.html','r',encoding='utf-8',errors='ignore').read()
print('HAS_SUBSTRING', 'SLA-based response time anywhere in LA County' in t)
# show a smaller slice around 'Our Emergency Services Include' index
idx=t.lower().find('our emergency services include')
print('IDX', idx)
print(t[idx:idx+300].replace('âœ“','[ok]'))
