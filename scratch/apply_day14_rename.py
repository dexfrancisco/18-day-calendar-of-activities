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

a3_day14_old = '''          <div class="single-act-block">
            <span class="act-tag-badge">MAIN ACTIVITY</span>
            <p class="single-act-desc dense">Painting Competition, Spoken Poetry, Declamation and Wearable Fashion Designing</p>
            <div style="font-family: 'Montserrat', sans-serif; font-size: 29px; font-weight: 800; color: #9a3412; background: #ffedd5; border: 1.5px solid #fed7aa; border-radius: 6px; padding: 4px 12px; align-self: flex-start; margin-top: 2px;">Awarding of Winners</div>
          </div>'''

a3_day14_new = '''          <div class="single-act-block">
            <span class="act-tag-badge">MAIN ACTIVITY</span>
            <p class="single-act-desc dense">Orange Exhibit and Orange Bubble Culture Arts and Public Advocacy: Painting Competition, Spoken Poetry, Declamation and Wearable Fashion Designing</p>
            <div style="font-family: 'Montserrat', sans-serif; font-size: 27px; font-weight: 800; color: #9a3412; background: #ffedd5; border: 1.5px solid #fed7aa; border-radius: 6px; padding: 3px 10px; align-self: flex-start; margin-top: 2px;">Awarding of Winners</div>
          </div>'''

a3_css_dense_old = '''  .single-act-desc.dense {
    font-size: 34.5px;
    line-height: 1.36;
  }'''

a3_css_dense_new = '''  .single-act-desc.dense {
    font-size: 27.5px;
    line-height: 1.25;
  }'''

# Also let's slightly adjust Row 3 in A3 from 1.05fr to 1.15fr for Day 14 (Column 2)
a3_grid_r3_old = '''  .grid-6.row-3 {
    grid-template-columns: 1.20fr 1.05fr 1.35fr 1.15fr 0.92fr 0.68fr;
  }'''

a3_grid_r3_new = '''  .grid-6.row-3 {
    grid-template-columns: 1.16fr 1.14fr 1.30fr 1.14fr 0.90fr 0.68fr;
  }'''

a3_replacements = [
    (a3_day14_old, a3_day14_new),
    (a3_css_dense_old, a3_css_dense_new),
    (a3_grid_r3_old, a3_grid_r3_new)
]

print("--- Updating A3 Files ---")
for fp in ['18-day-campaign-calendar-a3.html', '18-day-campaign-calendar.html']:
    update_file(fp, a3_replacements)

# ==========================================
# 2. A4 Page 2 Replacements
# ==========================================

a4_p2_day14_old = '''            <div class="single-act-block">
              <span class="act-tag-badge">MAIN ACTIVITY</span>
              <p class="single-act-desc dense">Painting Competition, Spoken Poetry, Declamation and Wearable Fashion Designing</p>
              <div style="font-family: 'Montserrat', sans-serif; font-size: 19px; font-weight: 800; color: #9a3412; background: #ffedd5; border: 1.2px solid #fed7aa; border-radius: 5px; padding: 3px 8px; align-self: flex-start;">Awarding of Winners</div>
            </div>'''

a4_p2_day14_new = '''            <div class="single-act-block">
              <span class="act-tag-badge">MAIN ACTIVITY</span>
              <p class="single-act-desc dense">Orange Exhibit and Orange Bubble Culture Arts and Public Advocacy: Painting Competition, Spoken Poetry, Declamation and Wearable Fashion Designing</p>
              <div style="font-family: 'Montserrat', sans-serif; font-size: 17.5px; font-weight: 800; color: #9a3412; background: #ffedd5; border: 1.2px solid #fed7aa; border-radius: 5px; padding: 2.5px 7px; align-self: flex-start;">Awarding of Winners</div>
            </div>'''

a4_p2_css_dense_old = '''  .single-act-desc.dense {
    font-size: 26.5px;
    line-height: 1.28;
  }'''

a4_p2_css_dense_new = '''  .single-act-desc.dense {
    font-size: 20px;
    line-height: 1.20;
  }'''

a4_p2_grid_old = '''  .p2-grid-row2 {
    display: grid;
    grid-template-columns: 1.05fr 1.05fr 1.48fr 1.12fr 1.04fr;
    gap: 8px;
    flex: 1;
  }'''

a4_p2_grid_new = '''  .p2-grid-row2 {
    display: grid;
    grid-template-columns: 1.02fr 1.14fr 1.42fr 1.12fr 1.02fr;
    gap: 8px;
    flex: 1;
  }'''

a4_p2_replacements = [
    (a4_p2_day14_old, a4_p2_day14_new),
    (a4_p2_css_dense_old, a4_p2_css_dense_new),
    (a4_p2_grid_old, a4_p2_grid_new)
]

print("--- Updating A4 Page 2 ---")
update_file('18-day-campaign-calendar-a4-page2.html', a4_p2_replacements)

# ==========================================
# 3. A4 Combined Replacements
# ==========================================

a4_comb_replacements = [
    (a4_p2_day14_old, a4_p2_day14_new),
    (a4_p2_css_dense_old, a4_p2_css_dense_new),
    (a4_p2_grid_old, a4_p2_grid_new)
]

print("--- Updating A4 Combined ---")
update_file('18-day-campaign-calendar-a4.html', a4_comb_replacements)

