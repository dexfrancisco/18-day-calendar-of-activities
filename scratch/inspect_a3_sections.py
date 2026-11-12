with open('18-day-campaign-calendar-a3.html', 'r', encoding='utf-8') as f:
    c = f.read()

import re
matches = re.finditer(r'<section class=["\']month-section["\'][^>]*>', c)
for m in matches:
    print(m.group(0))

rows = re.finditer(r'<div class=["\']grid-[^>]*>', c)
for r in rows:
    print(r.group(0))

