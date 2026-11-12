import os
import json

BASE_DIR = r"c:\Users\CODEX\Desktop\18 day calendar of activity\18 day calendar of activity"

# 1. Update schedule_data.json
schedule_path = os.path.join(BASE_DIR, "scratch", "schedule_data.json")
with open(schedule_path, "r", encoding="utf-8") as f:
    schedule_data = json.load(f)

for day in schedule_data:
    if day.get("filename") == "02-day-02.png":
        day["activities"] = [
            {
                "num": 1,
                "lead_office": "PESO / COOP / CEDIPO",
                "description": "Economic Empowerment for Women Safe Employment and Anti Trafficking Forum",
                "venue": "F. L. Dy Colliseum, District III, Cauayan City, Isabela"
            },
            {
                "num": 2,
                "lead_office": "City Accounting Office",
                "description": "GAD Employee Development, Recognition and Organizational Strengthening Program.",
                "date_range": "NOV 26–30, 2026",
                "venue": "F. L. Dy Colliseum, District III, Cauayan City, Isabela"
            },
            {
                "num": 3,
                "lead_office": "City Agriculture & Cooperative Office",
                "description": "Rural Women Protection, Livelihood and Cooperative Support Forum",
                "venue": "DA Tagaran, Cauayan City, Isabela",
                "partners": "DA, Cooperatives, MSMES, Barangays"
            }
        ]
        day["partners"] = "DOLE, DTI, OWWA, COA, Cooperatives, MSMES, Barangays, CSOs, Private Sector | DA, Cooperatives, MSMES, Barangays"
        day["venue"] = "F. L. Dy Colliseum, District III, Cauayan City, Isabela | DA Tagaran, Cauayan City, Isabela"

with open(schedule_path, "w", encoding="utf-8") as f:
    json.dump(schedule_data, f, indent=2, ensure_ascii=False)
print("Updated scratch/schedule_data.json")

