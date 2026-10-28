import os
import re

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

css_old = '  /* VENUE BOX STYLING */'
css_new = '''  /* SHARED MULTI-ACTIVITY PARTNER BOX (Top of Venue) */
  .card-partner-box {
    background: #fdf4ff;
    border: 2px solid #f0abfc;
    border-radius: 9px;
    padding: 6px 12px;
    font-size: 25px;
    color: #701a75;
    font-weight: 700;
    line-height: 1.22;
  }

  .card-partner-box strong {
    color: #86198f;
    font-weight: 900;
  }

  .card-body-5act .card-partner-box {
    font-size: 23px;
    padding: 5px 10px;
    line-height: 1.18;
  }

  .card-body-4act .card-partner-box {
    font-size: 20px;
    padding: 3px 8px;
    line-height: 1.15;
    border-radius: 6px;
  }

  /* VENUE BOX STYLING */'''

day1_old = '''        <!-- DAY 1 (2 Activities) -->
        <article class="day-card active-day">
          <div class="card-top-bar">
            <span class="day-pill">DAY 1</span>
            <span class="date-text">NOV 25</span>
            <span class="weekday-text">WED</span>
          </div>
          <div class="card-body-multi">
            <!-- Sub 1 -->
            <div class="sub-act-item-2">
              <div class="sub-act-header">ACTIVITY 1</div>
              <div class="sub-lead-name">📍 GAD Office</div>
              <div class="sub-act-desc">Wellness and Essential Care Distribution for Project S.U.N.S.H.I.N.E Beneficiaries.</div>
              <div class="sub-partner-box"><strong>Partners:</strong> BJMP, PNP, CSWD</div>
            </div>
            <!-- Sub 2 -->
            <div class="sub-act-item-2">
              <div class="sub-act-header">ACTIVITY 2</div>
              <div class="sub-lead-name">📍 GAD Office & Office of the City Mayor</div>
              <div class="sub-act-desc">Opening Program, Orange Campaign Kickoff, Parade around the City, Policy Call to Action, Project S.U.N.S.H.I.N.E. public launch.</div>
              <div class="sub-partner-box"><strong>Partners:</strong> All City Offices, Barangays, PNP, BFP, BJMP, Academe, CSOs</div>
            </div>
            <div class="card-venue-box">
              <svg viewBox="0 0 16 16"><path d="M8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10zm0-7a3 3 0 1 1 0-6 3 3 0 0 1 0 6z"/></svg>
              <span><strong>Venue:</strong> City Sports Complex, Tagaran</span>
            </div>
          </div>
        </article>'''

day1_new = '''        <!-- DAY 1 (2 Activities) -->
        <article class="day-card active-day">
          <div class="card-top-bar">
            <span class="day-pill">DAY 1</span>
            <span class="date-text">NOV 25</span>
            <span class="weekday-text">WED</span>
          </div>
          <div class="card-body-multi">
            <!-- Sub 1 -->
            <div class="sub-act-item-2">
              <div class="sub-act-header">ACTIVITY 1</div>
              <div class="sub-lead-name">📍 GAD Office</div>
              <div class="sub-act-desc">Wellness and Essential Care Distribution for Project S.U.N.S.H.I.N.E Beneficiaries.</div>
            </div>
            <!-- Sub 2 -->
            <div class="sub-act-item-2">
              <div class="sub-act-header">ACTIVITY 2</div>
              <div class="sub-lead-name">📍 GAD Office & Office of the City Mayor</div>
              <div class="sub-act-desc">Opening Program, Orange Campaign Kickoff, Parade around the City, Policy Call to Action, Project S.U.N.S.H.I.N.E. public launch.</div>
            </div>
            <div class="card-partner-box">
              <strong>Partners:</strong> All City Offices, Barangays, PNP, BFP, BJMP, CSWD, Academe, CSOs
            </div>
            <div class="card-venue-box">
              <svg viewBox="0 0 16 16"><path d="M8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10zm0-7a3 3 0 1 1 0-6 3 3 0 0 1 0 6z"/></svg>
              <span><strong>Venue:</strong> City Sports Complex, Tagaran</span>
            </div>
          </div>
        </article>'''

