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
    
    # In Day 9 block, change Venue: ICON to Isabela Convention Center, San Fermin, Cauayan City, Isabela
    c_new = c.replace(
        "<span><strong>Venue:</strong> ICON</span>",
        "<span><strong>Venue:</strong> Isabela Convention Center, San Fermin, Cauayan City, Isabela</span>"
    )
    if c_new != c:
        with open(fp, "w", encoding="utf-8") as f:
            f.write(c_new)
        print(f"✓ Updated venue in {os.path.basename(fp)}")
    else:
        print(f"- Already updated or no match in {os.path.basename(fp)}")

