import os
import re

BASE_DIR = r"c:\Users\CODEX\Desktop\18 day calendar of activity\18 day calendar of activity"

# 1. Update A3 and Calendar.html (both in root and Final Copy)
a3_replacements = [
    # Day 2 A1
    ("Women's economic empowerment, safe employment, anti-trafficking and cyber recruitment scam awareness.",
     "Economic Empowerment for Women Safe Employment and Anti Trafficking Forum"),
    # Day 2 A2
    ("Rural women protection, livelihood, cooperative support, and community-based prevention.",
     "Rural Women Protection, Livelihood and Cooperative Support Forum"),
    # Day 3 A1
    ("Protection of women with disabilities &amp; senior women; inclusive referral and access to support, and Sign Language Orientation.",
     "Inclusive Protection, Accessible Services, and Sign Language Orientation for Women with Disabilities and Senior Women"),
    ("Protection of women with disabilities & senior women; inclusive referral and access to support, and Sign Language Orientation.",
     "Inclusive Protection, Accessible Services, and Sign Language Orientation for Women with Disabilities and Senior Women"),
    # Day 3 A3
    ("Survivor-centered care management, psychosocial first aid, women and children referral mapping.",
     "Project SUNSHINE Survivor – Centered Case Management and Referral Review"),
    # Day 4
    ("Multi-stakeholder dialogues, citizen participation, social accountability, survivor advocacy, and community partnership building.",
     "Multi-Stakeholder Dialogue on Accountability to Survivors and Community Partnership"),
    # Day 8 A1
    ("Safe workplace, anti-sexual harassment, internal reporting and protection mechanisms.",
     "Safe Workplace Compliance and Anti-Sexual Harassment Orientation"),
    # Day 9 A1
    ("Men as allies forum, healthy masculinity, shared responsibility, and prevention of VAWC & online abuse.",
     "Men as Allies and Men Opposed to Violence Everywhere (MOVE) Forum on Healthy Masculinity and Shared Responsibility"),
    ("Men as allies forum, healthy masculinity, shared responsibility, and prevention of VAWC &amp; online abuse.",
     "Men as Allies and Men Opposed to Violence Everywhere (MOVE) Forum on Healthy Masculinity and Shared Responsibility"),
    # Day 9 A2
    ("Emergency response simulation, hotline awareness, safety drill, and rapid coordination.",
     "Safeline 922 Emergency Response Simulation and Referral Drill"),
    # Day 13 A1
    ("Seminar on Gender Functionality Assessment Tool (GFAST) and Gender Responsiveness LGU (GERL) Assessment Tool.",
     "Deepening Session on GFAsT and the GeRL Tool: Province of Isabela – LGUs Edition"),
    # Day 15 A1
    ("Awarding of all barangays &amp; offices, recognition of partners, presentation of commitments, and ceremonial signing of Memorandum of Partnership with NAPC and OPAPRU.",
     "Culminating and Awarding Ceremony: 2026 18-Day Campaign to End VAW"),
    ("Awarding of all barangays & offices, recognition of partners, presentation of commitments, and ceremonial signing of Memorandum of Partnership with NAPC and OPAPRU.",
     "Culminating and Awarding Ceremony: 2026 18-Day Campaign to End VAW")
]

a3_files = [
    os.path.join(BASE_DIR, "18-day-campaign-calendar-a3.html"),
    os.path.join(BASE_DIR, "18-day-campaign-calendar.html"),
    os.path.join(BASE_DIR, "Final Copy", "18-day-campaign-calendar-a3.html"),
    os.path.join(BASE_DIR, "Final Copy", "18-day-campaign-calendar.html")
]

