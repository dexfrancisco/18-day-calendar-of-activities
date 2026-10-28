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

# CSS additions for A3
a3_css_addition = '''  /* SHARED MULTI-ACTIVITY PARTNER BOX (Top of Venue) */
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
    font-size: 21px;
    padding: 3.5px 8px;
    line-height: 1.15;
    border-radius: 6px;
  }
'''

# -----------------
# A3 CARDS
# -----------------

# Day 1 A3
a3_day1_old = '''        <!-- DAY 1 (2 Activities: GAD Office Distribution, Opening & Launch) -->
        <article class="day-card active-day">
          <div class="card-top-bar">
            <span class="day-pill">DAY 1</span>
            <span class="date-text">NOV 25</span>
            <span class="weekday-text">WED</span>
          </div>
          <div class="card-body-multi">
            <div class="sub-act-item-2">
              <div class="sub-act-header">ACTIVITY 1</div>
              <div class="sub-lead-name">📍 GAD Office</div>
              <div class="sub-act-desc">Wellness and Essential Care Distribution for Project S.U.N.S.H.I.N.E Beneficiaries.</div>
              <div class="sub-partner-box"><strong>Partners:</strong> BJMP, PNP, CSWD</div>
            </div>
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

a3_day1_new = '''        <!-- DAY 1 (2 Activities: GAD Office Distribution, Opening & Launch) -->
        <article class="day-card active-day">
          <div class="card-top-bar">
            <span class="day-pill">DAY 1</span>
            <span class="date-text">NOV 25</span>
            <span class="weekday-text">WED</span>
          </div>
          <div class="card-body-multi">
            <div class="sub-act-item-2">
              <div class="sub-act-header">ACTIVITY 1</div>
              <div class="sub-lead-name">📍 GAD Office</div>
              <div class="sub-act-desc">Wellness and Essential Care Distribution for Project S.U.N.S.H.I.N.E Beneficiaries.</div>
            </div>
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

# Day 2 A3
a3_day2_old = '''        <!-- DAY 2 (3 Activities: PESO/COOP, Agriculture, Accounting) -->
        <article class="day-card active-day">
          <div class="card-top-bar">
            <span class="day-pill">DAY 2</span>
            <span class="date-text">NOV 26</span>
            <span class="weekday-text">THU</span>
          </div>
          <div class="card-body-3act">
            <div class="sub-act-item-3">
              <div class="sub-act-header">ACTIVITY 1</div>
              <div class="sub-lead-name">📍 PESO / COOP / CEDIPO</div>
              <div class="sub-act-desc">Women's economic empowerment, safe employment, anti-trafficking and cyber recruitment scam awareness.</div>
              <div class="sub-partner-box"><strong>Partners:</strong> DOLE, OWWA, DTI, Private Sector</div>
            </div>
            <div class="sub-act-item-3">
              <div class="sub-act-header">ACTIVITY 2</div>
              <div class="sub-lead-name">📍 City Agriculture & Cooperative Office</div>
              <div class="sub-act-desc">Rural women protection, livelihood, cooperative support, and community-based prevention.</div>
              <div class="sub-partner-box"><strong>Partners:</strong> DA, Cooperatives, MSMES, Barangays, CSOs</div>
            </div>
            <div class="sub-act-item-3">
              <div style="display: flex; align-items: center; justify-content: space-between; gap: 4px;">
                <span class="sub-act-header">ACTIVITY 3</span>
                <span class="act3-date-pill">NOV 26–30, 2026</span>
              </div>
              <div class="sub-lead-name">📍 City Accounting Office</div>
              <div class="sub-act-desc">GAD Employee Development, Recognition and Organizational Strengthening Program.</div>
              <div class="sub-partner-box"><strong>Partners:</strong> COA, Barangays</div>
            </div>
            <div class="card-venue-box">
              <svg viewBox="0 0 16 16"><path d="M8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10zm0-7a3 3 0 1 1 0-6 3 3 0 0 1 0 6z"/></svg>
              <span><strong>Venue:</strong> Isabela Convention Center, San Fermin, Cauayan City, Isabela</span>
            </div>
          </div>
        </article>'''

