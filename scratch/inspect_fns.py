with open('scratch/build_editor.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('<script>')
script_content = text[idx:]

# Find all function declarations
import re
functions = re.findall(r'function\s+([a-zA-Z0-9_]+)\s*\(', script_content)
print('Functions defined in script:')
for fn in functions:
    print(' -', fn)

