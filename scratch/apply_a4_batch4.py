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

css_3act = '''  /* 3 ACTIVITIES CARD */
  .card-body-3act {
    padding: 6px 8px;
    display: flex;
    flex-direction: column;
    gap: 4px;
    flex: 1;
    justify-content: space-between;
  }

  .sub-act-item-3 {
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    gap: 2.5px;
    background: #fffcf8;
    border: 1.8px solid #fed7aa;
    border-left: 6px solid #ea580c;
    border-radius: 9px;
    padding: 5px 9px;
  }

  .sub-act-item-3 .sub-act-header {
    background: #ffedd5;
    padding: 2px 7px;
    border-radius: 4px;
    font-family: 'Montserrat', sans-serif;
    font-size: 20px;
    font-weight: 900;
    color: #9a3412;
    text-transform: uppercase;
    letter-spacing: 0.4px;
    align-self: flex-start;
  }

  .sub-act-item-3 .sub-lead-name {
    font-size: 22.5px;
    font-weight: 800;
    color: #0f172a;
    line-height: 1.15;
  }

  .sub-act-item-3 .sub-act-desc {
    font-size: 20px;
    line-height: 1.18;
    color: #334155;
    font-weight: 600;
  }

  .sub-act-item-3 .sub-partner-box {
    background: #fdf4ff;
    border: 1.2px solid #f0abfc;
    border-radius: 5px;
    padding: 3.5px 7px;
    font-size: 19.5px;
    color: #701a75;
    font-weight: 700;
    line-height: 1.15;
  }

  .card-body-3act .card-venue-box {
    padding: 4px 8px;
    font-size: 20.5px;
    gap: 5px;
  }

'''

day13_old = '''        <!-- DAY 13 (2 Activities) -->
        <article class="day-card active-day">
          <div class="card-top-bar">
            <span class="day-pill">DAY 13</span>
            <span class="date-text">DEC 7</span>
            <span class="weekday-text">MON</span>
          </div>
          <div class="card-body-multi">
            <div class="sub-act-item-2">
              <div class="sub-act-header">ACTIVITY 1</div>
              <div class="sub-lead-name">📍 GAD Office</div>
              <div class="sub-act-desc">Seminar on Gender Functionality Assessment Tool (GFAST) & Gender Responsiveness LGU (GERL) Assessment.</div>
              <div class="sub-partner-box"><strong>Partners:</strong> DILG, PCW, Province of Isabela GFPS, Cauayan GFPS</div>
            </div>
            <div class="sub-act-item-2">
              <div class="sub-act-header">ACTIVITY 2</div>
              <div class="sub-lead-name">📍 CPDO / GAD KMS Team</div>
              <div class="sub-act-desc">Data-driven governance, sex-disaggregated data, monitoring dashboards, GERL tools.</div>
              <div class="sub-partner-box"><strong>Partners:</strong> IT Office, Planning Office, All Offices</div>
            </div>
            <div class="card-venue-box">
              <svg viewBox="0 0 16 16"><path d="M8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10zm0-7a3 3 0 1 1 0-6 3 3 0 0 1 0 6z"/></svg>
              <span><strong>Venue:</strong> Isabela Convention Center, San Fermin, Cauayan City</span>
            </div>
          </div>
        </article>'''

day13_new = '''        <!-- DAY 13 (3 Activities) -->
        <article class="day-card active-day">
          <div class="card-top-bar">
            <span class="day-pill">DAY 13</span>
            <span class="date-text">DEC 7</span>
            <span class="weekday-text">MON</span>
          </div>
          <div class="card-body-3act">
            <div class="sub-act-item-3">
              <div class="sub-act-header">ACTIVITY 1</div>
              <div class="sub-lead-name">📍 GAD Office</div>
              <div class="sub-act-desc">Seminar on GFAST & GERL Assessment.</div>
              <div class="sub-partner-box"><strong>Partners:</strong> DILG, PCW, Province of Isabela GFPS, Cauayan GFPS</div>
            </div>
            <div class="sub-act-item-3">
              <div class="sub-act-header">ACTIVITY 2</div>
              <div class="sub-lead-name">📍 CPDO / GAD KMS Team</div>
              <div class="sub-act-desc">Data-driven governance, sex-disaggregated data, monitoring dashboards, GERL tools.</div>
              <div class="sub-partner-box"><strong>Partners:</strong> IT Office, Planning Office, All Offices</div>
            </div>
            <div class="sub-act-item-3">
              <div class="sub-act-header">ACTIVITY 3</div>
              <div class="sub-lead-name">📍 GAD Office</div>
              <div class="sub-act-desc">Display of Orange Exhibits</div>
            </div>
            <div class="card-venue-box">
              <svg viewBox="0 0 16 16"><path d="M8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10zm0-7a3 3 0 1 1 0-6 3 3 0 0 1 0 6z"/></svg>
              <span><strong>Venue:</strong> Isabela Convention Center, San Fermin</span>
            </div>
          </div>
        </article>'''

