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
            print(f"[{filepath}] Successfully replaced: {old_norm[:40]}...")
        else:
            print(f"[{filepath}] WARNING: Target not found: {old_norm[:40]}...")
            all_matched = False

    if original_has_crlf:
        content_norm = content_norm.replace('\n', '\r\n')

    with open(filepath, 'w', encoding='utf-8', newline='') as f:
        f.write(content_norm)

    return all_matched

# --- PAGE 1 ---
with open('18-day-campaign-calendar-a4-page1.html', 'r', encoding='utf-8') as f:
    p1 = f.read()

# Remove pillars-grid
p1_pillars_re = r'  <!-- TOP 4 PILLARS -->\s*<section class="pillars-grid">.*?</section>\s*'
p1 = re.sub(p1_pillars_re, '', p1, flags=re.DOTALL)

# CSS updates for Page 1
p1 = p1.replace('margin-bottom: 10px;\n    z-index: 5;', 'margin-bottom: 16px;\n    z-index: 5;')
p1 = p1.replace('gap: 10px;\n    flex: 1;\n    z-index: 5;\n    justify-content: space-between;', 'gap: 14px;\n    flex: 1;\n    z-index: 5;\n    justify-content: space-between;')
p1 = p1.replace('font-size: 24px;\n    font-weight: 900;\n    letter-spacing: 1.5px;\n    padding: 6px 18px;', 'font-size: 27px;\n    font-weight: 900;\n    letter-spacing: 2px;\n    padding: 8px 22px;')

with open('18-day-campaign-calendar-a4-page1.html', 'w', encoding='utf-8', newline='') as f:
    f.write(p1)
print("Updated 18-day-campaign-calendar-a4-page1.html")

# --- PAGE 2 ---
with open('18-day-campaign-calendar-a4-page2.html', 'r', encoding='utf-8') as f:
    p2 = f.read()

# Remove pillars-grid
p2_pillars_re = r'  <!-- TOP 4 PILLARS -->\s*<section class="pillars-grid">.*?</section>\s*'
p2 = re.sub(p2_pillars_re, '', p2, flags=re.DOTALL)

# CSS updates for Page 2
p2 = p2.replace('margin-bottom: 10px;\n    z-index: 5;', 'margin-bottom: 16px;\n    z-index: 5;')
p2 = p2.replace('gap: 10px;\n    flex: 1;\n    z-index: 5;\n    justify-content: space-between;', 'gap: 14px;\n    flex: 1;\n    z-index: 5;\n    justify-content: space-between;')
p2 = p2.replace('font-size: 24px;\n    font-weight: 900;\n    letter-spacing: 1.5px;\n    padding: 6px 18px;', 'font-size: 27px;\n    font-weight: 900;\n    letter-spacing: 2px;\n    padding: 8px 22px;')

# Day 18 on Page 2
day18_p2_old = '''        <!-- DAY 18 -->
        <article class="day-card active-day">
          <div class="card-top-bar">
            <span class="day-pill">DAY 18</span>
            <span class="date-text">DEC 12</span>
            <span class="weekday-text">SAT</span>
          </div>
          <div class="card-body-single">
            <div class="single-lead-block">
              <span class="lead-tag-row">
                <svg viewBox="0 0 16 16"><path d="M8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10zm0-7a3 3 0 1 1 0-6 3 3 0 0 1 0 6z"/></svg>
                LEAD OFFICE
              </span>
              <span class="single-lead-name">GAD Office</span>
            </div>
            <div class="single-act-block">
              <span class="act-tag-badge">MAIN ACTIVITY</span>
              <p class="single-act-desc">Posting of Accomplishment Reports for the 18-day Campaign</p>
            </div>
            <div class="card-venue-box" style="background: #fffaf5; border: 1.5px solid #fed7aa; color: #ea580c;">
              <svg viewBox="0 0 24 24" style="fill: #ea580c; width: 17px; height: 17px;"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 14.5v-9l6 4.5-6 4.5z"/></svg>
              <span><strong>Online:</strong> Social Media & Portals</span>
            </div>
          </div>
        </article>'''

day18_p2_new = '''        <!-- DAY 18 -->
        <article class="day-card active-day">
          <div class="card-top-bar">
            <span class="day-pill">DAY 18</span>
            <span class="date-text">DEC 12</span>
            <span class="weekday-text">SAT</span>
          </div>
          <div class="card-body-multi">
            <div class="sub-act-item-2">
              <div class="sub-act-header">ACTIVITY 1</div>
              <div class="sub-lead-name">📍 GAD Office</div>
              <div class="sub-act-desc">Display of Orange Exhibits</div>
            </div>
            <div class="sub-act-item-2">
              <div class="sub-act-header">ACTIVITY 2</div>
              <div class="sub-lead-name">📍 GAD Office</div>
              <div class="sub-act-desc">Posting of Accomplishment Reports for the 18-day Campaign</div>
            </div>
            <div class="card-venue-box" style="background: #fffaf5; border: 1.5px solid #fed7aa; color: #ea580c;">
              <svg viewBox="0 0 24 24" style="fill: #ea580c; width: 17px; height: 17px;"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 14.5v-9l6 4.5-6 4.5z"/></svg>
              <span><strong>Online:</strong> Social Media & Portals</span>
            </div>
          </div>
        </article>'''

p2 = p2.replace(day18_p2_old, day18_p2_new)

with open('18-day-campaign-calendar-a4-page2.html', 'w', encoding='utf-8', newline='') as f:
    f.write(p2)
print("Updated 18-day-campaign-calendar-a4-page2.html")

# --- COMBINED A4 ---
with open('18-day-campaign-calendar-a4.html', 'r', encoding='utf-8') as f:
    pcomb = f.read()

pcomb = re.sub(p1_pillars_re, '', pcomb, flags=re.DOTALL)
pcomb = pcomb.replace('margin-bottom: 10px;\n    z-index: 5;', 'margin-bottom: 16px;\n    z-index: 5;')
pcomb = pcomb.replace('gap: 10px;\n    flex: 1;\n    z-index: 5;\n    justify-content: space-between;', 'gap: 14px;\n    flex: 1;\n    z-index: 5;\n    justify-content: space-between;')
pcomb = pcomb.replace('font-size: 24px;\n    font-weight: 900;\n    letter-spacing: 1.5px;\n    padding: 6px 18px;', 'font-size: 27px;\n    font-weight: 900;\n    letter-spacing: 2px;\n    padding: 8px 22px;')
pcomb = pcomb.replace(day18_p2_old, day18_p2_new)

with open('18-day-campaign-calendar-a4.html', 'w', encoding='utf-8', newline='') as f:
    f.write(pcomb)
print("Updated 18-day-campaign-calendar-a4.html")

