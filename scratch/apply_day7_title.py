import os
import re

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

# ==========================================
# Day 7 Replacement
# ==========================================

day7_act_old = '''            <div class="single-act-block">
              <span class="act-tag-badge">MAIN ACTIVITY</span>
              <p class="single-act-desc">Safe workplace, anti-sexual harassment, internal reporting and protection mechanisms.</p>
            </div>'''

day7_act_new = '''            <div class="single-act-block">
              <span class="act-tag-badge">MAIN ACTIVITY</span>
              <p class="single-act-desc">Gender Sensitivity Training for LGU Employees and LDC Members</p>
            </div>'''

print("--- Updating A3 Files ---")
for fp in ['18-day-campaign-calendar-a3.html', '18-day-campaign-calendar.html']:
    update_file(fp, [(day7_act_old, day7_act_new)])

print("--- Updating A4 Page 1 ---")
update_file('18-day-campaign-calendar-a4-page1.html', [(day7_act_old, day7_act_new)])

print("--- Updating A4 Combined ---")
update_file('18-day-campaign-calendar-a4.html', [(day7_act_old, day7_act_new)])

