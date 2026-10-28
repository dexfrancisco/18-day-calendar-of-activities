import re

with open('18-day-campaign-calendar-a3.html', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'  <!-- TOP 4 PILLARS -->\s*<section class="pillars-grid">.*?</section>\s*', text, re.DOTALL)
if m:
    print('Found pillars block, length:', len(m.group(0)))
else:
    print('Pillars block not found')

