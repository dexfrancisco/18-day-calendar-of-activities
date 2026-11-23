import os

BASE_DIR = r"c:\Users\CODEX\Desktop\18 day calendar of activity\18 day calendar of activity"

OLD_VAL = "PESO / COOP / CEDIPO"
NEW_VAL = "PESO / CSWDO"

target_files = [
    os.path.join(BASE_DIR, "scratch", "final_html", "02-day-02.html"),
    os.path.join(BASE_DIR, "scratch", "schedule_data.json"),
    os.path.join(BASE_DIR, "18-day-campaign-calendar-a3.html"),
    os.path.join(BASE_DIR, "18-day-campaign-calendar.html"),
    os.path.join(BASE_DIR, "Final Copy", "18-day-campaign-calendar-a3.html"),
    os.path.join(BASE_DIR, "Final Copy", "18-day-campaign-calendar.html"),
    os.path.join(BASE_DIR, "18-day-campaign-calendar-a4.html"),
    os.path.join(BASE_DIR, "18-day-campaign-calendar-a4-page1.html"),
    os.path.join(BASE_DIR, "18-Day_Campaign_Calendar_Extracted_Text.txt"),
    os.path.join(BASE_DIR, "Final Copy", "18-Day_Campaign_Calendar_Extracted_Text.txt"),
]

for fpath in target_files:
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    assert OLD_VAL in content, f"Missing '{OLD_VAL}' in {fpath}"
    updated = content.replace(OLD_VAL, NEW_VAL)
    assert OLD_VAL not in updated, f"Remaining '{OLD_VAL}' in {fpath}"
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(updated)
    print(f"Updated {os.path.relpath(fpath, BASE_DIR)}")

print("All Day 2 Activity 1 lead office updates verified.")
