with open('scratch/build_editor.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('function updateClearanceRadar')
print(text[idx:idx+4000])