a3_day2_new = '''        <!-- DAY 2 (3 Activities: PESO/COOP, Agriculture, Accounting) -->
        <article class="day-card active-day">
          <div class="card-top-bar">
            <span class="day-pill">DAY 2</span>
            <span class="date-text">NOV 26</span>
            <span class="weekday-text">THU</span>
          </div>
          <div class="card-body-3act">
            <div class="sub-act-item-3">
              <div class="sub-act-header">ACTIVITY 1</div>
              <div class="sub-lead-name">📍 PESO / COOP / CEDIPO</div>
              <div class="sub-act-desc">Women's economic empowerment, safe employment, anti-trafficking and cyber recruitment scam awareness.</div>
            </div>
            <div class="sub-act-item-3">
              <div class="sub-act-header">ACTIVITY 2</div>
              <div class="sub-lead-name">📍 City Agriculture & Cooperative Office</div>
              <div class="sub-act-desc">Rural women protection, livelihood, cooperative support, and community-based prevention.</div>
            </div>
            <div class="sub-act-item-3">
              <div style="display: flex; align-items: center; justify-content: space-between; gap: 4px;">
                <span class="sub-act-header">ACTIVITY 3</span>
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

# Day 3 A3 (2 venues)
a3_day3_old = '''        <!-- DAY 3 (4 Activities: PDAO & OSCA, GAD Office, CSWDO, City Population Office) -->
        <article class="day-card active-day">
          <div class="card-top-bar">
            <span class="day-pill">DAY 3</span>
            <span class="date-text">NOV 27</span>
            <span class="weekday-text">FRI</span>
          </div>
          <div class="card-body-4act">
            <div class="sub-act-item-4">
              <div class="sub-act-header">ACTIVITY 1</div>
              <div class="sub-lead-name">📍 PDAO & OSCA</div>
              <div class="sub-act-desc">Protection of women with disabilities & senior women; inclusive referral and support.</div>
              <div class="sub-partner-box"><strong>Partners:</strong> CSWDO, Health Office, PNP</div>
            </div>
            <div class="sub-act-item-4">
              <div class="sub-act-header">ACTIVITY 2</div>
              <div class="sub-lead-name">📍 GAD Office</div>
              <div class="sub-act-desc">Namnama (PWD Film Viewing)</div>
              <div class="sub-partner-box"><strong>Partners:</strong> Isabela Artist Club (ISAC), Women with Disabilities Group</div>
            </div>
            <div class="sub-act-item-4">
              <div class="sub-act-header">ACTIVITY 3</div>
              <div class="sub-lead-name">📍 CSWDO</div>
              <div class="sub-act-desc">Survivor-centered care management, psychosocial first aid, referral mapping. <strong>Project S.U.N.S.H.I.N.E. M&E</strong></div>
              <div class="sub-partner-box"><strong>Partners:</strong> Health Office, PNP-WCPD, NGAs, CSOs, ISAC</div>
            </div>
            <div class="card-venue-box">
              <svg viewBox="0 0 16 16"><path d="M8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10zm0-7a3 3 0 1 1 0-6 3 3 0 0 1 0 6z"/></svg>
              <span><strong>Venue:</strong> F. L. Dy Colliseum, District III</span>
            </div>
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

