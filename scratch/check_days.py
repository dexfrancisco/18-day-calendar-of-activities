with open('18-day-campaign-calendar-a3.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
for d in [f"DAY {i}" for i in range(1, 19)] + ["special-title-card"]:
    if d == "special-title-card":
        m = re.search(r'<article class="day-card special-title-card">(.*?)</article>', text, re.DOTALL)
        tag = "PRE-CAMPAIGN"
    else:
        m = re.search(r'<article class="day-card[^"]*">\s*<div class="card-top-bar">\s*<span class="day-pill">' + d + r'</span>(.*?)</article>', text, re.DOTALL)
        tag = d
    if m:
        clean = re.sub(r'<[^>]+>', ' ', m.group(1))
        clean = re.sub(r'&amp;', '&', clean)
        clean = re.sub(r'&ndash;', '–', clean)
        clean = re.sub(r'&quot;', '"', clean)
        clean = re.sub(r'\s+', ' ', clean).strip()
        print(f"=== {tag} ===\n{clean}\n")
    else:
        print(f"=== {tag} NOT FOUND ===")

