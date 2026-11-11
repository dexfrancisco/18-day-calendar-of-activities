import os

BASE_DIR = r"c:\Users\CODEX\Desktop\18 day calendar of activity\18 day calendar of activity"
h0 = os.path.join(BASE_DIR, "scratch", "final_html", "00-pre-campaign.html")
if os.path.exists(h0):
    with open(h0, "r", encoding="utf-8") as f:
        print("=== 00-pre-campaign.html ===")
        print(f.read())

h1 = os.path.join(BASE_DIR, "scratch", "final_html", "01-day-01.html")
if os.path.exists(h1):
    with open(h1, "r", encoding="utf-8") as f:
        print("\n=== 01-day-01.html ===")
        print(f.read())

