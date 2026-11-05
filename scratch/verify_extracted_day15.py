import re

with open('18-Day_Campaign_Calendar_Extracted_Text.txt', 'r', encoding='utf-8') as f:
    text = f.read()

m15 = re.search(r'DAY 15 \|.*?(?=DAY 16 \|)', text, re.DOTALL)
if m15:
    print(m15.group(0))
else:
    print("DAY 15 not found in text!")

