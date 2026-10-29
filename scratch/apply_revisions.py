import re
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
            print(f"[{os.path.basename(filepath)}] Successfully replaced: {old_norm[:45]}...")
        else:
            print(f"[{os.path.basename(filepath)}] WARNING: Target not found: {old_norm[:45]}...")
            all_matched = False

    if original_has_crlf:
        content_norm = content_norm.replace('\n', '\r\n')

    with open(filepath, 'w', encoding='utf-8', newline='') as f:
        f.write(content_norm)

    return all_matched

# ==========================================
# 1. A3 Replacements
# ==========================================

# Day 1 in A3
a3_day1_old = '''            <div class="card-venue-box">
              <svg viewBox="0 0 16 16"><path d="M8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10zm0-7a3 3 0 1 1 0-6 3 3 0 0 1 0 6z"/></svg>
              <span><strong>Venue:</strong> City Sports Complex, Tagaran</span>
            </div>
          </div>
        </article>

        <!-- DAY 2 (3 Activities) -->'''

a3_day1_new = '''            <div class="card-venue-box">
              <svg viewBox="0 0 16 16"><path d="M8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10zm0-7a3 3 0 1 1 0-6 3 3 0 0 1 0 6z"/></svg>
              <span><strong>Venue:</strong> CITYWIDE</span>
            </div>
          </div>
        </article>

        <!-- DAY 2 (3 Activities) -->'''

# Day 2 in A3
a3_day2_old = '''            <div class="card-venue-box">
              <svg viewBox="0 0 16 16"><path d="M8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10zm0-7a3 3 0 1 1 0-6 3 3 0 0 1 0 6z"/></svg>
              <span><strong>Venue:</strong> Isabela Convention Center, San Fermin, Cauayan City, Isabela</span>
            </div>
          </div>
        </article>

        <!-- DAY 3 (4 Activities: PDAO & OSCA, GAD Office, CSWDO, City Population Office) -->'''

a3_day2_new = '''            <div class="card-venue-box">
              <svg viewBox="0 0 16 16"><path d="M8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10zm0-7a3 3 0 1 1 0-6 3 3 0 0 1 0 6z"/></svg>
              <span><strong>Venue:</strong> F. L. Dy Colliseum, District III, Cauayan City, Isabela</span>
            </div>
          </div>
        </article>

        <!-- DAY 3 (4 Activities: PDAO & OSCA, GAD Office, CSWDO, City Population Office) -->'''

# Day 8 in A3
a3_day8_old = '''        <!-- DAY 8 -->
        <article class="day-card active-day">
          <div class="card-top-bar">
            <span class="day-pill">DAY 8</span>
            <span class="date-text">DEC 2</span>
            <span class="weekday-text">WED</span>
          </div>
          <div class="card-body-single">
            <div class="single-lead-block">
              <span class="lead-tag-row">
                <svg viewBox="0 0 16 16"><path d="M8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10zm0-7a3 3 0 1 1 0-6 3 3 0 0 1 0 6z"/></svg>
                LEAD OFFICE
              </span>
              <span class="single-lead-name">CHRMO & CODI</span>
            </div>
            <div class="single-act-block">
              <span class="act-tag-badge">MAIN ACTIVITY</span>
              <p class="single-act-desc">Safe workplace, anti-sexual harassment, internal reporting and protection mechanisms.</p>
            </div>
            <div class="single-partner-box">
              <strong>Partners:</strong> DILG, HR Office, GAD Office, CSOs
            </div>
            <div class="card-venue-box">
              <svg viewBox="0 0 16 16"><path d="M8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10zm0-7a3 3 0 1 1 0-6 3 3 0 0 1 0 6z"/></svg>
              <span><strong>Venue:</strong> F. L. Dy Colliseum, District III, Cauayan City, Isabela</span>
            </div>
          </div>
        </article>'''

a3_day8_new = '''        <!-- DAY 8 (2 Activities: CHRMO & CODI, CHO) -->
        <article class="day-card active-day">
          <div class="card-top-bar">
            <span class="day-pill">DAY 8</span>
            <span class="date-text">DEC 2</span>
            <span class="weekday-text">WED</span>
          </div>
          <div class="card-body-multi">
            <!-- Sub 1 -->
            <div class="sub-act-item-2">
              <div class="sub-act-header">ACTIVITY 1</div>
              <div class="sub-lead-name">📍 CHRMO &amp; CODI</div>
              <div class="sub-act-desc">Safe workplace, anti-sexual harassment, internal reporting and protection mechanisms.</div>
            </div>
            <!-- Sub 2 -->
            <div class="sub-act-item-2">
              <div class="sub-act-header">ACTIVITY 2</div>
              <div class="sub-lead-name">📍 City Health Office (CHO)</div>
              <div class="sub-act-desc">World Aids Day Celebrations 2026 : &ldquo;Ending Aids Starts with Access&rdquo;</div>
            </div>
            <div class="card-partner-box">
              <strong>Partners:</strong> DILG, HR Office, GAD Office, CSOs
            </div>
            <div class="card-venue-box">
              <svg viewBox="0 0 16 16"><path d="M8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10zm0-7a3 3 0 1 1 0-6 3 3 0 0 1 0 6z"/></svg>
              <span><strong>Venue:</strong> F. L. Dy Colliseum, District III, Cauayan City, Isabela</span>
            </div>
          </div>
        </article>'''

