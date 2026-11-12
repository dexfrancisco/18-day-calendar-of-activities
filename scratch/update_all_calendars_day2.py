import shutil

# 1. Update 18-day-campaign-calendar.html and Final Copy from 18-day-campaign-calendar-a3.html
shutil.copy2('18-day-campaign-calendar-a3.html', '18-day-campaign-calendar.html')
shutil.copy2('18-day-campaign-calendar-a3.html', 'Final Copy/18-day-campaign-calendar-a3.html')
shutil.copy2('18-day-campaign-calendar-a3.html', 'Final Copy/18-day-campaign-calendar.html')
print("✓ Updated 18-day-campaign-calendar.html and Final Copy A3/default")

# 2. Update A4 Page 1 and A4 2-page
a4_css = """  /* DAY 2 CARD (Activity 1 & 3 at F. L. Dy, Activity 2 below venue at DA Tagaran) */
  .card-body-day2 {
    padding: 4px 6px;
    display: flex;
    flex-direction: column;
    gap: 3px;
    flex: 1;
    justify-content: space-between;
  }

  .sub-act-item-d2 {
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    gap: 2px;
    background: #fffcf8;
    border: 1.5px solid #fed7aa;
    border-left: 5px solid #ea580c;
    border-radius: 7px;
    padding: 3px 8px;
  }

  .sub-act-item-d2 .sub-act-header {
    background: #ffedd5;
    padding: 1.5px 6px;
    border-radius: 4px;
    font-family: 'Montserrat', sans-serif;
    font-size: 19.5px;
    font-weight: 900;
    color: #9a3412;
    text-transform: uppercase;
    letter-spacing: 0.3px;
    align-self: flex-start;
  }

  .sub-act-item-d2 .act3-date-pill {
    background: #ea580c;
    color: #ffffff;
    font-family: 'Montserrat', sans-serif;
    font-size: 18px;
    font-weight: 800;
    padding: 1.5px 6px;
    border-radius: 4px;
    letter-spacing: 0.3px;
  }

  .sub-act-item-d2 .sub-lead-name {
    font-size: 21.5px;
    font-weight: 800;
    color: #0f172a;
    line-height: 1.12;
  }

  .sub-act-item-d2 .sub-act-desc {
    font-size: 19.5px;
    line-height: 1.16;
    color: #334155;
    font-weight: 600;
  }

  .card-body-day2 .card-partner-box {
    padding: 3px 7px;
    font-size: 18.5px;
    line-height: 1.14;
  }

  .card-body-day2 .card-venue-box {
    padding: 3px 7px;
    font-size: 19px;
    gap: 5px;
    line-height: 1.15;
    border-radius: 6px;
  }

  .card-body-day2 .card-venue-box svg {
    width: 17px;
    height: 17px;
  }

  .card-body-day2 .card-venue-box strong {
    font-size: 19px;
  }
"""

day2_markup = """        <!-- DAY 2 (Activity 1 & 3 at F. L. Dy, Activity 2 below venue at DA Tagaran) -->
        <article class="day-card active-day">
          <div class="card-top-bar">
            <span class="day-pill">DAY 2</span>
            <span class="date-text">NOV 26</span>
            <span class="weekday-text">THU</span>
          </div>
          <div class="card-body-day2">
            <!-- Sub 1 -->
            <div class="sub-act-item-d2">
              <div class="sub-act-header">ACTIVITY 1</div>
              <div class="sub-lead-name">📍 PESO / COOP / CEDIPO</div>
              <div class="sub-act-desc">Economic Empowerment for Women Safe Employment and Anti Trafficking Forum</div>
            </div>
            <!-- Sub 3 (Nov 26–30, 2026) -->
            <div class="sub-act-item-d2">
              <div style="display: flex; align-items: center; justify-content: space-between;">
                <div class="sub-act-header">ACTIVITY 3</div>
                <span class="act3-date-pill">NOV 26–30, 2026</span>
              </div>
              <div class="sub-lead-name">📍 City Accounting Office</div>
              <div class="sub-act-desc">GAD Employee Development, Recognition and Organizational Strengthening Program.</div>
            </div>
            <div class="card-partner-box">
              <strong>Partners:</strong> DOLE, DTI, OWWA, COA, Cooperatives, MSMES, Barangays, CSOs, Private Sector
            </div>
            <div class="card-venue-box">
              <svg viewBox="0 0 16 16"><path d="M8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10zm0-7a3 3 0 1 1 0-6 3 3 0 0 1 0 6z"/></svg>
              <span><strong>Venue:</strong> F. L. Dy Colliseum, District III, Cauayan City, Isabela</span>
            </div>
            <!-- Sub 2 (Below Venue with DA Tagaran) -->
            <div class="sub-act-item-d2">
              <div class="sub-act-header">ACTIVITY 2</div>
              <div class="sub-lead-name">📍 City Agriculture &amp; Cooperative Office</div>
              <div class="sub-act-desc">Rural Women Protection, Livelihood and Cooperative Support Forum</div>
            </div>
            <div class="card-partner-box">
              <strong>Partners:</strong> DA, Cooperatives, MSMES, Barangays
            </div>
            <div class="card-venue-box">
              <svg viewBox="0 0 16 16"><path d="M8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10zm0-7a3 3 0 1 1 0-6 3 3 0 0 1 0 6z"/></svg>
              <span><strong>Venue:</strong> DA Tagaran, Cauayan City, Isabela</span>
            </div>
          </div>
        </article>"""

import re

for a4_file in ['18-day-campaign-calendar-a4-page1.html', '18-day-campaign-calendar-a4.html']:
    with open(a4_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace Day 2 CSS (card-body-3act)
    css_target_re = r'/\*\s*DAY 2 CARD \(3 activities\)\s*\*/.*?\.card-body-3act \.card-venue-box strong\s*\{\s*font-size:\s*19px;\s*\}'
    if re.search(css_target_re, content, re.DOTALL):
        content = re.sub(css_target_re, a4_css.strip(), content, flags=re.DOTALL)
        print(f"✓ Replaced CSS in {a4_file}")
    else:
        # Fallback: search before card-partner-box
        idx = content.find('/* SHARED MULTI-ACTIVITY PARTNER BOX')
        if idx != -1:
            content = content[:idx] + a4_css + "\n  " + content[idx:]
            print(f"✓ Inserted CSS in {a4_file}")
    
    # Replace Day 2 markup
    card_re = r'<!--\s*DAY 2.*?</article>'
    if re.search(card_re, content, re.DOTALL):
        content = re.sub(card_re, day2_markup.strip(), content, flags=re.DOTALL, count=1)
        print(f"✓ Replaced Day 2 markup in {a4_file}")
    
    with open(a4_file, 'w', encoding='utf-8') as f:
        f.write(content)