# Let's check exact venue 1 text in A3: in A3 it is 'F. L. Dy Colliseum, District III, Cauayan City, Isabela'
a3_day3_old_real = '''        <!-- DAY 3 (4 Activities: PDAO & OSCA, GAD Office, CSWDO, City Population Office) -->
        <article class="day-card active-day">
          <div class="card-top-bar">
            <span class="day-pill">DAY 3</span>
            <span class="date-text">NOV 27</span>
            <span class="weekday-text">FRI</span>
          </div>
          <div class="card-body-4act">
            <div class="sub-act-item-4">
              <div class="sub-act-header">ACTIVITY 1</div>
              <div class="sub-lead-name">📍 PDAO & OSCA</div>
              <div class="sub-act-desc">Protection of women with disabilities & senior women; inclusive referral and access to support.</div>
              <div class="sub-partner-box"><strong>Partners:</strong> CSWDO, Health Office, PNP</div>
            </div>
            <div class="sub-act-item-4">
              <div class="sub-act-header">ACTIVITY 2</div>
              <div class="sub-lead-name">📍 GAD Office</div>
              <div class="sub-act-desc">Namnama (PWD Film Viewing)</div>
              <div class="sub-partner-box"><strong>Partners:</strong> Isabela Artist Club (ISAC), Women with Disabilities Group</div>
            </div>
            <div class="sub-act-item-4">
              <div class="sub-act-header">ACTIVITY 3</div>
              <div class="sub-lead-name">📍 CSWDO</div>
              <div class="sub-act-desc">Survivor-centered care management, psychosocial first aid, women and children referral mapping. <strong>Project S.U.N.S.H.I.N.E. M&E</strong></div>
              <div class="sub-partner-box"><strong>Partners:</strong> Health Office, PNP-WCPD, NGAs, CSOs, ISAC</div>
            </div>
            <div class="card-venue-box">
              <svg viewBox="0 0 16 16"><path d="M8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10zm0-7a3 3 0 1 1 0-6 3 3 0 0 1 0 6z"/></svg>
              <span><strong>Venue:</strong> F. L. Dy Colliseum, District III, Cauayan City, Isabela</span>
            </div>
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

a3_day3_new = '''        <!-- DAY 3 (4 Activities: PDAO & OSCA, GAD Office, CSWDO, City Population Office) -->
        <article class="day-card active-day">
          <div class="card-top-bar">
            <span class="day-pill">DAY 3</span>
            <span class="date-text">NOV 27</span>
            <span class="weekday-text">FRI</span>
          </div>
          <div class="card-body-4act">
            <div class="sub-act-item-4">
              <div class="sub-act-header">ACTIVITY 1</div>
              <div class="sub-lead-name">📍 PDAO & OSCA</div>
              <div class="sub-act-desc">Protection of women with disabilities & senior women; inclusive referral and access to support.</div>
            </div>
            <div class="sub-act-item-4">
              <div class="sub-act-header">ACTIVITY 2</div>
              <div class="sub-lead-name">📍 GAD Office</div>
              <div class="sub-act-desc">Namnama (PWD Film Viewing)</div>
            </div>
            <div class="sub-act-item-4">
              <div class="sub-act-header">ACTIVITY 3</div>
              <div class="sub-lead-name">📍 CSWDO</div>
              <div class="sub-act-desc">Survivor-centered care management, psychosocial first aid, women and children referral mapping. <strong>Project S.U.N.S.H.I.N.E. M&E</strong></div>
            </div>
            <div class="card-partner-box">
              <strong>Partners:</strong> CSWDO, Health Office, PNP, PNP-WCPD, NGAs, CSOs, ISAC, Women with Disabilities Group
            </div>
            <div class="card-venue-box">
              <svg viewBox="0 0 16 16"><path d="M8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10zm0-7a3 3 0 1 1 0-6 3 3 0 0 1 0 6z"/></svg>
              <span><strong>Venue:</strong> F. L. Dy Colliseum, District III, Cauayan City, Isabela</span>
            </div>
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

# Day 7 & 8 A3 (DILG first)
a3_day7_old = '''            <div class="single-partner-box">
              <strong>Partners:</strong> HR Office, GAD Office, DILG, CSOs
            </div>'''
a3_day7_new = '''            <div class="single-partner-box">
              <strong>Partners:</strong> DILG, HR Office, GAD Office, CSOs
            </div>'''

