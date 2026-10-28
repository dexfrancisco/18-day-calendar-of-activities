import os

def update_file(filepath, replacements):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_has_crlf = '\r\n' in content
    content_norm = content.replace('\r\n', '\n')

    all_matched = True
    for old, new in replacements:
        old_norm = old.replace('\r\n', '\n')
        new_norm = new.replace('\r\n', '\n')
        if old_norm in content_norm:
            content_norm = content_norm.replace(old_norm, new_norm)
            print(f"[{os.path.basename(filepath)}] Successfully replaced: {old_norm[:40]}...")
        else:
            print(f"[{os.path.basename(filepath)}] WARNING: Target not found: {old_norm[:40]}...")
            all_matched = False

    if original_has_crlf:
        content_norm = content_norm.replace('\n', '\r\n')

    with open(filepath, 'w', encoding='utf-8', newline='') as f:
        f.write(content_norm)

    return all_matched

# 1. A3 Replacements
a3_replacements = [
    # Day 14 Lead Office
    (
        '<span class="single-lead-name">City Tourism / Culture Office / PIO / GAD Office</span>',
        '<span class="single-lead-name">PIO, GAD Office, DepEd, ISU-Cauayan, Tourism Office, ISAC, CSOs</span>'
    ),
    # Day 15 Partners
    (
        '<div class="single-partner-box">\n            <strong>Partners:</strong> NAPC, OPAPRU, PCW, All Offices, All Partners\n          </div>',
        '<div class="single-partner-box">\n            <strong>Partners:</strong> DILG, NAPC, OPAPRU, PCW, All Offices, All Partners, Barangay, CSOs\n          </div>'
    ),
    # Day 16 Partners
    (
        '<!-- DAY 16 (New Activity: GAD Office) -->\n      <article class="day-card active-day">\n        <div class="card-top-bar">\n          <span class="day-pill">DAY 16</span>\n          <span class="date-text">DEC 10</span>\n          <span class="weekday-text">THU</span>\n        </div>\n        <div class="card-body-single">\n          <div class="single-lead-block">\n            <span class="lead-tag-row">\n              <svg viewBox="0 0 16 16"><path d="M8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10zm0-7a3 3 0 1 1 0-6 3 3 0 0 1 0 6z"/></svg>\n              LEAD OFFICE\n            </span>\n            <span class="single-lead-name">GAD Office</span>\n          </div>\n          <div class="single-act-block">\n            <span class="act-tag-badge">MAIN ACTIVITY</span>\n            <p class="single-act-desc">GAD in Action: Enhancing Gender-Responsive Management and Leadership</p>\n          </div>\n          <div class="single-partner-box">\n            <strong>Partners:</strong> SDO Cauayan City, DEPED RO2\n          </div>',
        '<!-- DAY 16 (New Activity: GAD Office) -->\n      <article class="day-card active-day">\n        <div class="card-top-bar">\n          <span class="day-pill">DAY 16</span>\n          <span class="date-text">DEC 10</span>\n          <span class="weekday-text">THU</span>\n        </div>\n        <div class="card-body-single">\n          <div class="single-lead-block">\n            <span class="lead-tag-row">\n              <svg viewBox="0 0 16 16"><path d="M8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10zm0-7a3 3 0 1 1 0-6 3 3 0 0 1 0 6z"/></svg>\n              LEAD OFFICE\n            </span>\n            <span class="single-lead-name">GAD Office</span>\n          </div>\n          <div class="single-act-block">\n            <span class="act-tag-badge">MAIN ACTIVITY</span>\n            <p class="single-act-desc">GAD in Action: Enhancing Gender-Responsive Management and Leadership</p>\n          </div>\n          <div class="single-partner-box">\n            <strong>Partners:</strong> DEPED RO2, SDO Cauayan City, CSOs\n          </div>'
    ),
    # Day 17 Main Activity
    (
        '<p class="single-act-desc" style="font-size: 30px; line-height: 1.28;">Regional Planning Conference</p>',
        '<p class="single-act-desc" style="font-size: 28px; line-height: 1.24;">Regional Educational Research Conference</p>'
    )
]

print("--- Updating A3 Files ---")
update_file('18-day-campaign-calendar-a3.html', a3_replacements)
update_file('18-day-campaign-calendar.html', a3_replacements)

