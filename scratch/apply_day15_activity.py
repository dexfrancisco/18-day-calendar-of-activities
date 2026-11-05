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

a3_day15_old = '''      <!-- DAY 15 (Moved from Day 16: Culminating Activity) -->
      <article class="day-card active-day">
        <div class="card-top-bar">
          <span class="day-pill">DAY 15</span>
          <span class="date-text">DEC 9</span>
          <span class="weekday-text">WED</span>
        </div>
        <div class="card-body-single">
          <div class="single-lead-block">
            <span class="lead-tag-row">
              <svg viewBox="0 0 16 16"><path d="M8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10zm0-7a3 3 0 1 1 0-6 3 3 0 0 1 0 6z"/></svg>
              LEAD OFFICE
            </span>
            <span class="single-lead-name">Culminating Activity led by LGU Cauayan</span>
          </div>
          <div class="single-act-block">
            <span class="act-tag-badge">MAIN ACTIVITY</span>
            <p class="single-act-desc">Awarding of all barangays and offices, recognition of partners, presentation of commitments, and ceremonial signing of Memorandum of Partnership with NAPC and OPAPRU.</p>
          </div>
          <div class="single-partner-box">
            <strong>Partners:</strong> DILG, NAPC, OPAPRU, PCW, All Offices, All Partners, Barangay, CSOs
          </div>
          <div class="card-venue-box">
            <svg viewBox="0 0 16 16"><path d="M8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10zm0-7a3 3 0 1 1 0-6 3 3 0 0 1 0 6z"/></svg>
            <span><strong>Venue:</strong> F. L. Dy Colliseum, District III, Cauayan City, Isabela</span>
          </div>
        </div>
      </article>'''

a3_day15_new = '''      <!-- DAY 15 (2 Activities: Culminating Activity, GAD PROJECT ORANGE RISE) -->
      <article class="day-card active-day">
        <div class="card-top-bar">
          <span class="day-pill">DAY 15</span>
          <span class="date-text">DEC 9</span>
          <span class="weekday-text">WED</span>
        </div>
        <div class="card-body-multi">
          <!-- Sub 1 -->
          <div class="sub-act-item-2">
            <div class="sub-act-header">ACTIVITY 1</div>
            <div class="sub-lead-name">📍 Culminating Activity led by LGU Cauayan</div>
            <div class="sub-act-desc">Awarding of all barangays &amp; offices, recognition of partners, presentation of commitments, and ceremonial signing of Memorandum of Partnership with NAPC and OPAPRU.</div>
          </div>
          <!-- Sub 2 -->
          <div class="sub-act-item-2">
            <div class="sub-act-header">ACTIVITY 2</div>
            <div class="sub-lead-name">📍 GAD Office</div>
            <div class="sub-act-desc">PROJECT ORANGE RISE: Empowering 12 Women in Economic Enterprise through the Proceeds of Orange Run</div>
          </div>
          <div class="card-partner-box">
            <strong>Partners:</strong> DILG, NAPC, OPAPRU, PCW, CEDIPO, CSWDO, City Budget Office, City Accounting Office, GSO, DTI, TESDA, Cooperatives, Barangay Local Government Units, All Offices, All Partners, CSOs
          </div>
          <div class="card-venue-box">
            <svg viewBox="0 0 16 16"><path d="M8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10zm0-7a3 3 0 1 1 0-6 3 3 0 0 1 0 6z"/></svg>
            <span><strong>Venue:</strong> F. L. Dy Colliseum, District III, Cauayan City, Isabela</span>
          </div>
        </div>
      </article>'''

# CSS for Row 3 in A3: Increase Day 15 column width from 1.15fr to 1.35fr
a3_grid_r3_old = '.grid-6.row-3 { grid-template-columns: 1.25fr 1.15fr 1.15fr 1.15fr 0.95fr 0.68fr; }'
a3_grid_r3_new = '.grid-6.row-3 { grid-template-columns: 1.20fr 1.05fr 1.35fr 1.15fr 0.92fr 0.68fr; }'

a3_replacements = [
    (a3_day15_old, a3_day15_new),
    (a3_grid_r3_old, a3_grid_r3_new)
]

print("--- Updating A3 Files ---")
for fp in ['18-day-campaign-calendar-a3.html', '18-day-campaign-calendar.html']:
    update_file(fp, a3_replacements)

# ==========================================
# 2. A4 Page 2 Replacements
# ==========================================