# Day 9 A3
a3_day9_old = '''        <!-- DAY 9 -->
        <article class="day-card active-day">
          <div class="card-top-bar">
            <span class="day-pill">DAY 9</span>
            <span class="date-text">DEC 3</span>
            <span class="weekday-text">THU</span>
          </div>
          <div class="card-body-multi">
            <!-- Sub 1 -->
            <div class="sub-act-item-2">
              <div class="sub-act-header">ACTIVITY 1</div>
              <div class="sub-lead-name">📍 GAD Office & MOVE</div>
              <div class="sub-act-desc">Men as allies forum, healthy masculinity, shared responsibility, and prevention of VAWC & online abuse.</div>
              <div class="sub-partner-box"><strong>Partners:</strong> JCI, PNP, BJMP, CDRRMO, BFP, Faith Groups, Youth Groups, Academe, DepEd, MASON, ROTARY Club of Cauayan</div>
            </div>
            <!-- Sub 2 -->
            <div class="sub-act-item-2">
              <div class="sub-act-header">ACTIVITY 2</div>
              <div class="sub-lead-name">📍 CDRRMO / Rescue 922 / Safe Line</div>
              <div class="sub-act-desc">Emergency response simulation, hotline awareness, safety drill, and rapid coordination.</div>
              <div class="sub-partner-box"><strong>Partners:</strong> PNP, BFP, MDRRMO, All Teams, JCI, Academe, DepEd</div>
            </div>
            <div class="card-venue-box">
              <svg viewBox="0 0 16 16"><path d="M8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10zm0-7a3 3 0 1 1 0-6 3 3 0 0 1 0 6z"/></svg>
              <span><strong>Venue:</strong> F. L. Dy Colliseum, District III, Cauayan City, Isabela</span>
            </div>
          </div>
        </article>'''

a3_day9_new = '''        <!-- DAY 9 -->
        <article class="day-card active-day">
          <div class="card-top-bar">
            <span class="day-pill">DAY 9</span>
            <span class="date-text">DEC 3</span>
            <span class="weekday-text">THU</span>
          </div>
          <div class="card-body-multi">
            <!-- Sub 1 -->
            <div class="sub-act-item-2">
              <div class="sub-act-header">ACTIVITY 1</div>
              <div class="sub-lead-name">📍 GAD Office & MOVE</div>
              <div class="sub-act-desc">Men as allies forum, healthy masculinity, shared responsibility, and prevention of VAWC & online abuse.</div>
            </div>
            <!-- Sub 2 -->
            <div class="sub-act-item-2">
              <div class="sub-act-header">ACTIVITY 2</div>
              <div class="sub-lead-name">📍 CDRRMO / Rescue 922 / Safe Line</div>
              <div class="sub-act-desc">Emergency response simulation, hotline awareness, safety drill, and rapid coordination.</div>
            </div>
            <div class="card-partner-box">
              <strong>Partners:</strong> PNP, BFP, BJMP, CDRRMO, MDRRMO, All Teams, JCI, Faith Groups, Youth Groups, Academe, DepEd, MASON, ROTARY Club of Cauayan
            </div>
            <div class="card-venue-box">
              <svg viewBox="0 0 16 16"><path d="M8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10zm0-7a3 3 0 1 1 0-6 3 3 0 0 1 0 6z"/></svg>
              <span><strong>Venue:</strong> F. L. Dy Colliseum, District III, Cauayan City, Isabela</span>
            </div>
          </div>
        </article>'''