# 2. Update scratch/final_html/02-day-02.html
html_02_path = os.path.join(BASE_DIR, "scratch", "final_html", "02-day-02.html")
html_02_content = """<!DOCTYPE html><html><head><meta charset="utf-8"><style>
@font-face {
    font-family: 'Gotham Black';
    src: url('/Gotham-font-family/Gotham/Gotham-Black.otf') format('opentype');
    font-weight: 900;
}
@font-face {
    font-family: 'Gotham Ultra';
    src: url('/Gotham-font-family/Gotham/Gotham-Ultra.otf') format('opentype');
    font-weight: 900;
}
@font-face {
    font-family: 'Gotham Bold';
    src: url('/Gotham-font-family/Gotham/Gotham-Bold.otf') format('opentype');
    font-weight: 700;
}
@font-face {
    font-family: 'Gotham Medium';
    src: url('/Gotham-font-family/Gotham/Gotham-Medium.otf') format('opentype');
    font-weight: 500;
}
@font-face {
    font-family: 'Gotham Book';
    src: url('/Gotham-font-family/Gotham/Gotham-Book.otf') format('opentype');
    font-weight: 400;
}
@font-face {
    font-family: 'Gotham Medium Italic';
    src: url('/Gotham-font-family/Gotham/Gotham-MediumItalic.otf') format('opentype');
    font-style: italic;
    font-weight: 500;
}

* { margin: 0; padding: 0; box-sizing: border-box; }

body {
    width: 2480px;
    height: 3508px;
    margin: 0;
    padding: 0;
    overflow: hidden;
    background: url('/FABMAT/fabmat_template.png') no-repeat top left;
    background-size: 2480px 3508px;
    font-family: 'Gotham Bold', sans-serif;
    -webkit-font-smoothing: antialiased;
}

.stroke-day {
    color: #FFFFFF;
    font-family: 'Gotham Ultra', sans-serif;
    letter-spacing: 3px;
    line-height: 1.05;
    paint-order: stroke fill;
    -webkit-text-stroke: 18px #FF6D00;
    font-size: 146px;
}

.stroke-date {
    color: #FFFFFF;
    font-family: 'Gotham Bold', sans-serif;
    letter-spacing: 2px;
    line-height: 1.15;
    paint-order: stroke fill;
    -webkit-text-stroke: 12px #FF6D00;
    font-size: 66px;
}

.stroke-tag {
    color: #FFFFFF;
    font-family: 'Gotham Ultra', sans-serif;
    letter-spacing: 2px;
    line-height: 1.2;
    text-transform: uppercase;
    paint-order: stroke fill;
    -webkit-text-stroke: 10px #FF6D00;
}

.stroke-num {
    color: #FFFFFF;
    font-family: 'Gotham Ultra', sans-serif;
    line-height: 1.1;
    paint-order: stroke fill;
    -webkit-text-stroke: 14px #FF6D00;
    font-size: 62px;
    flex-shrink: 0;
    width: 68px;
}

.stroke-act-desc {
    color: #FFFFFF;
    font-family: 'Gotham Bold', sans-serif;
    paint-order: stroke fill;
    -webkit-text-stroke: 12px #FF6D00;
    font-size: 56px;
    line-height: 1.16;
    flex: 1;
}

.stroke-label {
    color: #FFFFFF;
    font-family: 'Gotham Ultra', sans-serif;
    letter-spacing: 2px;
    line-height: 1.25;
    text-transform: uppercase;
    paint-order: stroke fill;
    -webkit-text-stroke: 11px #FF6D00;
}

.stroke-val {
    color: #FFFFFF;
    font-family: 'Gotham Bold', sans-serif;
    line-height: 1.25;
    paint-order: stroke fill;
    -webkit-text-stroke: 11px #FF6D00;
}

.detail-row {
    display: flex;
    align-items: baseline;
    gap: 18px;
}

.safe-zone {
    position: absolute;
    top: 1290px;
    left: 190px;
    width: 2100px;
    display: flex;
    flex-direction: column;
    gap: 20px;
}

.hero-icon {
    width: 580px;
    height: 580px;
    object-fit: contain;
    flex-shrink: 0;
}

.top-row {
    display: flex;
    align-items: center;
    gap: 40px;
    width: 100%;
}

.day-date-group {
    display: flex;
    flex-direction: column;
    gap: 10px;
}

.venue-section {
    display: flex;
    flex-direction: column;
    gap: 14px;
    width: 100%;
}

.acts-block {
    display: flex;
    flex-direction: column;
    gap: 14px;
    width: 100%;
}

.act-item {
    display: flex;
    flex-direction: column;
    gap: 4px;
}

.act-header-row {
    display: flex;
    align-items: baseline;
    gap: 16px;
}

.act-lead-row {
    display: flex;
    align-items: baseline;
    gap: 16px;
    margin-left: 84px;
}

.act-lead-lbl {
    font-size: 42px;
    flex-shrink: 0;
}

.act-lead-val {
    font-size: 46px;
    flex: 1;
}

.bottom-block {
    display: flex;
    flex-direction: column;
    gap: 10px;
    width: 100%;
}

.detail-label-col {
    width: 380px;
    flex-shrink: 0;
    font-size: 46px;
}

.detail-val-col {
    flex: 1;
    font-size: 46px;
    line-height: 1.2;
}

.section-divider {
    width: 100%;
    height: 3px;
    background: rgba(255, 109, 0, 0.4);
    margin: 4px 0;
}
</style></head><body>
<div class="safe-zone">
    <div class="top-row">
        <img class="hero-icon" src="/icons/DAY 2.png">
        <div class="day-date-group">
            <div class="stroke-day">DAY 2</div>
            <div class="stroke-date">NOVEMBER 26, 2026 | THURSDAY</div>
        </div>
    </div>

    <!-- VENUE 1 SECTION (F. L. Dy Coliseum) -->
    <div class="venue-section">
        <div class="acts-block">
            <div class="act-item">
                <div class="act-header-row">
                    <div class="stroke-num act-num">1.</div>
                    <div class="stroke-act-desc act-desc">Economic Empowerment for Women Safe Employment and Anti Trafficking Forum</div>
                </div>
                <div class="act-lead-row">
                    <span class="stroke-label act-lead-lbl">LEAD OFFICE:</span>
                    <span class="stroke-val act-lead-val">PESO / COOP / CEDIPO</span>
                </div>
            </div>
            <div class="act-item">
                <div class="act-header-row">
                    <div class="stroke-num act-num">2.</div>
                    <div class="stroke-act-desc act-desc">GAD Employee Development, Recognition and Organizational Strengthening Program. <span class="stroke-tag" style="font-size:36px; margin-left:12px;">(NOV 26–30, 2026)</span></div>
                </div>
                <div class="act-lead-row">
                    <span class="stroke-label act-lead-lbl">LEAD OFFICE:</span>
                    <span class="stroke-val act-lead-val">City Accounting Office</span>
                </div>
            </div>
        </div>
        <div class="bottom-block">
            <div class="detail-row">
                <div class="detail-label-col stroke-label">PARTNERS:</div>
                <div class="detail-val-col stroke-val">DOLE, DTI, OWWA, COA, Cooperatives, MSMES, Barangays, CSOs, Private Sector</div>
            </div>
            <div class="detail-row">
                <div class="detail-label-col stroke-label">VENUE:</div>
                <div class="detail-val-col stroke-val">F. L. Dy Colliseum, District III, Cauayan City, Isabela</div>
            </div>
        </div>
    </div>

    <div class="section-divider"></div>

    <!-- VENUE 2 SECTION (DA Tagaran) -->
    <div class="venue-section">
        <div class="acts-block">
            <div class="act-item">
                <div class="act-header-row">
                    <div class="stroke-num act-num">3.</div>
                    <div class="stroke-act-desc act-desc">Rural Women Protection, Livelihood and Cooperative Support Forum</div>
                </div>
                <div class="act-lead-row">
                    <span class="stroke-label act-lead-lbl">LEAD OFFICE:</span>
                    <span class="stroke-val act-lead-val">City Agriculture & Cooperative Office</span>
                </div>
            </div>
        </div>
        <div class="bottom-block">
            <div class="detail-row">
                <div class="detail-label-col stroke-label">PARTNERS:</div>
                <div class="detail-val-col stroke-val">DA, Cooperatives, MSMES, Barangays</div>
            </div>
            <div class="detail-row">
                <div class="detail-label-col stroke-label">VENUE:</div>
                <div class="detail-val-col stroke-val">DA Tagaran, Cauayan City, Isabela</div>
            </div>
        </div>
    </div>
</div>
</body></html>
"""
with open(html_02_path, "w", encoding="utf-8") as f:
    f.write(html_02_content)
