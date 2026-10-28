import os

def update_file(filepath, replacements):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Normalize to \n for replacement
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

# 1. Replacements for A3 files
a3_replacements = [
    # Day 6 Lead
    (
        '<span class="single-lead-name">City Youth Development Office / Kalinga Kabataan Program</span>',
        '<span class="single-lead-name">City Youth Development Office, SK Federation of Cauayan City / Kalinga Kabataan Program</span>'
    ),
    # Day 6 Partners
    (
        '<div class="single-partner-box">\n              <strong>Partners:</strong> DepEd, SK, VM Office, Sangguniang Panlungsod, Youth Groups\n            </div>',
        '<div class="single-partner-box">\n              <strong>Partners:</strong> DepEd, SK, VM Office, Sangguniang Panlungsod, Youth Groups, Faith Groups, PNP, Legal Office\n            </div>'
    ),
    # Day 7 Partners
    (
        '<!-- DAY 7 -->\n        <article class="day-card active-day">\n          <div class="card-top-bar">\n            <span class="day-pill">DAY 7</span>\n            <span class="date-text">DEC 1</span>\n            <span class="weekday-text">TUE</span>\n          </div>\n          <div class="card-body-single">\n            <div class="single-lead-block">\n              <span class="lead-tag-row">\n                <svg viewBox="0 0 16 16"><path d="M8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10zm0-7a3 3 0 1 1 0-6 3 3 0 0 1 0 6z"/></svg>\n                LEAD OFFICE\n              </span>\n              <span class="single-lead-name">CHRMO & CODI</span>\n            </div>\n            <div class="single-act-block">\n              <span class="act-tag-badge">MAIN ACTIVITY</span>\n              <p class="single-act-desc">Safe workplace, anti-sexual harassment, internal reporting and protection mechanisms.</p>\n            </div>\n            <div class="single-partner-box">\n              <strong>Partners:</strong> HR Units, DILG, CSOs\n            </div>',
        '<!-- DAY 7 -->\n        <article class="day-card active-day">\n          <div class="card-top-bar">\n            <span class="day-pill">DAY 7</span>\n            <span class="date-text">DEC 1</span>\n            <span class="weekday-text">TUE</span>\n          </div>\n          <div class="card-body-single">\n            <div class="single-lead-block">\n              <span class="lead-tag-row">\n                <svg viewBox="0 0 16 16"><path d="M8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10zm0-7a3 3 0 1 1 0-6 3 3 0 0 1 0 6z"/></svg>\n                LEAD OFFICE\n              </span>\n              <span class="single-lead-name">CHRMO & CODI</span>\n            </div>\n            <div class="single-act-block">\n              <span class="act-tag-badge">MAIN ACTIVITY</span>\n              <p class="single-act-desc">Safe workplace, anti-sexual harassment, internal reporting and protection mechanisms.</p>\n            </div>\n            <div class="single-partner-box">\n              <strong>Partners:</strong> HR Office, GAD Office, DILG, CSOs\n            </div>'
    ),
    # Day 8 Partners
    (
        '<!-- DAY 8 -->\n        <article class="day-card active-day">\n          <div class="card-top-bar">\n            <span class="day-pill">DAY 8</span>\n            <span class="date-text">DEC 2</span>\n            <span class="weekday-text">WED</span>\n          </div>\n          <div class="card-body-single">\n            <div class="single-lead-block">\n              <span class="lead-tag-row">\n                <svg viewBox="0 0 16 16"><path d="M8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10zm0-7a3 3 0 1 1 0-6 3 3 0 0 1 0 6z"/></svg>\n                LEAD OFFICE\n              </span>\n              <span class="single-lead-name">CHRMO & CODI</span>\n            </div>\n            <div class="single-act-block">\n              <span class="act-tag-badge">MAIN ACTIVITY</span>\n              <p class="single-act-desc">Safe workplace, anti-sexual harassment, internal reporting and protection mechanisms.</p>\n            </div>\n            <div class="single-partner-box">\n              <strong>Partners:</strong> HR Units, DILG, CSOs\n            </div>',
        '<!-- DAY 8 -->\n        <article class="day-card active-day">\n          <div class="card-top-bar">\n            <span class="day-pill">DAY 8</span>\n            <span class="date-text">DEC 2</span>\n            <span class="weekday-text">WED</span>\n          </div>\n          <div class="card-body-single">\n            <div class="single-lead-block">\n              <span class="lead-tag-row">\n                <svg viewBox="0 0 16 16"><path d="M8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10zm0-7a3 3 0 1 1 0-6 3 3 0 0 1 0 6z"/></svg>\n                LEAD OFFICE\n              </span>\n              <span class="single-lead-name">CHRMO & CODI</span>\n            </div>\n            <div class="single-act-block">\n              <span class="act-tag-badge">MAIN ACTIVITY</span>\n              <p class="single-act-desc">Safe workplace, anti-sexual harassment, internal reporting and protection mechanisms.</p>\n            </div>\n            <div class="single-partner-box">\n              <strong>Partners:</strong> HR Office, GAD Office, DILG, CSOs\n            </div>'
    ),
    # Day 9 Partners
    (
        '<div class="sub-partner-box"><strong>Partners:</strong> CSOs, Faith Groups, Youth Groups, JCI, PNP, Academe, DepEd</div>',
        '<div class="sub-partner-box"><strong>Partners:</strong> JCI, PNP, BJMP, CDRRMO, BFP, Faith Groups, Youth Groups, Academe, DepEd, MASON, ROTARY Club of Cauayan</div>'
    ),
    # Day 10 Activity 1
    (
        '<div class="sub-act-header">ACTIVITY 1</div>\n              <div class="sub-lead-name">📍 City Health Office</div>\n              <div class="sub-act-desc">Health response, mental health, reproductive health, medico-legal awareness, and support services for survivors.</div>\n              <div class="sub-partner-box"><strong>Partners:</strong> Hospitals, RHUs, NGOs, Mental Health Partners, BJMP</div>',
        '<div class="sub-act-header">ACTIVITY 1</div>\n              <div class="sub-lead-name">📍 City Health Office</div>\n              <div class="sub-act-desc">Health response, mental health, reproductive health, medico-legal awareness, and support services for survivors.</div>\n              <div class="sub-partner-box"><strong>Partners:</strong> Hospitals, RHUs, NGOs, Mental Health Partners, BJMP, Barangay Officials</div>'
    ),
    # Day 10 Activity 2
    (
        '<div class="sub-act-header">ACTIVITY 2</div>\n              <div class="sub-lead-name">📍 City Legal Office</div>\n              <div class="sub-act-desc">Orientation on RA 9262, Safe Spaces Act, Anti-Trafficking, cyber-related VAWC and online crimes; legal referral pathways.</div>\n              <div class="sub-partner-box"><strong>Partners:</strong> City Prosecutor\'s Office, PNP, DILG, BJMP</div>',
        '<div class="sub-act-header">ACTIVITY 2</div>\n              <div class="sub-lead-name">📍 City Legal Office</div>\n              <div class="sub-act-desc">Orientation on RA 9262, Safe Spaces Act, Anti-Trafficking, cyber-related VAWC and online crimes; legal referral pathways.</div>\n              <div class="sub-partner-box"><strong>Partners:</strong> City Prosecutor\'s Office, PNP, DILG, BJMP, Barangay</div>'
    ),
    # Day 10 Activity 5
    (
        '<div class="sub-act-header">ACTIVITY 5</div>\n              <div class="sub-lead-name">📍 JCD GAD CONNECT and CDRRMO</div>\n              <div class="sub-act-desc">Digital Safety Day: demo of Project S.U.N.S.H.I.N.E., iReport VAWC, Safe Line, online reporting, cyber safety & digital evidence awareness.</div>\n              <div class="sub-partner-box"><strong>Partners:</strong> GAD Office, PNP, PLDT, Tech Partners, BJMP</div>',
        '<div class="sub-act-header">ACTIVITY 5</div>\n              <div class="sub-lead-name">📍 JCD GAD CONNECT and CDRRMO</div>\n              <div class="sub-act-desc">Digital Safety Day: demo of Project S.U.N.S.H.I.N.E., iReport VAWC, Safe Line, online reporting, cyber safety & digital evidence awareness.</div>\n              <div class="sub-partner-box"><strong>Partners:</strong> GAD Office, PNP, Tech Partners, BJMP, JCI, Barangay Officials</div>'
    ),
    # Day 13 Activity 1
    (
        '<div class="sub-partner-box"><strong>Partners:</strong> PCW, Province of Isabela GFPS, Cauayan City GFPS</div>',
        '<div class="sub-partner-box"><strong>Partners:</strong> DILG, PCW, Province of Isabela GFPS, Cauayan City GFPS</div>'
    )
]

print("--- Updating A3 Files ---")
update_file('18-day-campaign-calendar-a3.html', a3_replacements)
update_file('18-day-campaign-calendar.html', a3_replacements)