# Day 10 A3
a3_day10_old = '''        <!-- DAY 10 -->
        <article class="day-card active-day">
          <div class="card-top-bar">
            <span class="day-pill">DAY 10</span>
            <span class="date-text">DEC 4</span>
            <span class="weekday-text">FRI</span>
          </div>
          <div class="card-body-5act">
            <!-- Sub 1: City Health -->
            <div class="sub-act-item-5">
              <div class="sub-act-header">ACTIVITY 1</div>
              <div class="sub-lead-name">📍 City Health Office</div>
              <div class="sub-act-desc">Health response, mental health, reproductive health, medico-legal awareness, and support services for survivors.</div>
              <div class="sub-partner-box"><strong>Partners:</strong> Hospitals, RHUs, NGOs, Mental Health Partners, BJMP, Barangay Officials</div>
            </div>
            <!-- Sub 2: City Legal -->
            <div class="sub-act-item-5">
              <div class="sub-act-header">ACTIVITY 2</div>
              <div class="sub-lead-name">📍 City Legal Office</div>
              <div class="sub-act-desc">Orientation on RA 9262, Safe Spaces Act, Anti-Trafficking, cyber-related VAWC and online crimes; legal referral pathways.</div>
              <div class="sub-partner-box"><strong>Partners:</strong> City Prosecutor's Office, PNP, DILG, BJMP, Barangay</div>
            </div>
            <!-- Sub 3: PNP -->
            <div class="sub-act-item-5">
              <div class="sub-act-header">ACTIVITY 3</div>
              <div class="sub-lead-name">📍 PNP-WCPD / LCAT-VAWC / BJMP / Justice Sector</div>
              <div class="sub-act-desc">Case documentation, law enforcement coordination, protection procedures, and anti-online exploitation response.</div>
              <div class="sub-partner-box"><strong>Partners:</strong> City Prosecutor's Office, DILG, PNP, PAO</div>
            </div>
            <!-- Sub 4: Liga -->
            <div class="sub-act-item-5">
              <div class="sub-act-header">ACTIVITY 4</div>
              <div class="sub-lead-name">📍 Liga ng mga Barangay / VAW Desks</div>
              <div class="sub-act-desc">Barangay action planning, desk strengthening, community watch, and referral readiness.</div>
              <div class="sub-partner-box"><strong>Partners:</strong> DILG, Barangays, BSWDO, BJMP</div>
            </div>
            <!-- Sub 5: JCD GAD CONNECT and CDRRMO -->
            <div class="sub-act-item-5">
              <div class="sub-act-header">ACTIVITY 5</div>
              <div class="sub-lead-name">📍 JCD GAD CONNECT and CDRRMO</div>
              <div class="sub-act-desc">Digital Safety Day: demo of Project S.U.N.S.H.I.N.E., iReport VAWC, Safe Line, online reporting, cyber safety & digital evidence awareness.</div>
              <div class="sub-partner-box"><strong>Partners:</strong> GAD Office, PNP, Tech Partners, BJMP, JCI, Barangay Officials</div>
            </div>
            <div class="card-venue-box">
              <svg viewBox="0 0 16 16"><path d="M8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10zm0-7a3 3 0 1 1 0-6 3 3 0 0 1 0 6z"/></svg>
              <span><strong>Venue:</strong> F. L. Dy Colliseum, District III, Cauayan City, Isabela</span>
            </div>
          </div>
        </article>'''