day2_old = '''        <!-- DAY 2 (3 Activities) -->
        <article class="day-card active-day">
          <div class="card-top-bar">
            <span class="day-pill">DAY 2</span>
            <span class="date-text">NOV 26</span>
            <span class="weekday-text">THU</span>
          </div>
          <div class="card-body-3act">
            <!-- Sub 1 -->
            <div class="sub-act-item-3">
              <div class="sub-act-header">ACTIVITY 1</div>
              <div class="sub-lead-name">📍 PESO / COOP / CEDIPO</div>
              <div class="sub-act-desc">Women's economic empowerment, safe employment, anti-trafficking and cyber recruitment scam awareness.</div>
              <div class="sub-partner-box"><strong>Partners:</strong> DOLE, OWWA, DTI, Private Sector</div>
            </div>
            <!-- Sub 2 -->
            <div class="sub-act-item-3">
              <div class="sub-act-header">ACTIVITY 2</div>
              <div class="sub-lead-name">📍 City Agriculture & Cooperative Office</div>
              <div class="sub-act-desc">Rural women protection, livelihood, cooperative support, and community-based prevention.</div>
              <div class="sub-partner-box"><strong>Partners:</strong> DA, Cooperatives, MSMES, Barangays, CSOs</div>
            </div>
            <div class="card-venue-box">
              <svg viewBox="0 0 16 16"><path d="M8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10zm0-7a3 3 0 1 1 0-6 3 3 0 0 1 0 6z"/></svg>
              <span><strong>Venue:</strong> Isabela Convention Center, San Fermin, Cauayan City, Isabela</span>
            </div>
            <!-- Sub 3 (Nov 26–30, 2026) -->
            <div class="sub-act-item-3">
              <div style="display: flex; align-items: center; justify-content: space-between;">
                <div class="sub-act-header">ACTIVITY 3</div>
                <span class="act3-date-pill">NOV 26–30, 2026</span>
              </div>
              <div class="sub-lead-name">📍 City Accounting Office</div>
              <div class="sub-act-desc">GAD Employee Development, Recognition and Organizational Strengthening Program.</div>
              <div class="sub-partner-box"><strong>Partners:</strong> COA, Barangays</div>
            </div>
          </div>
        </article>'''

day2_new = '''        <!-- DAY 2 (3 Activities) -->
        <article class="day-card active-day">
          <div class="card-top-bar">
            <span class="day-pill">DAY 2</span>
            <span class="date-text">NOV 26</span>
            <span class="weekday-text">THU</span>
          </div>
          <div class="card-body-3act">
            <!-- Sub 1 -->
            <div class="sub-act-item-3">
              <div class="sub-act-header">ACTIVITY 1</div>
              <div class="sub-lead-name">📍 PESO / COOP / CEDIPO</div>
              <div class="sub-act-desc">Women's economic empowerment, safe employment, anti-trafficking and cyber recruitment scam awareness.</div>
            </div>
            <!-- Sub 2 -->
            <div class="sub-act-item-3">
              <div class="sub-act-header">ACTIVITY 2</div>
              <div class="sub-lead-name">📍 City Agriculture & Cooperative Office</div>
              <div class="sub-act-desc">Rural women protection, livelihood, cooperative support, and community-based prevention.</div>
            </div>
            <!-- Sub 3 (Nov 26–30, 2026) -->
            <div class="sub-act-item-3">
              <div style="display: flex; align-items: center; justify-content: space-between;">
                <div class="sub-act-header">ACTIVITY 3</div>
                <span class="act3-date-pill">NOV 26–30, 2026</span>
              </div>
              <div class="sub-lead-name">📍 City Accounting Office</div>
              <div class="sub-act-desc">GAD Employee Development, Recognition and Organizational Strengthening Program.</div>
            </div>
            <div class="card-partner-box">
              <strong>Partners:</strong> DA, DOLE, DTI, OWWA, COA, Cooperatives, MSMES, Barangays, CSOs, Private Sector
            </div>
            <div class="card-venue-box">
              <svg viewBox="0 0 16 16"><path d="M8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10zm0-7a3 3 0 1 1 0-6 3 3 0 0 1 0 6z"/></svg>
              <span><strong>Venue:</strong> Isabela Convention Center, San Fermin, Cauayan City, Isabela</span>
            </div>
          </div>
        </article>'''

day3_old = '''        <!-- DAY 3 (4 Activities: PDAO & OSCA, GAD Office, CSWDO, City Population Office) -->
        <article class="day-card active-day">
          <div class="card-top-bar">
            <span class="day-pill">DAY 3</span>
            <span class="date-text">NOV 27</span>
            <span class="weekday-text">FRI</span>
          </div>
          <div class="card-body-4act">
            <!-- Sub 1 -->
            <div class="sub-act-item-4">
              <div class="sub-act-header">ACTIVITY 1</div>
              <div class="sub-lead-name">📍 PDAO &amp; OSCA</div>
              <div class="sub-act-desc">Protection of women with disabilities &amp; senior women; inclusive referral and access to support.</div>
              <div class="sub-partner-box"><strong>Partners:</strong> CSWDO, Health Office, PNP</div>
            </div>
            <!-- Sub 2 -->
            <div class="sub-act-item-4">
              <div class="sub-act-header">ACTIVITY 2</div>
              <div class="sub-lead-name">📍 GAD Office</div>
              <div class="sub-act-desc">Namnama (PWD Film Viewing)</div>
              <div class="sub-partner-box"><strong>Partners:</strong> Isabela Artist Club (ISAC), Women with Disabilities Group</div>
            </div>
            <!-- Sub 3 -->
            <div class="sub-act-item-4">
              <div class="sub-act-header">ACTIVITY 3</div>
              <div class="sub-lead-name">📍 CSWDO</div>
              <div style="display: flex; flex-direction: column; gap: 2px;">
                <div class="sub-act-desc">Survivor-centered care management, psychosocial first aid, women and children referral mapping.</div>
                <div style="font-family: \'Montserrat\', sans-serif; font-size: 20px; font-weight: 800; color: #9a3412; background: #ffedd5; border: 1.5px solid #fed7aa; border-radius: 4px; padding: 1px 6px; align-self: flex-start;">Project S.U.N.S.H.I.N.E. M&amp;E</div>
              </div>
              <div class="sub-partner-box"><strong>Partners:</strong> Health Office, PNP-WCPD, NGAs, CSOs, ISAC</div>
            </div>
            <div class="card-venue-box">
              <svg viewBox="0 0 16 16"><path d="M8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10zm0-7a3 3 0 1 1 0-6 3 3 0 0 1 0 6z"/></svg>
              <span><strong>Venue:</strong> F. L. Dy Colliseum, District III, Cauayan City, Isabela</span>
            </div>
            <!-- Sub 4 -->
            <div class="sub-act-item-4">
              <div class="sub-act-header">ACTIVITY 4</div>
              <div class="sub-lead-name">📍 City Population Office</div>
              <div class="sub-act-desc">KABATAAN PRO-TECT (Teen Empowerment and Care Team): Peer Helping Training on Safe Spaces, Mental Health, and ASRH</div>
              <div class="sub-partner-box"><strong>Partners:</strong> City Health Office, Local Youth Development Office, Cauayan City Stand Alone Senior High School</div>
            </div>
            <div class="card-venue-box">
              <svg viewBox="0 0 16 16"><path d="M8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10zm0-7a3 3 0 1 1 0-6 3 3 0 0 1 0 6z"/></svg>
              <span><strong>Venue:</strong> Cauayan City Stand Alone Senior High School</span>
            </div>
          </div>
        </article>'''