# Day 10 in A3
a3_day10_old = '''            <div class="card-venue-box">
              <svg viewBox="0 0 16 16"><path d="M8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10zm0-7a3 3 0 1 1 0-6 3 3 0 0 1 0 6z"/></svg>
              <span><strong>Venue:</strong> F. L. Dy Colliseum, District III, Cauayan City, Isabela</span>
            </div>
          </div>
        </article>

        <!-- DAY 11 -->'''

a3_day10_new = '''            <div class="card-venue-box">
              <svg viewBox="0 0 16 16"><path d="M8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10zm0-7a3 3 0 1 1 0-6 3 3 0 0 1 0 6z"/></svg>
              <span><strong>Venue:</strong> Isabela Convention Center, San Fermin, Cauayan City, Isabela</span>
            </div>
          </div>
        </article>

        <!-- DAY 11 -->'''

a3_replacements = [
    (a3_day1_old, a3_day1_new),
    (a3_day2_old, a3_day2_new),
    (a3_day8_old, a3_day8_new),
    (a3_day10_old, a3_day10_new)
]

print("--- Updating A3 Files ---")
for fp in ['18-day-campaign-calendar-a3.html', '18-day-campaign-calendar.html']:
    update_file(fp, a3_replacements)

# ==========================================
# 2. A4 Page 1 Replacements
# ==========================================

# Day 1 in A4 P1
a4_p1_day1_old = '''            <div class="card-venue-box">
              <svg viewBox="0 0 16 16"><path d="M8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10zm0-7a3 3 0 1 1 0-6 3 3 0 0 1 0 6z"/></svg>
              <span><strong>Venue:</strong> City Sports Complex, Tagaran</span>
            </div>
          </div>
        </article>

        <!-- DAY 2 (3 Activities) -->'''

a4_p1_day1_new = '''            <div class="card-venue-box">
              <svg viewBox="0 0 16 16"><path d="M8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10zm0-7a3 3 0 1 1 0-6 3 3 0 0 1 0 6z"/></svg>
              <span><strong>Venue:</strong> CITYWIDE</span>
            </div>
          </div>
        </article>

        <!-- DAY 2 (3 Activities) -->'''

# Day 2 in A4 P1
a4_p1_day2_old = '''            <div class="card-venue-box">
              <svg viewBox="0 0 16 16"><path d="M8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10zm0-7a3 3 0 1 1 0-6 3 3 0 0 1 0 6z"/></svg>
              <span><strong>Venue:</strong> Isabela Convention Center (ICON)</span>
            </div>
          </div>
        </article>

        <!-- DAY 3 (4 Activities: PDAO & OSCA, GAD Office, CSWDO, City Population Office) -->'''

a4_p1_day2_new = '''            <div class="card-venue-box">
              <svg viewBox="0 0 16 16"><path d="M8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10zm0-7a3 3 0 1 1 0-6 3 3 0 0 1 0 6z"/></svg>
              <span><strong>Venue:</strong> F. L. Dy Colliseum, District III</span>
            </div>
          </div>
        </article>

        <!-- DAY 3 (4 Activities: PDAO & OSCA, GAD Office, CSWDO, City Population Office) -->'''

# Day 8 in A4 P1
a4_p1_day8_old = '''        <!-- DAY 8 -->
        <article class="day-card active-day">
          <div class="card-top-bar">
            <span class="day-pill">DAY 8</span>
            <span class="date-text">DEC 2</span>
            <span class="weekday-text">WED</span>
          </div>
          <div class="card-body-single">
            <div class="single-lead-block">
              <span class="lead-tag-row">
                <svg viewBox="0 0 16 16"><path d="M8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10zm0-7a3 3 0 1 1 0-6 3 3 0 0 1 0 6z"/></svg>
                LEAD OFFICE
              </span>
              <span class="single-lead-name">CHRMO & CODI</span>
            </div>
            <div class="single-act-block">
              <span class="act-tag-badge">MAIN ACTIVITY</span>
              <p class="single-act-desc">Safe workplace, anti-sexual harassment, internal reporting and protection mechanisms.</p>
            </div>
            <div class="single-partner-box">
              <strong>Partners:</strong> DILG, HR Office, GAD Office, CSOs
            </div>
            <div class="card-venue-box">
              <svg viewBox="0 0 16 16"><path d="M8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10zm0-7a3 3 0 1 1 0-6 3 3 0 0 1 0 6z"/></svg>
              <span><strong>Venue:</strong> F. L. Dy Colliseum, District III</span>
            </div>
          </div>
        </article>'''

