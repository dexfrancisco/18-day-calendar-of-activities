import re

with open('18-Day_Campaign_Calendar_Extracted_Text.txt', 'r', encoding='utf-8') as f:
    text = f.read()

m7 = re.search(r'DAY 7 \|.*?(?=DAY 8 \|)', text, re.DOTALL)
if m7:
    print(m7.group(0))
else:
    print("DAY 7 not found in text!")

