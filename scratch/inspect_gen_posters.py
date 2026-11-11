with open('generate_posters.py', 'r', encoding='utf-8') as f:
    code = f.read()

# Let's find how HTML is generated
import re
print("Functions in generate_posters.py:")
for fn in re.findall(r'def\s+([a-zA-Z0-9_]+)\s*\(', code):
    print(" -", fn)

# Find where HTML templates are defined
for line in code.split('\n'):
    if 'def ' in line or 'HTML' in line or 'render' in line or 'style' in line[:20]:
        print(line[:80])

