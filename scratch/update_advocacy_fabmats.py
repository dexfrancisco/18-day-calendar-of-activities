import os
import re

BASE_DIR = r"c:\Users\CODEX\Desktop\18 day calendar of activity\18 day calendar of activity"

# === 1. Day 11 ===
h11_path = os.path.join(BASE_DIR, "scratch", "final_html", "11-day-11.html")
with open(h11_path, "r", encoding="utf-8") as f:
    h11 = f.read()

# Replace body of safe-zone
body_11 = """            <div class="top-row">
                <img class="hero-icon" src="/icons/DAY 11.png">
                <div class="day-date-group">
                    <div class="stroke-day">DAY 11</div>
                    <div class="stroke-date">DECEMBER 5, 2026 | SATURDAY</div>
                </div>
            </div>
            <div class="hybrid-container">
                <div class="track-block">
                    <div class="stroke-tag track-tag">IN-PERSON ACTIVITY</div>
                    <div class="stroke-act-desc" style="font-size:76px; line-height:1.2;">Campaign Learning and Service Readiness Day</div>
                    <div style="display:flex; align-items:baseline; gap:16px; margin-top:4px;">
                        <span class="stroke-label" style="font-size:50px;">LEAD OFFICE:</span>
                        <span class="stroke-val" style="font-size:54px;">GAD Office</span>
                    </div>
                    <div class="detail-row" style="margin-top:6px;">
                        <div class="detail-label-col stroke-label">VENUE:</div>
                        <div class="detail-val-col stroke-val">Bamboo Hall, City Hall, Cauayan City, Isabela</div>
                    </div>
                </div>

                <div style="width: 100%; height: 3px; background: rgba(255, 109, 0, 0.4); margin: 6px 0;"></div>

                <div class="track-block">
                    <div class="stroke-tag track-tag">ONLINE ADVOCACY</div>
                    <div class="stroke-act-desc" style="font-size:66px; line-height:1.2;">Posting of Advocacy Videos, Safe Spaces Pledges Videos and Advocacy Posters</div>
                </div>
            </div>
        </div>
        </body></html>"""

h11_new = re.sub(r'<div class="top-row">.*</body></html>', body_11, h11, flags=re.DOTALL)
with open(h11_path, "w", encoding="utf-8") as f:
    f.write(h11_new)
print("Updated 11-day-11.html")

# === 2. Day 17 ===
h17_path = os.path.join(BASE_DIR, "scratch", "final_html", "17-day-17.html")
with open(h17_path, "r", encoding="utf-8") as f:
    h17 = f.read()

body_17 = """            <div class="top-row">
                <img class="hero-icon" src="/icons/DAY 17.png">
                <div class="day-date-group">
                    <div class="stroke-day">DAY 17</div>
                    <div class="stroke-date">DECEMBER 11, 2026 | FRIDAY</div>
                </div>
            </div>
            <div class="hybrid-container">
                <div class="track-block">
                    <div class="stroke-tag track-tag">IN-PERSON ACTIVITY</div>
                    <div class="stroke-act-desc" style="font-size:76px; line-height:1.2;">Regional Educational Research Conference</div>
                    <div style="display:flex; align-items:baseline; gap:16px; margin-top:4px;">
                        <span class="stroke-label" style="font-size:50px;">LEAD OFFICE:</span>
                        <span class="stroke-val" style="font-size:54px;">GAD Office</span>
                    </div>
                    <div class="detail-row" style="margin-top:6px;">
                        <div class="detail-label-col stroke-label">PARTNERS:</div>
                        <div class="detail-val-col stroke-val">SDO Cauayan City, DEPED RO2</div>
                    </div>
                    <div class="detail-row">
                        <div class="detail-label-col stroke-label">VENUE:</div>
                        <div class="detail-val-col stroke-val">F. L. Dy Colliseum, District III, Cauayan City, Isabela</div>
                    </div>
                </div>

                <div style="width: 100%; height: 3px; background: rgba(255, 109, 0, 0.4); margin: 6px 0;"></div>

                <div class="track-block">
                    <div class="stroke-tag track-tag">ONLINE ADVOCACY</div>
                    <div class="stroke-act-desc" style="font-size:66px; line-height:1.2;">Posting of Advocacy Videos, Safe Spaces Pledges Videos and Advocacy Posters</div>
                </div>
            </div>
        </div>
        </body></html>"""

h17_new = re.sub(r'<div class="top-row">.*</body></html>', body_17, h17, flags=re.DOTALL)
with open(h17_path, "w", encoding="utf-8") as f:
    f.write(h17_new)
print("Updated 17-day-17.html")

# === 3. Day 18 ===
h18_path = os.path.join(BASE_DIR, "scratch", "final_html", "18-day-18.html")
with open(h18_path, "r", encoding="utf-8") as f:
    h18 = f.read()

body_18 = """            <div class="top-row">
                <img class="hero-icon" src="/icons/DAY 18.png">
                <div class="day-date-group">
                    <div class="stroke-day">DAY 18</div>
                    <div class="stroke-date">DECEMBER 12, 2026 | SATURDAY</div>
                </div>
            </div>
            <div class="hybrid-container">
                <div class="track-block">
                    <div class="stroke-tag track-tag">IN-PERSON ACTIVITY</div>
                    <div style="display:flex; align-items:baseline; gap:16px;">
                        <div class="stroke-num" style="font-size:66px; width:74px; flex-shrink:0;">1.</div>
                        <div class="stroke-act-desc" style="font-size:66px; line-height:1.18;">Display of Orange Exhibits</div>
                    </div>
                    <div style="display:flex; align-items:baseline; gap:16px;">
                        <div class="stroke-num" style="font-size:66px; width:74px; flex-shrink:0;">2.</div>
                        <div class="stroke-act-desc" style="font-size:66px; line-height:1.18;">Posting of Accomplishment Reports for the 18-day Campaign</div>
                    </div>
                    <div style="display:flex; align-items:baseline; gap:16px; margin-top:4px;">
                        <span class="stroke-label" style="font-size:52px;">LEAD OFFICE:</span>
                        <span class="stroke-val" style="font-size:52px;">GAD Office</span>
                    </div>
                    <div class="detail-row" style="margin-top:6px;">
                        <div class="detail-label-col stroke-label">PARTNERS:</div>
                        <div class="detail-val-col stroke-val">GAD Office, City Information Office, Partner Agencies</div>
                    </div>
                    <div class="detail-row">
                        <div class="detail-label-col stroke-label">VENUE:</div>
                        <div class="detail-val-col stroke-val">F. L. Dy Colliseum & Cauayan City Hall Grounds</div>
                    </div>
                </div>

                <div style="width: 100%; height: 3px; background: rgba(255, 109, 0, 0.4); margin: 6px 0;"></div>

                <div class="track-block">
                    <div class="stroke-tag track-tag">ONLINE ADVOCACY</div>
                    <div class="stroke-act-desc" style="font-size:62px; line-height:1.18;">Posting of Advocacy Videos, Safe Spaces Pledges Videos and Advocacy Posters</div>
                </div>
            </div>
        </div>
        </body></html>"""

h18_new = re.sub(r'<div class="top-row">.*</body></html>', body_18, h18, flags=re.DOTALL)
with open(h18_path, "w", encoding="utf-8") as f:
    f.write(h18_new)
print("Updated 18-day-18.html")

