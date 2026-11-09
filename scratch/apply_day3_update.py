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
# 1. A3 Replacements
# ==========================================

a3_day3_act1_old = '''            <!-- Sub 1 -->
            <div class="sub-act-item-4">
              <div class="sub-act-header">ACTIVITY 1</div>
              <div class="sub-lead-name">📍 PDAO &amp; OSCA</div>
              <div class="sub-act-desc">Protection of women with disabilities &amp; senior women; inclusive referral and access to support.</div>
            </div>'''

a3_day3_act1_new = '''            <!-- Sub 1 -->
            <div class="sub-act-item-4">
              <div class="sub-act-header">ACTIVITY 1</div>
              <div class="sub-lead-name">📍 PDAO &amp; OSCA</div>
              <div class="sub-act-desc">Protection of women with disabilities &amp; senior women; inclusive referral and access to support, and Sign Language Orientation.</div>
            </div>'''

print("--- Updating A3 Files ---")
for fp in ['18-day-campaign-calendar-a3.html', '18-day-campaign-calendar.html']:
    update_file(fp, [(a3_day3_act1_old, a3_day3_act1_new)])

# ==========================================
# 2. A4 Page 1 Replacements
# ==========================================

a4_day3_act1_old = '''            <div class="sub-act-item-4">
              <div class="sub-act-header">ACTIVITY 1</div>
              <div class="sub-lead-name">📍 PDAO & OSCA</div>
              <div class="sub-act-desc">Protection of women with disabilities & senior women; inclusive referral and support.</div>
            </div>'''

a4_day3_act1_new = '''            <div class="sub-act-item-4">
              <div class="sub-act-header">ACTIVITY 1</div>
              <div class="sub-lead-name">📍 PDAO & OSCA</div>
              <div class="sub-act-desc">Protection of women with disabilities & senior women; inclusive referral, support, and Sign Language Orientation.</div>
            </div>'''

print("--- Updating A4 Page 1 ---")
update_file('18-day-campaign-calendar-a4-page1.html', [(a4_day3_act1_old, a4_day3_act1_new)])

# ==========================================
# 3. A4 Combined Replacements
# ==========================================

print("--- Updating A4 Combined ---")
update_file('18-day-campaign-calendar-a4.html', [(a4_day3_act1_old, a4_day3_act1_new)])

