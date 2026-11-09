import re

with open('18-Day_Campaign_Calendar_Extracted_Text.txt', 'r', encoding='utf-8') as f:
    text = f.read()

m14 = re.search(r'DAY 14 \|.*?(?=DAY 15 \|)', text, re.DOTALL)
if m14:
    print(m14.group(0))
else:
    print("DAY 14 not found in text!")