a3_day10_new = '''        <!-- DAY 10 -->
        <article class="day-card active-day">
          <div class="card-top-bar">
            <span class="day-pill">DAY 10</span>
            <span class="date-text">DEC 4</span>
            <span class="weekday-text">FRI</span>
          </div>
          <div class="card-body-5act">
            <!-- Sub 1: City Health -->
            <div class="sub-act-item-5">
              <div class="sub-act-header">ACTIVITY 1</div>
              <div class="sub-lead-name">📍 City Health Office</div>
              <div class="sub-act-desc">Health response, mental health, reproductive health, medico-legal awareness, and support services for survivors.</div>
            </div>
            <!-- Sub 2: City Legal -->
            <div class="sub-act-item-5">
              <div class="sub-act-header">ACTIVITY 2</div>
              <div class="sub-lead-name">📍 City Legal Office</div>
              <div class="sub-act-desc">Orientation on RA 9262, Safe Spaces Act, Anti-Trafficking, cyber-related VAWC and online crimes; legal referral pathways.</div>
            </div>
            <!-- Sub 3: PNP -->
            <div class="sub-act-item-5">
              <div class="sub-act-header">ACTIVITY 3</div>
              <div class="sub-lead-name">📍 PNP-WCPD / LCAT-VAWC / BJMP / Justice Sector</div>
              <div class="sub-act-desc">Case documentation, law enforcement coordination, protection procedures, and anti-online exploitation response.</div>
            </div>
            <!-- Sub 4: Liga -->
            <div class="sub-act-item-5">
              <div class="sub-act-header">ACTIVITY 4</div>
              <div class="sub-lead-name">📍 Liga ng mga Barangay / VAW Desks</div>
              <div class="sub-act-desc">Barangay action planning, desk strengthening, community watch, and referral readiness.</div>
            </div>
            <!-- Sub 5: JCD GAD CONNECT and CDRRMO -->
            <div class="sub-act-item-5">
              <div class="sub-act-header">ACTIVITY 5</div>
              <div class="sub-lead-name">📍 JCD GAD CONNECT and CDRRMO</div>
              <div class="sub-act-desc">Digital Safety Day: demo of Project S.U.N.S.H.I.N.E., iReport VAWC, Safe Line, online reporting, cyber safety & digital evidence awareness.</div>
            </div>
            <div class="card-partner-box">
              <strong>Partners:</strong> DILG, PNP, BJMP, City Prosecutor's Office, PAO, Barangays, Barangay Officials, BSWDO, Hospitals, RHUs, NGOs, Mental Health Partners, GAD Office, Tech Partners, JCI
            </div>
            <div class="card-venue-box">
              <svg viewBox="0 0 16 16"><path d="M8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10zm0-7a3 3 0 1 1 0-6 3 3 0 0 1 0 6z"/></svg>
              <span><strong>Venue:</strong> F. L. Dy Colliseum, District III, Cauayan City, Isabela</span>
            </div>
          </div>
        </article>'''

# Day 13 A3
a3_day13_old = '''      <!-- DAY 13 (3 Activities: GAD Office, CPDO / GAD KMS Team, GAD Office) -->
      <article class="day-card active-day">
        <div class="card-top-bar">
          <span class="day-pill">DAY 13</span>
          <span class="date-text">DEC 7</span>
          <span class="weekday-text">MON</span>
        </div>
        <div class="card-body-3act">
          <!-- Sub 1: GAD Office -->
          <div class="sub-act-item-3">
            <div class="sub-act-header">ACTIVITY 1</div>
            <div class="sub-lead-name">📍 GAD Office</div>
            <div class="sub-act-desc">Seminar on Gender Functionality Assessment Tool (GFAST) and Gender Responsiveness LGU (GERL) Assessment Tool.</div>
            <div class="sub-partner-box"><strong>Partners:</strong> DILG, PCW, Province of Isabela GFPS, Cauayan City GFPS</div>
          </div>
          <!-- Sub 2: CPDO / GAD KMS Team -->
          <div class="sub-act-item-3">
            <div class="sub-act-header">ACTIVITY 2</div>
            <div class="sub-lead-name">📍 CPDO / GAD KMS Team</div>
            <div class="sub-act-desc">Data-driven governance, sex-disaggregated data, monitoring dashboards, GERL and accountability tools.</div>
            <div class="sub-partner-box"><strong>Partners:</strong> IT Office, Planning Office, All Offices</div>
          </div>
          <!-- Sub 3: GAD Office -->
          <div class="sub-act-item-3">
            <div class="sub-act-header">ACTIVITY 3</div>
            <div class="sub-lead-name">📍 GAD Office</div>
            <div class="sub-act-desc">Display of Orange Exhibits</div>
          </div>
          <div class="card-venue-box">
            <svg viewBox="0 0 16 16"><path d="M8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10zm0-7a3 3 0 1 1 0-6 3 3 0 0 1 0 6z"/></svg>
            <span><strong>Venue:</strong> Isabela Convention Center, San Fermin, Cauayan City, Isabela</span>
          </div>
        </div>
      </article>'''

