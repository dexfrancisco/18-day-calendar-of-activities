with open('scratch/build_editor.py', 'r', encoding='utf-8') as f:
    text = f.read()

print('build_editor.py length:', len(text))
# Check if it writes editor.html
print('writes editor.html:', 'editor.html' in text)
# Find function names or structure in build_editor.py
import re
lines = text.split('\n')
print(f'Total lines: {len(lines)}')
for i in range(min(50, len(lines))):
    print(lines[i])