day3_new = '''        <!-- DAY 3 (4 Activities: PDAO & OSCA, GAD Office, CSWDO, City Population Office) -->
        <article class="day-card active-day">
          <div class="card-top-bar">
            <span class="day-pill">DAY 3</span>
            <span class="date-text">NOV 27</span>
            <span class="weekday-text">FRI</span>
          </div>
          <div class="card-body-4act">
            <!-- Sub 1 -->
            <div class="sub-act-item-4">
              <div class="sub-act-header">ACTIVITY 1</div>
              <div class="sub-lead-name">📍 PDAO &amp; OSCA</div>
              <div class="sub-act-desc">Protection of women with disabilities &amp; senior women; inclusive referral and access to support.</div>
            </div>
            <!-- Sub 2 -->
            <div class="sub-act-item-4">
              <div class="sub-act-header">ACTIVITY 2</div>
              <div class="sub-lead-name">📍 GAD Office</div>
              <div class="sub-act-desc">Namnama (PWD Film Viewing)</div>
            </div>
            <!-- Sub 3 -->
            <div class="sub-act-item-4">
              <div class="sub-act-header">ACTIVITY 3</div>
              <div class="sub-lead-name">📍 CSWDO</div>
              <div style="display: flex; flex-direction: column; gap: 2px;">
                <div class="sub-act-desc">Survivor-centered care management, psychosocial first aid, women and children referral mapping.</div>
                <div style="font-family: \'Montserrat\', sans-serif; font-size: 20px; font-weight: 800; color: #9a3412; background: #ffedd5; border: 1.5px solid #fed7aa; border-radius: 4px; padding: 1px 6px; align-self: flex-start;">Project S.U.N.S.H.I.N.E. M&amp;E</div>
              </div>
            </div>
            <div class="card-partner-box">
              <strong>Partners:</strong> CSWDO, Health Office, PNP, PNP-WCPD, NGAs, CSOs, ISAC, Women with Disabilities Group
            </div>
            <div class="card-venue-box">
              <svg viewBox="0 0 16 16"><path d="M8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10zm0-7a3 3 0 1 1 0-6 3 3 0 0 1 0 6z"/></svg>
              <span><strong>Venue:</strong> F. L. Dy Colliseum, District III, Cauayan City, Isabela</span>
            </div>
            <!-- Sub 4 -->
            <div class="sub-act-item-4">
              <div class="sub-act-header">ACTIVITY 4</div>
              <div class="sub-lead-name">📍 City Population Office</div>
              <div class="sub-act-desc">KABATAAN PRO-TECT (Teen Empowerment and Care Team): Peer Helping Training on Safe Spaces, Mental Health, and ASRH</div>
            </div>
            <div class="card-partner-box">
              <strong>Partners:</strong> City Health Office, Local Youth Development Office, Cauayan City Stand Alone Senior High School
            </div>
            <div class="card-venue-box">
              <svg viewBox="0 0 16 16"><path d="M8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10zm0-7a3 3 0 1 1 0-6 3 3 0 0 1 0 6z"/></svg>
              <span><strong>Venue:</strong> Cauayan City Stand Alone Senior High School</span>
            </div>
          </div>
        </article>'''

replacements = [
    (css_old, css_new),
    (day1_old, day1_new),
    (day2_old, day2_new),
    (day3_old, day3_new)
]

for fp in ['18-day-campaign-calendar-a3.html', '18-day-campaign-calendar.html']:
    update_file(fp, replacements)