a4_p1_day8_new = '''        <!-- DAY 8 (2 Activities) -->
        <article class="day-card active-day">
          <div class="card-top-bar">
            <span class="day-pill">DAY 8</span>
            <span class="date-text">DEC 2</span>
            <span class="weekday-text">WED</span>
          </div>
          <div class="card-body-multi">
            <div class="sub-act-item-2">
              <div class="sub-act-header">ACTIVITY 1</div>
              <div class="sub-lead-name">📍 CHRMO &amp; CODI</div>
              <div class="sub-act-desc">Safe workplace, anti-sexual harassment, internal reporting and protection mechanisms.</div>
            </div>
            <div class="sub-act-item-2">
              <div class="sub-act-header">ACTIVITY 2</div>
              <div class="sub-lead-name">📍 City Health Office (CHO)</div>
              <div class="sub-act-desc">World Aids Day Celebrations 2026 : &ldquo;Ending Aids Starts with Access&rdquo;</div>
            </div>
            <div class="card-partner-box">
              <strong>Partners:</strong> DILG, HR Office, GAD Office, CSOs
            </div>
            <div class="card-venue-box">
              <svg viewBox="0 0 16 16"><path d="M8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10zm0-7a3 3 0 1 1 0-6 3 3 0 0 1 0 6z"/></svg>
              <span><strong>Venue:</strong> F. L. Dy Colliseum, District III</span>
            </div>
          </div>
        </article>'''

# Row 3 CSS in A4 P1
a4_p1_css_old = '''  .p1-grid-row3 {
    display: grid;
    grid-template-columns: 0.82fr 0.82fr 1.71fr;
    gap: 10px;
    flex: 1;
  }'''

a4_p1_css_new = '''  .p1-grid-row3 {
    display: grid;
    grid-template-columns: 0.82fr 1.25fr 1.35fr;
    gap: 10px;
    flex: 1;
  }'''

a4_p1_replacements = [
    (a4_p1_day1_old, a4_p1_day1_new),
    (a4_p1_day2_old, a4_p1_day2_new),
    (a4_p1_day8_old, a4_p1_day8_new),
    (a4_p1_css_old, a4_p1_css_new)
]

print("--- Updating A4 Page 1 ---")
update_file('18-day-campaign-calendar-a4-page1.html', a4_p1_replacements)

# ==========================================
# 3. A4 Page 2 Replacements
# ==========================================

# Day 10 in A4 P2
a4_p2_day10_old = '''            <div class="card-venue-box">
              <svg viewBox="0 0 16 16"><path d="M8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10zm0-7a3 3 0 1 1 0-6 3 3 0 0 1 0 6z"/></svg>
              <span><strong>Venue:</strong> F. L. Dy Colliseum, District III</span>
            </div>
          </div>
        </article>

        <!-- DAY 11 -->'''

a4_p2_day10_new = '''            <div class="card-venue-box">
              <svg viewBox="0 0 16 16"><path d="M8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10zm0-7a3 3 0 1 1 0-6 3 3 0 0 1 0 6z"/></svg>
              <span><strong>Venue:</strong> Isabela Convention Center (ICON)</span>
            </div>
          </div>
        </article>

        <!-- DAY 11 -->'''

a4_p2_replacements = [
    (a4_p2_day10_old, a4_p2_day10_new)
]

print("--- Updating A4 Page 2 ---")
update_file('18-day-campaign-calendar-a4-page2.html', a4_p2_replacements)

# ==========================================
# 4. A4 Combined Replacements
# ==========================================

a4_comb_replacements = [
    (a4_p1_day1_old, a4_p1_day1_new),
    (a4_p1_day2_old, a4_p1_day2_new),
    (a4_p1_day8_old, a4_p1_day8_new),
    (a4_p1_css_old, a4_p1_css_new),
    (a4_p2_day10_old, a4_p2_day10_new)
]

print("--- Updating A4 Combined ---")
update_file('18-day-campaign-calendar-a4.html', a4_comb_replacements)

