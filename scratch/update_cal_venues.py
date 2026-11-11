import os

BASE_DIR = r"c:\Users\CODEX\Desktop\18 day calendar of activity\18 day calendar of activity"

cal_files = [
    os.path.join(BASE_DIR, "18-day-campaign-calendar-a3.html"),
    os.path.join(BASE_DIR, "18-day-campaign-calendar.html"),
    os.path.join(BASE_DIR, "Final Copy", "18-day-campaign-calendar-a3.html"),
    os.path.join(BASE_DIR, "Final Copy", "18-day-campaign-calendar.html"),
    os.path.join(BASE_DIR, "18-day-campaign-calendar-a4.html"),
    os.path.join(BASE_DIR, "18-day-campaign-calendar-a4-page1.html")
]

for fp in cal_files:
    if not os.path.exists(fp): continue
    with open(fp, "r", encoding="utf-8") as f:
        c = f.read()
    
    # In Day 9 block:
    # <span><strong>Venue:</strong> ICON, San Fermin, Cauayan City, Isabela</span>
    # to <span><strong>Venue:</strong> ICON</span>
    c_new = c.replace(
        "<span><strong>Venue:</strong> ICON, San Fermin, Cauayan City, Isabela</span>",
        "<span><strong>Venue:</strong> ICON</span>"
    )
    if c_new != c:
        with open(fp, "w", encoding="utf-8") as f:
            f.write(c_new)
        print(f"✓ Updated venue to ICON in {os.path.basename(fp)}")
    else:
        print(f"- No change needed or already updated in {os.path.basename(fp)}")

