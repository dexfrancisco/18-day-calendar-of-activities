for fn in ['18-day-campaign-calendar-a4-page1.html', '18-day-campaign-calendar-a4.html']:
    with open(fn, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # normalize to \n first
    text = text.replace('\r\n', '\n')
    
    target = '  /* 4 ACTIVITIES CARD (Day 3 with 2 venues) */'
    first_idx = text.find(target)
    second_idx = text.find(target, first_idx + len(target))
    
    if first_idx != -1 and second_idx != -1:
        # remove the second occurrence up to '  /* DAY 2 CARD (3 activities) */'
        day2_target = '  /* DAY 2 CARD (3 activities) */'
        day2_idx = text.find(day2_target, second_idx)
        text = text[:second_idx] + text[day2_idx:]
        print(f"Fixed duplicate in {fn}")
    
    # ensure consistent \r\n line endings
    text = text.replace('\n', '\r\n')
    with open(fn, 'w', encoding='utf-8', newline='') as f:
        f.write(text)

