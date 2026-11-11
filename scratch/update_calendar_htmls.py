import os
import re

BASE_DIR = r"c:\Users\CODEX\Desktop\18 day calendar of activity\18 day calendar of activity"

# 1. Update A3 files
a3_files = [
    os.path.join(BASE_DIR, "18-day-campaign-calendar-a3.html"),
    os.path.join(BASE_DIR, "18-day-campaign-calendar.html"),
    os.path.join(BASE_DIR, "Final Copy", "18-day-campaign-calendar-a3.html"),
    os.path.join(BASE_DIR, "Final Copy", "18-day-campaign-calendar.html")
]

new_day9_a3 = """        <!-- DAY 9 -->
        <article class="day-card active-day">
          <div class="card-top-bar">
            <span class="day-pill">DAY 9</span>
            <span class="date-text">DEC 3</span>
            <span class="weekday-text">THU</span>
          </div>
          <div class="card-body-5act">
            <!-- Sub 1: City Health -->
            <div class="sub-act-item-5">
              <div class="sub-act-header">ACTIVITY 1</div>
              <div class="sub-lead-name">📍 City Health Office</div>
              <div class="sub-act-desc">Health response, mental health, reproductive health, medico-legal awareness, and support services for survivors.</div>
            </div>
            <!-- Sub 2: City Legal -->
            <div class="sub-act-item-5">
              <div class="sub-act-header">ACTIVITY 2</div>
              <div class="sub-lead-name">📍 City Legal Office</div>
              <div class="sub-act-desc">Orientation on RA 9262, Safe Spaces Act, Anti-Trafficking, cyber-related VAWC and online crimes; legal referral pathways.</div>
            </div>
            <!-- Sub 3: PNP -->
            <div class="sub-act-item-5">
              <div class="sub-act-header">ACTIVITY 3</div>
              <div class="sub-lead-name">📍 PNP-WCPD / LCAT-VAWC / BJMP / Justice Sector</div>
              <div class="sub-act-desc">Case documentation, law enforcement coordination, protection procedures, and anti-online exploitation response.</div>
            </div>
            <!-- Sub 4: Liga -->
            <div class="sub-act-item-5">
              <div class="sub-act-header">ACTIVITY 4</div>
              <div class="sub-lead-name">📍 Liga ng mga Barangay / VAW Desks</div>
              <div class="sub-act-desc">Barangay action planning, desk strengthening, community watch, and referral readiness.</div>
            </div>
            <!-- Sub 5: JCD GAD CONNECT and CDRRMO -->
            <div class="sub-act-item-5">
              <div class="sub-act-header">ACTIVITY 5</div>
              <div class="sub-lead-name">📍 JCD GAD CONNECT and CDRRMO</div>
              <div class="sub-act-desc">Digital Safety Day: demo of Project S.U.N.S.H.I.N.E., iReport VAWC, Safe Line, online reporting, cyber safety & digital evidence awareness.</div>
            </div>
            <div class="card-partner-box">
              <strong>Partners:</strong> DILG, PNP, BJMP, City Prosecutor's Office, PAO, Barangays, Barangay Officials, BSWDO, Hospitals, RHUs, NGOs, Mental Health Partners, GAD Office, Tech Partners, JCI
            </div>
            <div class="card-venue-box">
              <svg viewBox="0 0 16 16"><path d="M8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10zm0-7a3 3 0 1 1 0-6 3 3 0 0 1 0 6z"/></svg>
              <span><strong>Venue:</strong> ICON, San Fermin, Cauayan City, Isabela</span>
            </div>
          </div>
        </article>"""

new_day10_a3 = """        <!-- DAY 10 -->
        <article class="day-card active-day">
          <div class="card-top-bar">
            <span class="day-pill">DAY 10</span>
            <span class="date-text">DEC 4</span>
            <span class="weekday-text">FRI</span>
          </div>
          <div class="card-body-multi">
            <!-- Sub 1 -->
            <div class="sub-act-item-2">
              <div class="sub-act-header">ACTIVITY 1</div>
              <div class="sub-lead-name">📍 GAD Office & MOVE</div>
              <div class="sub-act-desc">Men as Allies and Men Opposed to Violence Everywhere (MOVE) Forum on Healthy Masculinity and Shared Responsibility</div>
            </div>
            <!-- Sub 2 -->
            <div class="sub-act-item-2">
              <div class="sub-act-header">ACTIVITY 2</div>
              <div class="sub-lead-name">📍 CDRRMO / Rescue 922 / Safe Line</div>
              <div class="sub-act-desc">Safeline 922 Emergency Response Simulation and Referral Drill</div>
            </div>
            <div class="card-partner-box">
              <strong>Partners:</strong> PNP, BFP, BJMP, CDRRMO, MDRRMO, All Teams, JCI, Faith Groups, Youth Groups, Academe, DepEd, MASON, ROTARY Club of Cauayan
            </div>
            <div class="card-venue-box">
              <svg viewBox="0 0 16 16"><path d="M8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10zm0-7a3 3 0 1 1 0-6 3 3 0 0 1 0 6z"/></svg>
              <span><strong>Venue:</strong> F. L. Dy Colliseum, District III, Cauayan City, Isabela</span>
            </div>
          </div>
        </article>"""

