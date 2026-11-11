import os
import re

with open('editor.html', 'r', encoding='utf-8') as f:
    html = f.read()

print('HTML total size:', len(html), 'bytes')

# Check title
m_title = re.search(r'<title>(.*?)</title>', html)
print('Title:', m_title.group(1) if m_title else 'None')

# Check if SCHEDULE_DATA is embedded
print('SCHEDULE_DATA in html:', 'const SCHEDULE_DATA =' in html)

# Check features in JS
js_features = [
    'fitToViewport',
    'selectElement',
    'updateInspector',
    'updateRadar',
    'exportHighResPng',
    'copyLayoutJson',
    'startDragging',
    'switchDay',
]
for feat in js_features:
    print(f'JS feature {feat}:', feat in html)

# Check fonts
print('Gotham fonts embedded:', 'Gotham-Bold' in html, 'Gotham-Black' in html)

# Check days available
day_matches = re.findall(r'<option value=\"(\d+)\">', html)
print('Days count in dropdown:', len(day_matches), 'Days:', day_matches)

