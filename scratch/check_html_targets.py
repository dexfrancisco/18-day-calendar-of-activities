import os

targets = [
    ("Day 2 A1", "Women's economic empowerment, safe employment, anti-trafficking and cyber recruitment scam awareness."),
    ("Day 2 A2", "Rural women protection, livelihood, cooperative support, and community-based prevention."),
    ("Day 3 A1", "Protection of women with disabilities &amp; senior women; inclusive referral and access to support, and Sign Language Orientation."),
    ("Day 3 A3", "Survivor-centered care management, psychosocial first aid, women and children referral mapping."),
    ("Day 4 Act", "Multi-stakeholder dialogues, citizen participation, social accountability, survivor advocacy, and community partnership building."),
    ("Day 8 A1", "Safe workplace, anti-sexual harassment, internal reporting and protection mechanisms."),
    ("Day 9 A1", "Men as allies forum, healthy masculinity, shared responsibility, and prevention of VAWC & online abuse."),
    ("Day 9 A2", "Emergency response simulation, hotline awareness, safety drill, and rapid coordination."),
    ("Day 13 A1", "Seminar on Gender Functionality Assessment Tool (GFAST) and Gender Responsiveness LGU (GERL) Assessment Tool."),
    ("Day 15 A1", "Awarding of all barangays &amp; offices, recognition of partners, presentation of commitments, and ceremonial signing of Memorandum of Partnership with NAPC and OPAPRU.")
]

files = [
    "18-day-campaign-calendar-a3.html",
    "18-day-campaign-calendar.html",
    "18-day-campaign-calendar-a4.html",
    "18-day-campaign-calendar-a4-page1.html",
    "18-day-campaign-calendar-a4-page2.html",
    "Final Copy/18-day-campaign-calendar-a3.html",
    "Final Copy/18-day-campaign-calendar.html"
]

for fn in files:
    if not os.path.exists(fn):
        continue
    with open(fn, "r", encoding="utf-8") as f:
        content = f.read()
    print(f"\nChecking {fn}:")
    for name, t in targets:
        # Also check without &amp;
        t_raw = t.replace("&amp;", "&")
        found = (t in content) or (t_raw in content)
        print(f"  {name:<12}: {found}")

