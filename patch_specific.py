from pathlib import Path

# Patch emergency blog <ul> block via exact substring replacement
p = Path('blog/emergency-cleaning-failed-inspections.html')
t = p.read_text(encoding='utf-8', errors='ignore')
old = 'Our Emergency Services Include:</h3> <ul> <li>âœ“ SLA-based response time anywhere in LA County</li> <li>âœ“ Former health inspectors on our team</li> <li>âœ“ Complete kitchen recovery in 24 hours</li> <li>âœ“ 100% pass on re-inspection</li> <li>âœ“ Documentation package for inspectors</li> <li>âœ“ priority/365 availability</li> <li>âœ“ Insurance billing assistance</li> <li>âœ“ Discrete service to protect reputation</li> </ul>'
new = 'Our Emergency Services Include:</h3> <ul> <li>âœ“ SLA-based response targets by trade and region</li> <li>âœ“ Former health inspectors on our team</li> <li>âœ“ Corrective actions logged with owners and due dates</li> <li>âœ“ Documented re-inspection readiness (checklists + evidence)</li> <li>âœ“ Documentation package for inspectors</li> <li>âœ“ Issue escalation (per SLA)</li> <li>âœ“ Insurance billing assistance</li> <li>âœ“ Discrete service to protect reputation</li> </ul>'
if old in t:
    t = t.replace(old, new)

# Remove remaining 500+ in DTLA hero badge
p2 = Path('downtown-la-restaurant-cleaning.html')
if p2.exists():
    d = p2.read_text(encoding='utf-8', errors='ignore')
    d = d.replace('ðŸ¢ 500+ DTLA Restaurants Cleaned', 'ðŸ“· Checklists + photo evidence')
    d = d.replace('over 500 DTLA establishments', 'DTLA establishments')
    p2.write_text(d, encoding='utf-8')

p.write_text(t, encoding='utf-8')
print('patched')
