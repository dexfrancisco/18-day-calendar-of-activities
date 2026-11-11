with open('scratch/build_clean_editor.py', 'r', encoding='utf-8') as f:
    text = f.read()

import re
m = re.search(r'\.app-logo-badge\s*\{[^}]*\}', text)
print('Found:', m.group(0) if m else 'Not found')

