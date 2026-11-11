with open('scratch/final_html/09-day-09.html', 'r', encoding='utf-8') as f:
    c9 = f.read()
print('Day 9 has DAY 10 icon?', 'DAY 10.png' in c9)
print('Day 9 has venue ICON?', 'VENUE:</div>\n                    <div class="detail-val-col stroke-val">ICON</div>' in c9)

with open('scratch/final_html/10-day-10.html', 'r', encoding='utf-8') as f:
    c10 = f.read()
print('Day 10 has DAY 9 icon?', 'DAY 9.png' in c10)
print('Day 10 has venue F. L. Dy?', 'F. L. Dy Colliseum' in c10)

