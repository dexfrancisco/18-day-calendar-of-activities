import os

BASE_DIR = r"c:\Users\CODEX\Desktop\18 day calendar of activity\18 day calendar of activity"

a3_card = """        <!-- DAY 2 (3 Activities: Activity 1, 2, and 3) -->
        <article class="day-card active-day">
          <div class="card-top-bar">
            <span class="day-pill">DAY 2</span>
            <span class="date-text">NOV 26</span>
            <span class="weekday-text">THU</span>
          </div>
          <div class="card-body-3act">
            <!-- Sub 1 -->
            <div class="sub-act-item-3">
              <div class="sub-act-header">ACTIVITY 1</div>
              <div class="sub-lead-name">📍 PESO / COOP / CEDIPO</div>
              <div class="sub-act-desc">Economic Empowerment for Women Safe Employment and Anti Trafficking Forum</div>
            </div>
            <!-- Sub 2 -->
            <div class="sub-act-item-3">
              <div style="display: flex; align-items: center; justify-content: space-between;">
                <div class="sub-act-header">ACTIVITY 2</div>
                <span style="background: #dcfce7; color: #166534; font-family: 'Montserrat', sans-serif; font-size: 21px; font-weight: 800; padding: 2px 7px; border-radius: 4px; letter-spacing: 0.3px;">DA TAGARAN</span>
              </div>
              <div class="sub-lead-name">📍 City Agriculture & Cooperative Office</div>
              <div class="sub-act-desc">Rural Women Protection, Livelihood and Cooperative Support Forum</div>
            </div>
            <!-- Sub 3 (Nov 26–30, 2026) -->
            <div class="sub-act-item-3">
              <div style="display: flex; align-items: center; justify-content: space-between;">
                <div class="sub-act-header">ACTIVITY 3</div>
                <span class="act3-date-pill">NOV 26–30, 2026</span>
              </div>
              <div class="sub-lead-name">📍 City Accounting Office</div>
              <div class="sub-act-desc">GAD Employee Development, Recognition and Organizational Strengthening Program.</div>
            </div>
            <div class="card-partner-box">
              <strong>Partners:</strong> DA, DOLE, DTI, OWWA, COA, Cooperatives, MSMES, Barangays, CSOs, Private Sector
            </div>
            <div class="card-venue-box">
              <svg viewBox="0 0 16 16"><path d="M8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10zm0-7a3 3 0 1 1 0-6 3 3 0 0 1 0 6z"/></svg>
              <span><strong>Venue:</strong> F. L. Dy Colliseum (Act 1 & 3) | DA Tagaran (Act 2)</span>
            </div>
          </div>
        </article>"""

a4_card = """        <!-- DAY 2 (3 Activities: Activity 1, 2, and 3) -->
        <article class="day-card active-day">
          <div class="card-top-bar">
            <span class="day-pill">DAY 2</span>
            <span class="date-text">NOV 26</span>
            <span class="weekday-text">THU</span>
          </div>
          <div class="card-body-3act">
            <!-- Sub 1 -->
            <div class="sub-act-item-3">
              <div class="sub-act-header">ACTIVITY 1</div>
              <div class="sub-lead-name">📍 PESO / COOP / CEDIPO</div>
              <div class="sub-act-desc">Economic Empowerment for Women Safe Employment and Anti Trafficking Forum</div>
            </div>
            <!-- Sub 2 -->
            <div class="sub-act-item-3">
              <div style="display: flex; align-items: center; justify-content: space-between;">
                <div class="sub-act-header">ACTIVITY 2</div>
                <span style="background: #dcfce7; color: #166534; font-family: 'Montserrat', sans-serif; font-size: 18px; font-weight: 800; padding: 1.5px 6px; border-radius: 4px; letter-spacing: 0.3px;">DA TAGARAN</span>
              </div>
              <div class="sub-lead-name">📍 City Agriculture & Cooperative Office</div>
              <div class="sub-act-desc">Rural Women Protection, Livelihood and Cooperative Support Forum</div>
            </div>
            <!-- Sub 3 (Nov 26–30, 2026) -->
            <div class="sub-act-item-3">
              <div style="display: flex; align-items: center; justify-content: space-between;">
                <div class="sub-act-header">ACTIVITY 3</div>
                <span class="act3-date-pill">NOV 26–30, 2026</span>
              </div>
              <div class="sub-lead-name">📍 City Accounting Office</div>
              <div class="sub-act-desc">GAD Employee Development, Recognition and Organizational Strengthening Program.</div>
            </div>
            <div class="card-partner-box">
              <strong>Partners:</strong> DA, DOLE, DTI, OWWA, COA, Cooperatives, MSMES, Barangays, CSOs, Private Sector
            </div>
            <div class="card-venue-box">
              <svg viewBox="0 0 16 16"><path d="M8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10zm0-7a3 3 0 1 1 0-6 3 3 0 0 1 0 6z"/></svg>
              <span><strong>Venue:</strong> F. L. Dy Colliseum (Act 1 & 3) | DA Tagaran (Act 2)</span>
            </div>
          </div>
        </article>"""

# Apply to A3 calendars
for p in ['18-day-campaign-calendar-a3.html', '18-day-campaign-calendar.html', 'Final Copy/18-day-campaign-calendar-a3.html', 'Final Copy/18-day-campaign-calendar.html']:
    fp = os.path.join(BASE_DIR, p)
    if os.path.exists(fp):
        with open(fp, 'r', encoding='utf-8') as f:
            c = f.read()
        s = c.find('<!-- DAY 2')
        e = c.find('<!-- DAY 3')
        if s != -1 and e != -1:
            c = c[:s] + a3_card + '\n\n        ' + c[e:]
            with open(fp, 'w', encoding='utf-8') as f:
                f.write(c)
            print(f'Updated Day 2 in {p}')

# Apply to A4 calendars
for p in ['18-day-campaign-calendar-a4.html', '18-day-campaign-calendar-a4-page1.html']:
    fp = os.path.join(BASE_DIR, p)
    if os.path.exists(fp):
        with open(fp, 'r', encoding='utf-8') as f:
            c = f.read()
        s = c.find('<!-- DAY 2')
        e = c.find('<!-- DAY 3')
        if s != -1 and e != -1:
            c = c[:s] + a4_card + '\n\n        ' + c[e:]
            with open(fp, 'w', encoding='utf-8') as f:
                f.write(c)
            print(f'Updated Day 2 in {p}')

print('\nAll calendar Day 2 cards updated successfully!')