print("Updated scratch/final_html/02-day-02.html with Activity 1, 2 (F. L. Dy) and Activity 3 (DA Tagaran)")

# 3. Update Calendar HTML files
a3_card = """        <!-- DAY 2 (Venue 1: Activity 1 & 2 at F. L. Dy; Venue 2: Activity 3 at DA Tagaran) -->
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
            <!-- Sub 2 (Nov 26–30, 2026) -->
            <div class="sub-act-item-d2">
              <div style="display: flex; align-items: center; justify-content: space-between;">
                <div class="sub-act-header">ACTIVITY 2</div>
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
            <!-- Sub 3 (DA Tagaran) -->
            <div class="sub-act-item-d2">
              <div class="sub-act-header">ACTIVITY 3</div>
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

a4_card = """        <!-- DAY 2 (Venue 1: Activity 1 & 2 at F. L. Dy; Venue 2: Activity 3 at DA Tagaran) -->
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
            <!-- Sub 2 (Nov 26–30, 2026) -->
            <div class="sub-act-item-d2">
              <div style="display: flex; align-items: center; justify-content: space-between;">
                <div class="sub-act-header">ACTIVITY 2</div>
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
            <!-- Sub 3 (DA Tagaran) -->
            <div class="sub-act-item-d2">
              <div class="sub-act-header">ACTIVITY 3</div>
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

print("All Day 2 updates applied successfully.")

