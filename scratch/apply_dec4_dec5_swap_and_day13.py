import os
import json
import re
import shutil

BASE_DIR = r"c:\Users\CODEX\Desktop\18 day calendar of activity\18 day calendar of activity"

# 1. A3 & Standard Master Calendars
a3_files = [
    os.path.join(BASE_DIR, "18-day-campaign-calendar-a3.html"),
    os.path.join(BASE_DIR, "18-day-campaign-calendar.html"),
    os.path.join(BASE_DIR, "Final Copy", "18-day-campaign-calendar-a3.html"),
    os.path.join(BASE_DIR, "Final Copy", "18-day-campaign-calendar.html"),
]

for fpath in a3_files:
    with open(fpath, "r", encoding="utf-8") as f:
        html = f.read()

    old_row2 = "grid-template-columns: 0.92fr 1.08fr 2.05fr 1.20fr 0.90fr 0.65fr;"
    new_row2 = "grid-template-columns: 0.92fr 1.08fr 2.05fr 0.90fr 1.20fr 0.65fr;"
    assert old_row2 in html, f"row-2 CSS not found in {fpath}"
    html = html.replace(old_row2, new_row2, 1)

    m10 = re.search(r'(<!-- DAY 10 -->\s*<article[^>]*>\s*<div class="card-top-bar">.*?</div>)(.*?)(</article>)', html, re.DOTALL)
    m11 = re.search(r'(<!-- DAY 11 -->\s*<article[^>]*>\s*<div class="card-top-bar">.*?</div>)(.*?)(</article>)', html, re.DOTALL)
    assert m10 and m11, f"DAY 10 or DAY 11 block not found in {fpath}"

    new_d10 = m10.group(1) + m11.group(2) + m10.group(3)
    new_d11 = m11.group(1) + m10.group(2) + m11.group(3)

    # Replace in reverse order of positions so offsets stay valid
    assert m10.end() < m11.start()
    html = html[:m11.start()] + new_d11 + html[m11.end():]
    html = html[:m10.start()] + new_d10 + html[m10.end():]

    assert "Deepening Session on GFAsT" in html, f"Deepening not found in {fpath}"
    html = html.replace("Deepening Session on GFAsT", "Leveling Session on GFAsT")

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Updated A3/standard calendar: {os.path.relpath(fpath, BASE_DIR)}")

# 2. A4 Master Calendars
a4_files = [
    os.path.join(BASE_DIR, "18-day-campaign-calendar-a4.html"),
    os.path.join(BASE_DIR, "18-day-campaign-calendar-a4-page2.html"),
]

