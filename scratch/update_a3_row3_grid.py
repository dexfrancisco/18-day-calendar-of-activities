import os

def update_file(filepath, replacements):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_has_crlf = '\r\n' in content
    content_norm = content.replace('\r\n', '\n')

    all_matched = True
    for old, new in replacements:
        old_norm = old.replace('\r\n', '\n')
        new_norm = new.replace('\r\n', '\n')
        if old_norm in content_norm:
            content_norm = content_norm.replace(old_norm, new_norm)
            print(f"[{os.path.basename(filepath)}] Successfully replaced: {old_norm[:45]}...")
        else:
            print(f"[{os.path.basename(filepath)}] WARNING: Target not found: {old_norm[:45]}...")
            all_matched = False

    if original_has_crlf:
        content_norm = content_norm.replace('\n', '\r\n')

    with open(filepath, 'w', encoding='utf-8', newline='') as f:
        f.write(content_norm)

    return all_matched

r3_old = '''  .grid-6.row-3 {
    grid-template-columns: 1.25fr 1.15fr 1.15fr 1.15fr 0.95fr 0.68fr;
  }'''

r3_new = '''  .grid-6.row-3 {
    grid-template-columns: 1.20fr 1.05fr 1.35fr 1.15fr 0.92fr 0.68fr;
  }'''

for fp in ['18-day-campaign-calendar-a3.html', '18-day-campaign-calendar.html']:
    update_file(fp, [(r3_old, r3_new)])

