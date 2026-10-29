import re

with open('18-day-campaign-calendar-a4-page1.html', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'<div class="p1-grid-row3">(.*?)</div>\s*</section>', text, re.DOTALL)
if m:
    print('Row 3 found!')
    cards = re.findall(r'<span class="day-pill">([^<]+)</span>', m.group(1))
    print('Cards in Row 3:', cards)

m_css = re.search(r'\.p1-grid-row3\s*\{([^}]+)\}', text)
if m_css:
    print('.p1-grid-row3 CSS:', m_css.group(1).strip())