NEW_A4_D10_D11 = """<!-- DAY 10 (Hybrid: In-Person + Online Advocacy) -->
        <article class="day-card active-day">
          <div class="card-top-bar">
            <span class="day-pill">DAY 10</span>
            <span class="date-text">DEC 4</span>
            <span class="weekday-text">FRI</span>
          </div>
          <div style="padding: 9px 11px; display: flex; flex-direction: column; gap: 8px; flex: 1;">
            <!-- TOP 50%: GAD In-Person Activity -->
            <div style="flex: 1; display: flex; flex-direction: column; justify-content: space-between; gap: 6px;">
              <div class="single-lead-block" style="padding: 6px 10px; gap: 2px;">
                <span class="lead-tag-row" style="font-size: 20px;">
                  <svg viewBox="0 0 16 16" style="width: 18px; height: 18px;"><path d="M8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10zm0-7a3 3 0 1 1 0-6 3 3 0 0 1 0 6z"/></svg>
                  LEAD OFFICE
                </span>
                <span class="single-lead-name" style="font-size: 26px;">GAD Office</span>
              </div>
              <div class="single-act-block" style="padding: 8px 10px; gap: 4px; flex: 1; justify-content: center;">
                <span class="act-tag-badge" style="font-size: 19px; padding: 3px 10px;">MAIN ACTIVITY</span>
                <p class="single-act-desc" style="font-size: 23px; line-height: 1.24;">Campaign Learning and Service Readiness Day</p>
              </div>
              <div class="card-venue-box" style="padding: 5px 10px; font-size: 20px; line-height: 1.2;">
                <svg viewBox="0 0 16 16" style="width: 18px; height: 18px;"><path d="M8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10zm0-7a3 3 0 1 1 0-6 3 3 0 0 1 0 6z"/></svg>
                <span><strong>Venue:</strong> Bamboo Hall, City Hall, Cauayan City, Isabela</span>
              </div>
            </div>

            <!-- BOTTOM 50%: Online Advocacy -->
            <div style="flex: 1; background: radial-gradient(circle at center, #fffaf5 0%, #ffffff 100%); border: 2px solid #fed7aa; border-radius: 10px; padding: 12px 10px; display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; gap: 10px;">
              <div style="width: 56px; height: 56px; border-radius: 50%; background: #ffedd5; border: 3px solid #fdba74; display: flex; align-items: center; justify-content: center; box-shadow: 0 3px 8px rgba(234, 88, 12, 0.12);">
                <svg viewBox="0 0 24 24" style="width: 30px; height: 30px; fill: #ea580c;"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 14.5v-9l6 4.5-6 4.5z"/></svg>
              </div>
              <div class="weekend-badge" style="font-size: 21px; padding: 4px 16px;">ONLINE ADVOCACY</div>
              <div class="weekend-advocacy-text" style="font-size: 23px; line-height: 1.32;">Posting of Advocacy Videos, Safe Spaces Pledges Videos and Advocacy Posters</div>
            </div>
          </div>
        </article>

        <!-- DAY 11 (2 ACTIVITIES) -->
        <article class="day-card active-day">
          <div class="card-top-bar">
            <span class="day-pill">DAY 11</span>
            <span class="date-text">DEC 5</span>
            <span class="weekday-text">SAT</span>
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
              <span><strong>Venue:</strong> Isabela Convention Center, San Fermin, Cauayan City, Isabela</span>
            </div>
          </div>
        </article>"""

for fpath in a4_files:
    with open(fpath, "r", encoding="utf-8") as f:
        html = f.read()

    old_p2r1 = "grid-template-columns: 1.30fr 1.10fr 0.75fr 1.65fr;"
    new_p2r1 = "grid-template-columns: 1.10fr 1.30fr 0.75fr 1.65fr;"
    assert old_p2r1 in html, f"p2-grid-row1 CSS not found in {fpath}"
    html = html.replace(old_p2r1, new_p2r1, 1)

    m_block = re.search(r'<!-- DAY 10 \(2 ACTIVITIES\) -->.*?</article>\s*<!-- DAY 11 -->.*?</article>', html, re.DOTALL)
    assert m_block, f"DAY 10..11 block not found in {fpath}"
    html = html[:m_block.start()] + NEW_A4_D10_D11 + html[m_block.end():]

    assert "Deepening Session on GFAsT" in html, f"Deepening not found in {fpath}"
    html = html.replace("Deepening Session on GFAsT", "Leveling Session on GFAsT")

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Updated A4 calendar: {os.path.relpath(fpath, BASE_DIR)}")

# 3. FABMAT HTMLs (scratch/final_html and scratch/final_html_sdd)
for html_dir_rel in [os.path.join("scratch", "final_html"), os.path.join("scratch", "final_html_sdd")]:
    dpath = os.path.join(BASE_DIR, html_dir_rel)
    p10 = os.path.join(dpath, "10-day-10.html")
    p11 = os.path.join(dpath, "11-day-11.html")
    p13 = os.path.join(dpath, "13-day-13.html")

    with open(p10, "r", encoding="utf-8") as f:
        old10 = f.read()
    with open(p11, "r", encoding="utf-8") as f:
        old11 = f.read()

    assert '<div class="stroke-day">DAY 11</div>' in old11 and '<div class="stroke-date">DECEMBER 5, 2026 | SATURDAY</div>' in old11
    new10 = old11.replace('<div class="stroke-day">DAY 11</div>', '<div class="stroke-day">DAY 10</div>', 1)
    new10 = new10.replace('<div class="stroke-date">DECEMBER 5, 2026 | SATURDAY</div>', '<div class="stroke-date">DECEMBER 4, 2026 | FRIDAY</div>', 1)

    assert '<div class="stroke-day">DAY 10</div>' in old10 and '<div class="stroke-date">DECEMBER 4, 2026 | FRIDAY</div>' in old10
    new11 = old10.replace('.stroke-date { font-size: 68px; }', '.stroke-date { font-size: 66px; }', 1)
    new11 = new11.replace('<div class="stroke-day">DAY 10</div>', '<div class="stroke-day">DAY 11</div>', 1)
    new11 = new11.replace('<div class="stroke-date">DECEMBER 4, 2026 | FRIDAY</div>', '<div class="stroke-date">DECEMBER 5, 2026 | SATURDAY</div>', 1)

    with open(p10, "w", encoding="utf-8") as f:
        f.write(new10)
    with open(p11, "w", encoding="utf-8") as f:
        f.write(new11)

    with open(p13, "r", encoding="utf-8") as f:
        h13 = f.read()
    assert "Deepening Session on GFAsT" in h13
    h13 = h13.replace("Deepening Session on GFAsT", "Leveling Session on GFAsT")
    with open(p13, "w", encoding="utf-8") as f:
        f.write(h13)

    print(f"Updated 10, 11, 13 HTMLs in {html_dir_rel}")

