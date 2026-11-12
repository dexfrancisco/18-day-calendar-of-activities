import os
import re

BASE_DIR = r"c:\Users\CODEX\Desktop\18 day calendar of activity\18 day calendar of activity"

# === 1. Update 11-day-11.html ===
h11_path = os.path.join(BASE_DIR, "scratch", "final_html", "11-day-11.html")
with open(h11_path, "r", encoding="utf-8") as f:
    h11 = f.read()

# Replace the inner body of safe-zone
new_content_11 = """            <div class="hybrid-container">
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

                <div style="width: 100%; height: 3px; background: rgba(255, 109, 0, 0.4); margin: 4px 0;"></div>

                <div class="track-block">
                    <div class="stroke-tag track-tag">ONLINE ADVOCACY</div>
                    <div class="stroke-act-desc" style="font-size:66px; line-height:1.2;">Posting of Advocacy Videos, Safe Spaces Pledges Videos and Advocacy Posters</div>
                </div>
            </div>"""

# Remove old hybrid-container + bottom-block
pattern_11 = re.compile(r'<div class="hybrid-container">.*?</div>\s*</div>\s*</body>', re.DOTALL)
# Wait, let's look at exact closing tags of 11-day-11.html
print("h11 has hybrid-container:", '<div class="hybrid-container">' in h11)

