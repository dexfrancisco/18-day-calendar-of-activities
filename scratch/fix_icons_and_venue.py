import json
import os

BASE_DIR = r"c:\Users\CODEX\Desktop\18 day calendar of activity\18 day calendar of activity"
json_path = os.path.join(BASE_DIR, "scratch", "schedule_data.json")

with open(json_path, "r", encoding="utf-8") as f:
    data = json.load(f)

# Day 9 is index 9, Day 10 is index 10
# Day 9 (End VAWC Action Forum) should have DAY 10.png (Justice / Health / Digital)
# and venue strictly "ICON"
data[9]["icon_filename"] = "DAY 10.png"
data[9]["venue"] = "ICON"

# Day 10 (MOVE & Safeline 922) should have DAY 9.png (Emergency phone & siren)
# and venue "F. L. Dy Colliseum, District III, Cauayan City, Isabela"
data[10]["icon_filename"] = "DAY 9.png"
data[10]["venue"] = "F. L. Dy Colliseum, District III, Cauayan City, Isabela"

with open(json_path, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("✓ Updated schedule_data.json with matched icons and venue 'ICON'!")

