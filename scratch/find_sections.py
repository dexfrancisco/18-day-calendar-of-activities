with open('18-day-campaign-calendar-a3.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if '<section class="month-section' in l:
        print(i+1, l.strip())

