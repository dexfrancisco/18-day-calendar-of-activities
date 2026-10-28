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

# A3 Day 17 restoration
a3_day17_pure_weekend = '''      <!-- DAY 17 -->
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

a3_day17_restored_hybrid = '''      <!-- DAY 17 (Copied Activity: Regional Educational Research Conference + Online Advocacy) -->
      <article class="day-card active-day">
        <div class="card-top-bar">
          <span class="day-pill">DAY 17</span>
          <span class="date-text">DEC 11</span>
          <span class="weekday-text">FRI</span>
        </div>
        <div style="padding: 12px 14px; display: flex; flex-direction: column; gap: 12px; flex: 1;">
          <!-- TOP: GAD In-Person Activity -->
          <div style="flex: 1; display: flex; flex-direction: column; justify-content: space-between; gap: 6px;">
            <div class="single-lead-block" style="padding: 7px 12px; gap: 2px;">
              <span class="lead-tag-row" style="font-size: 25px;">
                <svg viewBox="0 0 16 16" style="width: 21px; height: 21px;"><path d="M8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10zm0-7a3 3 0 1 1 0-6 3 3 0 0 1 0 6z"/></svg>
                LEAD OFFICE
              </span>
              <span class="single-lead-name" style="font-size: 33px;">GAD Office</span>
            </div>
            <div class="single-act-block" style="padding: 9px 12px; gap: 5px; flex: 1; justify-content: center;">
              <span class="act-tag-badge" style="font-size: 23px; padding: 4px 12px;">MAIN ACTIVITY</span>
              <p class="single-act-desc" style="font-size: 28px; line-height: 1.24;">Regional Educational Research Conference</p>
            </div>
            <div class="single-partner-box" style="padding: 7px 12px; font-size: 25px; line-height: 1.25;">
              <strong>Partners:</strong> SDO Cauayan City, DEPED RO2
            </div>
            <div class="card-venue-box" style="padding: 7px 12px; font-size: 25px; line-height: 1.25;">
              <svg viewBox="0 0 16 16" style="width: 23px; height: 23px;"><path d="M8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10zm0-7a3 3 0 1 1 0-6 3 3 0 0 1 0 6z"/></svg>
              <span><strong>Venue:</strong> F. L. Dy Colliseum, District III, Cauayan City, Isabela</span>
            </div>
          </div>

          <!-- BOTTOM: Online Advocacy -->
          <div style="flex: 1; background: radial-gradient(circle at center, #fffaf5 0%, #ffffff 100%); border: 2.5px solid #fed7aa; border-radius: 14px; padding: 16px 14px; display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; gap: 12px;">
            <div style="width: 76px; height: 76px; border-radius: 50%; background: #ffedd5; border: 3.5px solid #fdba74; display: flex; align-items: center; justify-content: center; box-shadow: 0 4px 12px rgba(234, 88, 12, 0.12);">
              <svg viewBox="0 0 24 24" style="width: 38px; height: 38px; fill: #ea580c;"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 14.5v-9l6 4.5-6 4.5z"/></svg>
            </div>
            <div class="weekend-badge" style="font-size: 27px; padding: 6px 22px;">ONLINE ADVOCACY</div>
            <div class="weekend-advocacy-text" style="font-size: 29px; line-height: 1.36;">Posting of Advocacy Videos, Safe Spaces Pledges Videos and Advocacy Posters</div>
          </div>
        </div>
      </article>'''

a3_replacements = [
    ('grid-template-columns: 1.28fr 1.20fr 1.20fr 1.15fr 0.65fr 0.68fr;', 'grid-template-columns: 1.25fr 1.15fr 1.15fr 1.15fr 0.95fr 0.68fr;'),
    (a3_day17_pure_weekend, a3_day17_restored_hybrid)
]

print("--- Updating A3 Files ---")
update_file('18-day-campaign-calendar-a3.html', a3_replacements)
update_file('18-day-campaign-calendar.html', a3_replacements)

# A4 Day 17 restoration
a4_day17_pure_weekend = '''        <!-- DAY 17 -->
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

a4_day17_restored_active = '''        <!-- DAY 17 (Copied Activity: Regional Educational Research Conference) -->
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

a4_replacements = [
    ('grid-template-columns: 1.15fr 1.18fr 1.38fr 0.72fr 1.05fr;', 'grid-template-columns: 1.12fr 1.15fr 1.30fr 1.12fr 1.05fr;'),
    (a4_day17_pure_weekend, a4_day17_restored_active)
]

print("\n--- Updating A4 Page 2 ---")
update_file('18-day-campaign-calendar-a4-page2.html', a4_replacements)

print("\n--- Updating A4 Combined ---")
update_file('18-day-campaign-calendar-a4.html', a4_replacements)

