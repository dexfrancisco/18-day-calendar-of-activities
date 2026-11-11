with open('editor.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos_09 = text.find('"09":')
pos_10 = text.find('"10":')
pos_11 = text.find('"11":')

block_09 = text[pos_09:pos_10]
block_10 = text[pos_10:pos_11]

print('--- DAY 09 TEMPLATE IN EDITOR.HTML ---')
print('Has End VAWC Forum:', 'End VAWC Action Forum' in block_09)
print('Has Venue ICON:', 'ICON, San Fermin' in block_09)

print('\n--- DAY 10 TEMPLATE IN EDITOR.HTML ---')
print('Has MOVE Forum:', 'Men as Allies' in block_10)
print('Has Safeline 922:', 'Safeline 922' in block_10)
print('Has Venue F. L. Dy:', 'F. L. Dy Colliseum' in block_10)