for fp in a3_files:
    if not os.path.exists(fp): continue
    with open(fp, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Replace Day 9 and Day 10 block
    pattern = r'<!-- DAY 9 -->.*?<!-- DAY 11 -->'
    replacement = f"{new_day9_a3}\n\n{new_day10_a3}\n\n        <!-- DAY 11 -->"
    new_content, count = re.subn(pattern, replacement, content, flags=re.DOTALL)
    if count > 0:
        with open(fp, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"✓ Updated Day 9 & 10 in {os.path.basename(fp)}")
    else:
        print(f"✗ Failed pattern match in {os.path.basename(fp)}")

# 2. Update A4 Page 1 (Day 9)
p1_path = os.path.join(BASE_DIR, "18-day-campaign-calendar-a4-page1.html")
with open(p1_path, "r", encoding="utf-8") as f:
    p1 = f.read()

# Add .sub-act-item-5 CSS if missing in p1
if ".sub-act-item-5" not in p1:
    css_5act = """
  /* 5 ACTIVITIES CARD (Day 9 on Page 1) */
  .card-body-5act {
    padding: 6px 9px;
    display: flex;
    flex-direction: column;
    gap: 4px;
    flex: 1;
    justify-content: space-between;
  }

  .sub-act-item-5 {
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    gap: 2px;
    background: #fffcf8;
    border: 1.5px solid #fed7aa;
    border-left: 5px solid #ea580c;
    border-radius: 8px;
    padding: 4px 10px;
  }

  .sub-act-item-5 .sub-act-header {
    padding: 2px 9px;
    font-size: 22px;
  }

  .sub-act-item-5 .sub-lead-name {
    font-size: 24px;
  }

  .sub-act-item-5 .sub-act-desc {
    font-size: 22px;
    line-height: 1.2;
  }
"""
    p1 = p1.replace("</style>", f"{css_5act}\n</style>")

p1_day9_html = """        <!-- DAY 9 (5 ACTIVITIES) -->
        <article class="day-card active-day">
          <div class="card-top-bar">
            <span class="day-pill">DAY 9</span>
            <span class="date-text">DEC 3</span>
            <span class="weekday-text">THU</span>
          </div>
          <div class="card-body-5act">
            <div class="sub-act-item-5">
              <div class="sub-act-header">ACTIVITY 1</div>
              <div class="sub-lead-name">📍 City Health Office</div>
              <div class="sub-act-desc">Health response, mental health, reproductive health, medico-legal awareness, support services.</div>
            </div>
            <div class="sub-act-item-5">
              <div class="sub-act-header">ACTIVITY 2</div>
              <div class="sub-lead-name">📍 City Legal Office</div>
              <div class="sub-act-desc">Orientation on RA 9262, Safe Spaces Act, Anti-Trafficking, cyber-related VAWC and online crimes.</div>
            </div>
            <div class="sub-act-item-5">
              <div class="sub-act-header">ACTIVITY 3</div>
              <div class="sub-lead-name">📍 PNP-WCPD / LCAT-VAWC / BJMP / Justice Sector</div>
              <div class="sub-act-desc">Case documentation, law enforcement coordination, protection procedures, anti-online exploitation.</div>
            </div>
            <div class="sub-act-item-5">
              <div class="sub-act-header">ACTIVITY 4</div>
              <div class="sub-lead-name">📍 Liga ng mga Barangay / VAW Desks</div>
              <div class="sub-act-desc">Barangay action planning, desk strengthening, community watch, and referral readiness.</div>
            </div>
            <div class="sub-act-item-5">
              <div class="sub-act-header">ACTIVITY 5</div>
              <div class="sub-lead-name">📍 JCD GAD CONNECT and CDRRMO</div>
              <div class="sub-act-desc">Digital Safety Day: demo of Project S.U.N.S.H.I.N.E., iReport VAWC, Safe Line, cyber safety & digital evidence.</div>
            </div>
            <div class="card-partner-box" style="font-size: 20px; line-height: 1.2; padding: 4px 8px;">
              <strong>Partners:</strong> DILG, PNP, BJMP, Prosecutor, PAO, Barangays, BSWDO, Hospitals, RHUs, NGOs, Mental Health, GAD, Tech, JCI
            </div>
            <div class="card-venue-box" style="font-size: 22px; padding: 4px 8px;">
              <svg viewBox="0 0 16 16"><path d="M8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10zm0-7a3 3 0 1 1 0-6 3 3 0 0 1 0 6z"/></svg>
              <span><strong>Venue:</strong> ICON, San Fermin, Cauayan City, Isabela</span>
            </div>
          </div>
        </article>"""

pattern_p1 = r'<!-- DAY 9.*?-->\s*<article class="day-card active-day">.*?</article>'
p1_new, count_p1 = re.subn(pattern_p1, p1_day9_html, p1, flags=re.DOTALL)
if count_p1 > 0:
    with open(p1_path, "w", encoding="utf-8") as f:
        f.write(p1_new)
    print("✓ Updated Day 9 on A4 Page 1")
else:
    print("✗ Failed to update Day 9 on A4 Page 1")

# 3. Update A4 Page 2 (Day 10)
p2_path = os.path.join(BASE_DIR, "18-day-campaign-calendar-a4-page2.html")
with open(p2_path, "r", encoding="utf-8") as f:
    p2 = f.read()

p2_day10_html = """        <!-- DAY 10 (2 ACTIVITIES) -->
        <article class="day-card active-day">
          <div class="card-top-bar">
            <span class="day-pill">DAY 10</span>
            <span class="date-text">DEC 4</span>
            <span class="weekday-text">FRI</span>
          </div>
          <div class="card-body-multi">
            <div class="sub-act-item-2">
              <div class="sub-act-header">ACTIVITY 1</div>
              <div class="sub-lead-name">📍 GAD Office & MOVE</div>
              <div class="sub-act-desc">Men as Allies and Men Opposed to Violence Everywhere (MOVE) Forum on Healthy Masculinity and Shared Responsibility</div>
            </div>
            <div class="sub-act-item-2">
              <div class="sub-act-header">ACTIVITY 2</div>
              <div class="sub-lead-name">📍 CDRRMO / Rescue 922 / Safe Line</div>
              <div class="sub-act-desc">Safeline 922 Emergency Response Simulation and Referral Drill</div>
            </div>
            <div class="card-partner-box">
              <strong>Partners:</strong> PNP, BFP, BJMP, CDRRMO, MDRRMO, All Teams, JCI, Faith Groups, Youth Groups, Academe, DepEd, MASON, ROTARY
            </div>
            <div class="card-venue-box">
              <svg viewBox="0 0 16 16"><path d="M8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10zm0-7a3 3 0 1 1 0-6 3 3 0 0 1 0 6z"/></svg>
              <span><strong>Venue:</strong> F. L. Dy Colliseum, District III, Cauayan City, Isabela</span>
            </div>
          </div>
        </article>"""

pattern_p2 = r'<!-- DAY 10.*?-->\s*<article class="day-card active-day">.*?</article>'
p2_new, count_p2 = re.subn(pattern_p2, p2_day10_html, p2, flags=re.DOTALL)
if count_p2 > 0:
    with open(p2_path, "w", encoding="utf-8") as f:
        f.write(p2_new)
    print("✓ Updated Day 10 on A4 Page 2")
else:
    print("✗ Failed to update Day 10 on A4 Page 2")

# 4. Update A4 Combined (18-day-campaign-calendar-a4.html)
a4_path = os.path.join(BASE_DIR, "18-day-campaign-calendar-a4.html")
if os.path.exists(a4_path):
    with open(a4_path, "r", encoding="utf-8") as f:
        a4 = f.read()
    # Apply p1 day 9 and p2 day 10
    a4_new, c1 = re.subn(pattern_p1, p1_day9_html, a4, flags=re.DOTALL)
    a4_new, c2 = re.subn(pattern_p2, p2_day10_html, a4_new, flags=re.DOTALL)
    if c1 > 0 or c2 > 0:
        with open(a4_path, "w", encoding="utf-8") as f:
            f.write(a4_new)
        print("✓ Updated Day 9 & 10 in 18-day-campaign-calendar-a4.html")