day16_old = '''        <!-- DAY 16 (GAD Office) -->
        <article class="day-card active-day">
          <div class="card-top-bar">
            <span class="day-pill">DAY 16</span>
            <span class="date-text">DEC 10</span>
            <span class="weekday-text">THU</span>
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
              <p class="single-act-desc">GAD in Action: Enhancing Gender-Responsive Management and Leadership</p>
            </div>
            <div class="single-partner-box">
              <strong>Partners:</strong> DEPED RO2, SDO Cauayan City, CSOs
            </div>
            <div class="card-venue-box">
              <svg viewBox="0 0 16 16"><path d="M8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10zm0-7a3 3 0 1 1 0-6 3 3 0 0 1 0 6z"/></svg>
              <span><strong>Venue:</strong> F. L. Dy Colliseum</span>
            </div>
          </div>
        </article>'''

day16_new = '''        <!-- DAY 16 (2 Activities) -->
        <article class="day-card active-day">
          <div class="card-top-bar">
            <span class="day-pill">DAY 16</span>
            <span class="date-text">DEC 10</span>
            <span class="weekday-text">THU</span>
          </div>
          <div class="card-body-multi">
            <div class="sub-act-item-2">
              <div class="sub-act-header">ACTIVITY 1</div>
              <div class="sub-lead-name">📍 GAD Office</div>
              <div class="sub-act-desc">GAD in Action: Enhancing Gender-Responsive Management and Leadership</div>
              <div class="sub-partner-box"><strong>Partners:</strong> DEPED RO2, SDO Cauayan City, CSOs</div>
            </div>
            <div class="sub-act-item-2">
              <div class="sub-act-header">ACTIVITY 2</div>
              <div class="sub-lead-name">📍 GAD Office</div>
              <div class="sub-act-desc">Regional Educational Research Conference</div>
              <div class="sub-partner-box"><strong>Partners:</strong> SDO Cauayan City, DEPED RO2</div>
            </div>
            <div class="card-venue-box">
              <svg viewBox="0 0 16 16"><path d="M8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10zm0-7a3 3 0 1 1 0-6 3 3 0 0 1 0 6z"/></svg>
              <span><strong>Venue:</strong> F. L. Dy Colliseum</span>
            </div>
          </div>
        </article>'''

day17_old = '''        <!-- DAY 17 (Active Day: Regional Educational Research Conference) -->
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

day17_new = '''        <!-- DAY 17 -->
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
        </article>'''

day18_old = '''        <!-- DAY 18 -->
        <article class="day-card weekend-advocacy-day">
          <div class="card-top-bar">
            <span class="day-pill">DAY 18</span>
            <span class="date-text">DEC 12</span>
            <span class="weekday-text">SAT</span>
          </div>
          <div class="card-body-weekend">
            <div class="weekend-icon-box">
              <svg viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 14.5v-9l6 4.5-6 4.5z"/></svg>
            </div>
            <div class="weekend-badge">ONLINE ADVOCACY</div>
            <div class="weekend-advocacy-text">Posting of Advocacy Videos, Safe Spaces Pledges Videos and Advocacy Posters</div>
          </div>
        </article>'''

day18_new = '''        <!-- DAY 18 -->
        <article class="day-card active-day">
          <div class="card-top-bar">
            <span class="day-pill">DAY 18</span>
            <span class="date-text">DEC 12</span>
            <span class="weekday-text">SAT</span>
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
              <p class="single-act-desc">Posting of Accomplishment Reports for the 18-day Campaign</p>
            </div>
            <div class="card-venue-box" style="background: #fffaf5; border: 1.5px solid #fed7aa; color: #ea580c;">
              <svg viewBox="0 0 24 24" style="fill: #ea580c; width: 17px; height: 17px;"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 14.5v-9l6 4.5-6 4.5z"/></svg>
              <span><strong>Online:</strong> Social Media & Portals</span>
            </div>
          </div>
        </article>'''

a4_p2_replacements = [
    ('  /* 5 ACTIVITIES CARD */', css_3act + '  /* 5 ACTIVITIES CARD */'),
    ('grid-template-columns: 2.45fr 0.79fr 0.72fr 1.18fr;', 'grid-template-columns: 2.35fr 0.72fr 0.68fr 1.39fr;'),
    ('grid-template-columns: 1.18fr 1.22fr 1.12fr 1.12fr 0.80fr;', 'grid-template-columns: 1.15fr 1.18fr 1.38fr 0.72fr 1.05fr;'),
    (day13_old, day13_new),
    (day16_old, day16_new),
    (day17_old, day17_new),
    (day18_old, day18_new)
]

print("--- Updating A4 Page 2 ---")
update_file('18-day-campaign-calendar-a4-page2.html', a4_p2_replacements)

# In A4 combined, card-body-3act already exists from page 1, so don't duplicate CSS
a4_combined_replacements = [
    ('grid-template-columns: 2.45fr 0.79fr 0.72fr 1.18fr;', 'grid-template-columns: 2.35fr 0.72fr 0.68fr 1.39fr;'),
    ('grid-template-columns: 1.18fr 1.22fr 1.12fr 1.12fr 0.80fr;', 'grid-template-columns: 1.15fr 1.18fr 1.38fr 0.72fr 1.05fr;'),
    (day13_old, day13_new),
    (day16_old, day16_new),
    (day17_old, day17_new),
    (day18_old, day18_new)
]

print("\n--- Updating A4 Combined ---")
update_file('18-day-campaign-calendar-a4.html', a4_combined_replacements)

