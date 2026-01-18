import re
p = 'blog/emergency-cleaning-failed-inspections.html'
t = open(p,'r',encoding='utf-8',errors='ignore').read()
print('TITLE:', re.search(r'<title>([\s\S]*?)</title>', t, re.I).group(1))
print('DESC:', re.search(r'<meta name="description" content="([\s\S]*?)"', t, re.I).group(1))
print('CANON:', re.search(r'<link rel="canonical" href="([\s\S]*?)"', t, re.I).group(1))
