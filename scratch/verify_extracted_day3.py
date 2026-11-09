import re

with open('18-Day_Campaign_Calendar_Extracted_Text.txt', 'r', encoding='utf-8') as f:
    text = f.read()

m3 = re.search(r'DAY 3 \|.*?(?=DAY 4 \|)', text, re.DOTALL)
if m3:
    print(m3.group(0))
else:
    print("DAY 3 not found in text!")

