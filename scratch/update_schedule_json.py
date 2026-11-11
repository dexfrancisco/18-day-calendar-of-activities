import json

with open('scratch/schedule_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

d9 = data[9]
d10 = data[10]

# Preserve day identifiers
d9_id = d9["id"]
d9_num = d9["day_number"]
d9_fn = d9["filename"]
d9_icon = d9["icon_filename"]
d9_badge = d9["badge"]
d9_date = d9["date_str"]

d10_id = d10["id"]
d10_num = d10["day_number"]
d10_fn = d10["filename"]
d10_icon = d10["icon_filename"]
d10_badge = d10["badge"]
d10_date = d10["date_str"]

# Build updated Day 9 with Day 10's content, venue = ICON
new_d9 = {
    "id": d9_id,
    "day_number": d9_num,
    "filename": d9_fn,
    "icon_filename": d9_icon,
    "badge": d9_badge,
    "date_str": d9_date,
    "layout_type": "single_activity",
    "main_activity": "End VAWC Action Forum: Enhancing Survivor Healthcare, Legal Frameworks, LCAT-VAW Desk Coordination, and Digital Safety Innovations",
    "lead_office": "City Health Office, City Legal Office, PNP-WCPD, Liga ng mga Barangay, JCD GAD CONNECT & CDRRMO",
    "partners": "DILG, PNP, BJMP, City Prosecutor's Office, PAO, Barangays, Barangay Officials, BSWDO, Hospitals, RHUs, NGOs, Mental Health Partners, GAD Office, Tech Partners, JCI",
    "venue": "ICON, San Fermin, Cauayan City, Isabela",
    "activities_detailed": d10["activities_detailed"]
}

# Build updated Day 10 with Day 9's content, venue = F. L. Dy Colliseum
new_d10 = {
    "id": d10_id,
    "day_number": d10_num,
    "filename": d10_fn,
    "icon_filename": d10_icon,
    "badge": d10_badge,
    "date_str": d10_date,
    "layout_type": "standard_activities",
    "activities": d9["activities"],
    "partners": d9["partners"],
    "venue": "F. L. Dy Colliseum, District III, Cauayan City, Isabela"
}

data[9] = new_d9
data[10] = new_d10

with open('scratch/schedule_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("✓ Updated schedule_data.json successfully!")