a4_p2_day15_old = '''        <!-- DAY 15 (Culminating Activity) -->
        <article class="day-card active-day">
          <div class="card-top-bar">
            <span class="day-pill">DAY 15</span>
            <span class="date-text">DEC 9</span>
            <span class="weekday-text">WED</span>
          </div>
          <div class="card-body-single">
            <div class="single-lead-block">
              <span class="lead-tag-row">
                <svg viewBox="0 0 16 16"><path d="M8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10zm0-7a3 3 0 1 1 0-6 3 3 0 0 1 0 6z"/></svg>
                LEAD OFFICE
              </span>
              <span class="single-lead-name">Culminating Activity led by LGU</span>
            </div>
            <div class="single-act-block">
              <span class="act-tag-badge">MAIN ACTIVITY</span>
              <p class="single-act-desc">Awarding of all barangays & offices, recognition of partners, presentation of commitments, and ceremonial signing with NAPC & OPAPRU.</p>
            </div>
            <div class="single-partner-box">
              <strong>Partners:</strong> DILG, NAPC, OPAPRU, PCW, All Offices, All Partners, Barangay, CSOs
            </div>
            <div class="card-venue-box">
              <svg viewBox="0 0 16 16"><path d="M8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10zm0-7a3 3 0 1 1 0-6 3 3 0 0 1 0 6z"/></svg>
              <span><strong>Venue:</strong> F. L. Dy Colliseum</span>
            </div>
          </div>
        </article>'''

a4_p2_day15_new = '''        <!-- DAY 15 (2 Activities: Culminating Activity, GAD PROJECT ORANGE RISE) -->
        <article class="day-card active-day">
          <div class="card-top-bar">
            <span class="day-pill">DAY 15</span>
            <span class="date-text">DEC 9</span>
            <span class="weekday-text">WED</span>
          </div>
          <div class="card-body-multi">
            <div class="sub-act-item-2">
              <div class="sub-act-header">ACTIVITY 1</div>
              <div class="sub-lead-name">📍 Culminating Activity led by LGU</div>
              <div class="sub-act-desc">Awarding of barangays &amp; offices, partner recognition, commitment presentations, ceremonial signing with NAPC &amp; OPAPRU.</div>
            </div>
            <div class="sub-act-item-2">
              <div class="sub-act-header">ACTIVITY 2</div>
              <div class="sub-lead-name">📍 GAD Office</div>
              <div class="sub-act-desc">PROJECT ORANGE RISE: Empowering 12 Women in Economic Enterprise through the Proceeds of Orange Run</div>
            </div>
            <div class="card-partner-box">
              <strong>Partners:</strong> DILG, NAPC, OPAPRU, PCW, CEDIPO, CSWDO, City Budget Office, City Accounting Office, GSO, DTI, TESDA, Cooperatives, Barangay Local Government Units, All Offices, All Partners, CSOs
            </div>
            <div class="card-venue-box">
              <svg viewBox="0 0 16 16"><path d="M8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10zm0-7a3 3 0 1 1 0-6 3 3 0 0 1 0 6z"/></svg>
              <span><strong>Venue:</strong> F. L. Dy Colliseum</span>
            </div>
          </div>
        </article>'''

# CSS for Row 2 in A4 P2: Day 15 width adjustment from 1.15fr to 1.30fr
a4_p2_grid_old = '''  .p2-grid-row2 {
    display: grid;
    grid-template-columns: 1.12fr 1.15fr 1.30fr 1.12fr 1.05fr;
    gap: 8px;
    flex: 1;
  }'''

a4_p2_grid_new = '''  .p2-grid-row2 {
    display: grid;
    grid-template-columns: 1.05fr 1.05fr 1.48fr 1.12fr 1.04fr;
    gap: 8px;
    flex: 1;
  }'''

a4_p2_replacements = [
    (a4_p2_day15_old, a4_p2_day15_new),
    (a4_p2_grid_old, a4_p2_grid_new)
]

print("--- Updating A4 Page 2 ---")
update_file('18-day-campaign-calendar-a4-page2.html', a4_p2_replacements)

# ==========================================
# 3. A4 Combined Replacements
# ==========================================

a4_comb_replacements = [
    (a4_p2_day15_old, a4_p2_day15_new),
    (a4_p2_grid_old, a4_p2_grid_new)
]

print("--- Updating A4 Combined ---")
update_file('18-day-campaign-calendar-a4.html', a4_comb_replacements)