a3_day13_new = '''      <!-- DAY 13 (3 Activities: GAD Office, CPDO / GAD KMS Team, GAD Office) -->
      <article class="day-card active-day">
        <div class="card-top-bar">
          <span class="day-pill">DAY 13</span>
          <span class="date-text">DEC 7</span>
          <span class="weekday-text">MON</span>
        </div>
        <div class="card-body-3act">
          <!-- Sub 1: GAD Office -->
          <div class="sub-act-item-3">
            <div class="sub-act-header">ACTIVITY 1</div>
            <div class="sub-lead-name">📍 GAD Office</div>
            <div class="sub-act-desc">Seminar on Gender Functionality Assessment Tool (GFAST) and Gender Responsiveness LGU (GERL) Assessment Tool.</div>
          </div>
          <!-- Sub 2: CPDO / GAD KMS Team -->
          <div class="sub-act-item-3">
            <div class="sub-act-header">ACTIVITY 2</div>
            <div class="sub-lead-name">📍 CPDO / GAD KMS Team</div>
            <div class="sub-act-desc">Data-driven governance, sex-disaggregated data, monitoring dashboards, GERL and accountability tools.</div>
          </div>
          <!-- Sub 3: GAD Office -->
          <div class="sub-act-item-3">
            <div class="sub-act-header">ACTIVITY 3</div>
            <div class="sub-lead-name">📍 GAD Office</div>
            <div class="sub-act-desc">Display of Orange Exhibits</div>
          </div>
          <div class="card-partner-box">
            <strong>Partners:</strong> DILG, PCW, Province of Isabela GFPS, Cauayan City GFPS, IT Office, Planning Office, All Offices
          </div>
          <div class="card-venue-box">
            <svg viewBox="0 0 16 16"><path d="M8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10zm0-7a3 3 0 1 1 0-6 3 3 0 0 1 0 6z"/></svg>
            <span><strong>Venue:</strong> Isabela Convention Center, San Fermin, Cauayan City, Isabela</span>
          </div>
        </div>
      </article>'''

# Day 16 A3
a3_day16_old = '''      <!-- DAY 16 (2 Activities: GAD Office) -->
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
            <span><strong>Venue:</strong> F. L. Dy Colliseum, District III, Cauayan City, Isabela</span>
          </div>
        </div>
      </article>'''

a3_day16_new = '''      <!-- DAY 16 (2 Activities: GAD Office) -->
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
          </div>
          <div class="sub-act-item-2">
            <div class="sub-act-header">ACTIVITY 2</div>
            <div class="sub-lead-name">📍 GAD Office</div>
            <div class="sub-act-desc">Regional Educational Research Conference</div>
          </div>
          <div class="card-partner-box">
            <strong>Partners:</strong> DEPED RO2, SDO Cauayan City, CSOs
          </div>
          <div class="card-venue-box">
            <svg viewBox="0 0 16 16"><path d="M8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10zm0-7a3 3 0 1 1 0-6 3 3 0 0 1 0 6z"/></svg>
            <span><strong>Venue:</strong> F. L. Dy Colliseum, District III, Cauayan City, Isabela</span>
          </div>
        </div>
      </article>'''

a3_replacements = [
    ('  /* VENUE BOX */', a3_css_addition + '  /* VENUE BOX */'),
    (a3_day1_old, a3_day1_new),
    (a3_day2_old, a3_day2_new),
    (a3_day3_old_real, a3_day3_new),
    (a3_day7_old, a3_day7_new),
    (a3_day9_old, a3_day9_new),
    (a3_day10_old, a3_day10_new),
    (a3_day13_old, a3_day13_new),
    (a3_day16_old, a3_day16_new)
]

print("--- Updating A3 Files ---")
update_file('18-day-campaign-calendar-a3.html', a3_replacements)
update_file('18-day-campaign-calendar.html', a3_replacements)
