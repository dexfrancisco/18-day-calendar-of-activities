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

a4_p2_replacements = [
    # Grid adjustment for Row 2
    (
        'grid-template-columns: 1.22fr 1.26fr 1.16fr 0.75fr 0.75fr;',
        'grid-template-columns: 1.18fr 1.22fr 1.12fr 1.12fr 0.80fr;'
    ),
    # Day 14 Lead Office
    (
        '<span class="single-lead-name">City Tourism / Culture / PIO / GAD</span>',
        '<span class="single-lead-name" style="font-size: 20px; line-height: 1.15;">PIO, GAD Office, DepEd, ISU-Cauayan, Tourism Office, ISAC, CSOs</span>'
    ),
    # Day 15 Partners
    (
        '<div class="single-partner-box">\n              <strong>Partners:</strong> NAPC, OPAPRU, PCW, All Offices\n            </div>',
        '<div class="single-partner-box">\n              <strong>Partners:</strong> DILG, NAPC, OPAPRU, PCW, All Offices, All Partners, Barangay, CSOs\n            </div>'
    ),
    # Day 16 Partners
    (
        '<div class="single-partner-box">\n              <strong>Partners:</strong> SGO Cauayan City, DEPED RO2\n            </div>',
        '<div class="single-partner-box">\n              <strong>Partners:</strong> DEPED RO2, SDO Cauayan City, CSOs\n            </div>'
    ),
    # Day 17 Card (Upgraded from pure weekend to Active Day with Regional Educational Research Conference)
    (
        '''        <!-- DAY 17 -->
        <article class="day-card weekend-advocacy-day">
          <div class="card-top-bar">
            <span class="day-pill">DAY 17</span>
            <span class="date-text">DEC 11</span>
            <span class="weekday-text">FRI</span>
          </div>
          <div class="card-body-weekend">
            <div class="weekend-icon-box">
              <svg viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 14.5v-9l6 4.5-6 4.5z"/></svg>
            </div>
            <div class="weekend-badge">ONLINE ADVOCACY</div>
            <div class="weekend-advocacy-text">Posting of Advocacy Videos, Safe Spaces Pledges Videos and Advocacy Posters</div>
          </div>
        </article>''',
        '''        <!-- DAY 17 (Active Day: Regional Educational Research Conference) -->
        <article class="day-card active-day">
          <div class="card-top-bar">
            <span class="day-pill">DAY 17</span>
            <span class="date-text">DEC 11</span>
            <span class="weekday-text">FRI</span>
          </div>
          <div class="card-body-single">
            <div class="single-lead-block">
              <span class="lead-tag-row">
                <svg viewBox="0 0 16 16"><path d="M8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10zm0-7a3 3 0 1 1 0-6 3 3 0 0 1 0 6z"/></svg>
                LEAD OFFICE
              </span>
              <span class="single-lead-name">GAD Office</span>
            </div>
            <div class="single-act-block">
              <span class="act-tag-badge">MAIN ACTIVITY</span>
              <p class="single-act-desc">Regional Educational Research Conference</p>
            </div>
            <div class="single-partner-box">
              <strong>Partners:</strong> SDO Cauayan City, DEPED RO2
            </div>
            <div class="card-venue-box">
              <svg viewBox="0 0 16 16"><path d="M8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10zm0-7a3 3 0 1 1 0-6 3 3 0 0 1 0 6z"/></svg>
              <span><strong>Venue:</strong> F. L. Dy Colliseum</span>
            </div>
          </div>
        </article>'''
    )
]

print("--- Updating A4 Page 2 ---")
update_file('18-day-campaign-calendar-a4-page2.html', a4_p2_replacements)

print("\n--- Updating A4 Combined ---")
update_file('18-day-campaign-calendar-a4.html', a4_p2_replacements)

