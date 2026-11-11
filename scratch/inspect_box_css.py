with open('scratch/build_clean_editor.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's inspect where transformBox and handles are defined in CSS and JS
print('CSS .transform-box / .transform-handle:')
idx1 = text.find('.transform-box {')
print(text[idx1:idx1+800])

