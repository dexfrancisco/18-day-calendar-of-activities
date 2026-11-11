import re

with open('editor.html', 'r', encoding='utf-8') as f:
    text = f.read()

m1 = re.search(r'\.app-logo-badge\s*\{[^}]*\}', text)
print('Current CSS:\n', m1.group(0) if m1 else 'Not found')

m2 = re.search(r'<span class="app-logo-badge">.*?</span>', text)
print('Current HTML:\n', m2.group(0) if m2 else 'Not found')