# 4. scratch/schedule_data.json
sched_path = os.path.join(BASE_DIR, "scratch", "schedule_data.json")
with open(sched_path, "r", encoding="utf-8") as f:
    sched = json.load(f)

d10_idx = next(i for i, d in enumerate(sched) if d.get("id") == "10")
d11_idx = next(i for i, d in enumerate(sched) if d.get("id") == "11")
d13_idx = next(i for i, d in enumerate(sched) if d.get("id") == "13")

keep_keys = ["id", "day_number", "filename", "badge", "date_str"]
old_d10 = sched[d10_idx]
old_d11 = sched[d11_idx]

new_d10 = {k: old_d10[k] for k in keep_keys}
for k, v in old_d11.items():
    if k not in keep_keys:
        new_d10[k] = v

new_d11 = {k: old_d11[k] for k in keep_keys}
for k, v in old_d10.items():
    if k not in keep_keys:
        new_d11[k] = v

sched[d10_idx] = new_d10
sched[d11_idx] = new_d11

for act in sched[d13_idx].get("activities", []):
    if "Deepening Session on GFAsT" in act.get("description", ""):
        act["description"] = act["description"].replace("Deepening Session on GFAsT", "Leveling Session on GFAsT")

with open(sched_path, "w", encoding="utf-8") as f:
    json.dump(sched, f, indent=2, ensure_ascii=False)
print("Updated scratch/schedule_data.json")

# 5. Extracted Text Files
txt_main = os.path.join(BASE_DIR, "18-Day_Campaign_Calendar_Extracted_Text.txt")
txt_final = os.path.join(BASE_DIR, "Final Copy", "18-Day_Campaign_Calendar_Extracted_Text.txt")

with open(txt_main, "r", encoding="utf-8") as f:
    txt = f.read().replace("\r\n", "\n")

m_txt10 = re.search(r'(DAY 10 \| DEC 4, 2026 \| FRI\n-+\n)(.*?)(\n-+\nDAY 11 \| DEC 5, 2026 \| SAT)', txt, re.DOTALL)
m_txt11 = re.search(r'(DAY 11 \| DEC 5, 2026 \| SAT\n-+\n)(.*?)(\n-+\nDAY 12 \| DEC 6, 2026 \| SUN)', txt, re.DOTALL)
assert m_txt10 and m_txt11, "DAY 10 or DAY 11 section not found in Extracted_Text.txt"

new_t10 = m_txt10.group(1) + m_txt11.group(2)
new_t11 = m_txt11.group(1) + m_txt10.group(2)

txt = txt[:m_txt11.start()] + new_t11 + m_txt11.group(3) + txt[m_txt11.end():]
txt = txt[:m_txt10.start()] + new_t10 + m_txt10.group(3) + txt[m_txt10.end():]

assert "Deepening Session on GFAsT" in txt
txt = txt.replace("Deepening Session on GFAsT", "Leveling Session on GFAsT")

with open(txt_main, "w", encoding="utf-8") as f:
    f.write(txt)
shutil.copy2(txt_main, txt_final)
print("Updated 18-Day_Campaign_Calendar_Extracted_Text.txt and Final Copy/")
