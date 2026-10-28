import re

with open('18-day-campaign-calendar-a4-page1.html', 'r', encoding='utf-8') as f:
    text = f.read()

print("P1 pillars in text:", 'pillars-grid' in text)
m_pillars = re.search(r'  <!-- TOP 4 PILLARS -->\s*<section class="pillars-grid">.*?</section>\s*', text, re.DOTALL)
print("P1 pillars matched:", bool(m_pillars))

with open('18-day-campaign-calendar-a4-page2.html', 'r', encoding='utf-8') as f:
    text2 = f.read()

print("P2 pillars in text:", 'pillars-grid' in text2)
m_pillars2 = re.search(r'  <!-- TOP 4 PILLARS -->\s*<section class="pillars-grid">.*?</section>\s*', text2, re.DOTALL)
print("P2 pillars matched:", bool(m_pillars2))

