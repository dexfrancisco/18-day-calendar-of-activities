import os
import re

HTML_DIR = r"c:\Users\CODEX\Desktop\18 day calendar of activity\18 day calendar of activity\scratch\final_html"

revisions = {
    "02-day-02.html": [
        "Economic Empowerment for Women Safe Employment and Anti Trafficking Forum",
        "Rural Women Protection, Livelihood and Cooperative Support Forum"
    ],
    "03-day-03.html": [
        "Inclusive Protection, Accessible Services, and Sign Language Orientation for Women with Disabilities and Senior Women",
        "Project SUNSHINE Survivor – Centered Case Management and Referral Review"
    ],
    "04-day-04.html": [
        "Multi-Stakeholder Dialogue on Accountability to Survivors and Community Partnership"
    ],
    "08-day-08.html": [
        "Safe Workplace Compliance and Anti-Sexual Harassment Orientation"
    ],
    "09-day-09.html": [
        "End VAWC Action Forum: Enhancing Survivor Healthcare, Legal Frameworks, LCAT-VAW Desk Coordination, and Digital Safety Innovations",
        "ICON"
    ],
    "10-day-10.html": [
        "Men as Allies and Men Opposed to Violence Everywhere (MOVE) Forum on Healthy Masculinity and Shared Responsibility",
        "Safeline 922 Emergency Response Simulation and Referral Drill"
    ],
    "13-day-13.html": [
        "Deepening Session on GFAsT and the GeRL Tool: Province of Isabela – LGUs Edition"
    ],
    "15-day-15.html": [
        "Culminating and Awarding Ceremony: 2026 18-Day Campaign to End VAW"
    ]
}

print("=== CHECKING REVISED TITLES IN FINAL_HTML ===")
for fname, targets in revisions.items():
    path = os.path.join(HTML_DIR, fname)
    if not os.path.exists(path):
        print(f"MISSING: {fname}")
        continue
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    for t in targets:
        # replace smart dashes if needed
        found = t in content or t.replace("–", "-") in content or t.replace("-", "–") in content
        print(f"{fname}: '{t[:40]}...' -> {'FOUND' if found else 'NOT FOUND'}")

