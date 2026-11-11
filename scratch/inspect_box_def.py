with open('scratch/build_clean_editor.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('function updateTransformBox()')
print(text[idx:idx+1500])

