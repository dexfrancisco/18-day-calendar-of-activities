with open('scratch/build_editor.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's search for <script> in text
idx = text.find('<script>')
if idx != -1:
    print('Found <script> at index:', idx)
    script_content = text[idx:idx+4000]
    print(script_content[:2000])
else:
    print('No <script> tag found!')

