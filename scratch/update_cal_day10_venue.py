import re

files = [
    '18-day-campaign-calendar-a3.html',
    '18-day-campaign-calendar.html',
    'Final Copy/18-day-campaign-calendar-a3.html',
    'Final Copy/18-day-campaign-calendar.html',
    '18-day-campaign-calendar-a4.html',
    '18-day-campaign-calendar-a4-page2.html'
]

old_venue = "F. L. Dy Colliseum, District III, Cauayan City, Isabela"
new_venue = "Isabela Convention Center, San Fermin, Cauayan City, Isabela"

for fp in files:
    with open(fp, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Locate DAY 10 block
    # Matches from DAY 10 up to DAY 11 or end of article
    pattern = r'(<!--\s*DAY 10\s*-->.*?)(F\. L\. Dy Colliseum, District III, Cauayan City, Isabela)(.*?<!--\s*DAY 11\s*-->)'
    
    match = re.search(pattern, content, re.DOTALL)
    if match:
        new_content = content[:match.start(2)] + new_venue + content[match.end(2):]
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"✓ Successfully updated Day 10 venue in {fp}")
    else:
        # Fallback for files where comment format might differ
        # Search for DAY 10 pill followed by F. L. Dy
        pattern2 = r'(DAY 10.*?)(F\. L\. Dy Colliseum, District III, Cauayan City, Isabela)(.*?DAY 11)'
        match2 = re.search(pattern2, content, re.DOTALL)
        if match2:
            new_content = content[:match2.start(2)] + new_venue + content[match2.end(2):]
            with open(fp, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"✓ Successfully updated (pattern 2) Day 10 venue in {fp}")
        else:
            print(f"✗ Could not find Day 10 with old venue in {fp}")