for fp in a3_files:
    with open(fp, "r", encoding="utf-8") as f:
        content = f.read()
    for target, repl in a3_replacements:
        content = content.replace(target, repl)
    with open(fp, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated {os.path.basename(fp)}")

# 2. Update A4 Page 1
p1_path = os.path.join(BASE_DIR, "18-day-campaign-calendar-a4-page1.html")
with open(p1_path, "r", encoding="utf-8") as f:
    p1 = f.read()

p1_replacements = [
    # Day 2 A1
    ("Women's economic empowerment, safe employment, anti-trafficking & cyber recruitment scam awareness.",
     "Economic Empowerment for Women Safe Employment and Anti Trafficking Forum"),
    ("Women's economic empowerment, safe employment, anti-trafficking and cyber recruitment scam awareness.",
     "Economic Empowerment for Women Safe Employment and Anti Trafficking Forum"),
    # Day 2 A2
    ("Rural women protection, livelihood, cooperative support & community prevention.",
     "Rural Women Protection, Livelihood and Cooperative Support Forum"),
    ("Rural women protection, livelihood, cooperative support, and community-based prevention.",
     "Rural Women Protection, Livelihood and Cooperative Support Forum"),
    # Day 3 A1
    ("Protection of women with disabilities & senior women; inclusive referral, support, and Sign Language Orientation.",
     "Inclusive Protection, Accessible Services, and Sign Language Orientation for Women with Disabilities and Senior Women"),
    ("Protection of women with disabilities &amp; senior women; inclusive referral and access to support, and Sign Language Orientation.",
     "Inclusive Protection, Accessible Services, and Sign Language Orientation for Women with Disabilities and Senior Women"),
    # Day 3 A3
    ("Survivor-centered care management, psychosocial first aid, women and children referral mapping.",
     "Project SUNSHINE Survivor – Centered Case Management and Referral Review"),
    ("Survivor-centered care management, psychosocial first aid, referral mapping.",
     "Project SUNSHINE Survivor – Centered Case Management and Referral Review"),
    # Day 4
    ("Multi-stakeholder dialogues, citizen participation, social accountability, survivor advocacy, and community partnership building.",
     "Multi-Stakeholder Dialogue on Accountability to Survivors and Community Partnership"),
    # Day 8 A1
    ("Safe workplace, anti-sexual harassment, internal reporting and protection mechanisms.",
     "Safe Workplace Compliance and Anti-Sexual Harassment Orientation"),
    # Day 9 A1
    ("Men as allies forum, healthy masculinity, shared responsibility & prevention of VAWC.",
     "Men as Allies and Men Opposed to Violence Everywhere (MOVE) Forum on Healthy Masculinity and Shared Responsibility"),
    ("Men as allies forum, healthy masculinity, shared responsibility, and prevention of VAWC & online abuse.",
     "Men as Allies and Men Opposed to Violence Everywhere (MOVE) Forum on Healthy Masculinity and Shared Responsibility"),
    # Day 9 A2
    ("Emergency response simulation, hotline awareness, safety drill, and rapid coordination.",
     "Safeline 922 Emergency Response Simulation and Referral Drill")
]

for target, repl in p1_replacements:
    p1 = p1.replace(target, repl)
with open(p1_path, "w", encoding="utf-8") as f:
    f.write(p1)
print("Updated 18-day-campaign-calendar-a4-page1.html")

# 3. Update A4 Page 2
p2_path = os.path.join(BASE_DIR, "18-day-campaign-calendar-a4-page2.html")
with open(p2_path, "r", encoding="utf-8") as f:
    p2 = f.read()

p2_replacements = [
    # Day 13 A1
    ("Seminar on GFAST & GERL Assessment.",
     "Deepening Session on GFAsT and the GeRL Tool: Province of Isabela – LGUs Edition"),
    ("Seminar on Gender Functionality Assessment Tool (GFAST) and Gender Responsiveness LGU (GERL) Assessment Tool.",
     "Deepening Session on GFAsT and the GeRL Tool: Province of Isabela – LGUs Edition"),
    # Day 15 A1
    ("Awarding of barangays &amp; offices, partner recognition, commitment presentations, ceremonial signing with NAPC &amp; OPAPRU.",
     "Culminating and Awarding Ceremony: 2026 18-Day Campaign to End VAW"),
    ("Awarding of all barangays &amp; offices, recognition of partners, presentation of commitments, and ceremonial signing of Memorandum of Partnership with NAPC and OPAPRU.",
     "Culminating and Awarding Ceremony: 2026 18-Day Campaign to End VAW")
]

for target, repl in p2_replacements:
    p2 = p2.replace(target, repl)
with open(p2_path, "w", encoding="utf-8") as f:
    f.write(p2)
print("Updated 18-day-campaign-calendar-a4-page2.html")

# 4. Update A4 combined
a4_path = os.path.join(BASE_DIR, "18-day-campaign-calendar-a4.html")
with open(a4_path, "r", encoding="utf-8") as f:
    a4 = f.read()
all_a4_replacements = p1_replacements + p2_replacements
for target, repl in all_a4_replacements:
    a4 = a4.replace(target, repl)
with open(a4_path, "w", encoding="utf-8") as f:
    f.write(a4)
print("Updated 18-day-campaign-calendar-a4.html")

