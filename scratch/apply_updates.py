import re

def update_a3(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update .grid-7
    content = content.replace(
        'grid-template-columns: 1.00fr 1.22fr 1.26fr 1.18fr 0.94fr 0.68fr 0.98fr;',
        'grid-template-columns: 0.98fr 1.20fr 1.25fr 1.30fr 0.92fr 0.66fr 0.95fr;'
    )

    # 2. Update .card-body-4act CSS
    old_css_4act = '''  /* DAY 15 CARD (4 activities) */
  .card-body-4act {
    padding: 8px 10px;
    display: flex;
    flex-direction: column;
    gap: 6px;
    flex: 1;
    justify-content: space-between;
  }

  .sub-act-item-4 {
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    gap: 4px;
    background: #fffcf8;
    border: 2px solid #fed7aa;
    border-left: 7px solid #ea580c;
    border-radius: 12px;
    padding: 8px 14px;
  }

  .sub-act-item-4 .sub-act-header {
    padding: 3px 10px;
    font-size: 28px;
    border-radius: 5px;
    align-self: flex-start;
  }

  .sub-act-item-4 .sub-lead-name {
    font-size: 31.5px;
    line-height: 1.16;
  }

  .sub-act-item-4 .sub-act-desc {
    font-size: 29.5px;
    line-height: 1.24;
    color: #334155;
    font-weight: 600;
  }

  .sub-act-item-4 .sub-partner-box {
    font-size: 28.5px;
    padding: 5px 12px;
    border-radius: 6px;
    line-height: 1.2;
  }'''

    new_css_4act = '''  /* 4 ACTIVITIES CARD (Day 3 with 2 venues) */
  .card-body-4act {
    padding: 5px 7px;
    display: flex;
    flex-direction: column;
    gap: 3px;
    flex: 1;
    justify-content: space-between;
  }

  .sub-act-item-4 {
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    gap: 2px;
    background: #fffcf8;
    border: 1.8px solid #fed7aa;
    border-left: 6px solid #ea580c;
    border-radius: 9px;
    padding: 4px 9px;
  }

  .sub-act-item-4 .sub-act-header {
    padding: 2px 7px;
    font-size: 23px;
    border-radius: 4px;
    align-self: flex-start;
  }

  .sub-act-item-4 .sub-lead-name {
    font-size: 25.5px;
    font-weight: 800;
    color: #0f172a;
    line-height: 1.12;
  }

  .sub-act-item-4 .sub-act-desc {
    font-size: 22.5px;
    line-height: 1.16;
    color: #334155;
    font-weight: 600;
  }

  .sub-act-item-4 .sub-partner-box {
    font-size: 21.5px;
    padding: 2.5px 7px;
    border-radius: 5px;
    line-height: 1.14;
  }

  .card-body-4act .card-venue-box {
    padding: 3.5px 8px;
    font-size: 22.5px;
    gap: 5px;
    line-height: 1.15;
    border-radius: 7px;
  }

  .card-body-4act .card-venue-box svg {
    width: 20px;
    height: 20px;
  }

  .card-body-4act .card-venue-box strong {
    font-size: 22.5px;
  }'''

    # Normalize newlines for matching
    content = content.replace(old_css_4act.replace('\n', '\r\n'), new_css_4act.replace('\n', '\r\n'))
    if old_css_4act in content:
        content = content.replace(old_css_4act, new_css_4act)

    # 3. Update Pre-campaign card
    old_pre = '''            <div class="special-partner-row">
              <strong>Partners:</strong> DILG, Liga ng mga Barangay
            </div>'''
    new_pre = '''            <div class="special-partner-row">
              <strong>Partners:</strong> DILG, LGU Offices, Liga ng mga Barangay, CCGLO
            </div>'''
    content = content.replace(old_pre.replace('\n', '\r\n'), new_pre.replace('\n', '\r\n'))
    if old_pre in content: content = content.replace(old_pre, new_pre)

    # 4. Update Day 1
    old_d1 = '''              <div class="sub-lead-name">📍 GAD Office & Office of the City Mayor</div>
              <div class="sub-act-desc">Opening Program, Orange Campaign Kickoff, Parade around the City, Policy Call to Action, Project S.U.N.S.H.I.N.E. public launch.</div>
              <div class="sub-partner-box"><strong>Partners:</strong> All City Offices, Barangays, Partners</div>'''
    new_d1 = '''              <div class="sub-lead-name">📍 GAD Office & Office of the City Mayor</div>
              <div class="sub-act-desc">Opening Program, Orange Campaign Kickoff, Parade around the City, Policy Call to Action, Project S.U.N.S.H.I.N.E. public launch.</div>
              <div class="sub-partner-box"><strong>Partners:</strong> All City Offices, Barangays, PNP, BFP, BJMP, Academe, CSOs</div>'''
    content = content.replace(old_d1.replace('\n', '\r\n'), new_d1.replace('\n', '\r\n'))
    if old_d1 in content: content = content.replace(old_d1, new_d1)

    # 5. Update Day 2
    old_d2 = '''              <div class="sub-lead-name">📍 City Agriculture & Cooperative Office</div>
              <div class="sub-act-desc">Rural women protection, livelihood, cooperative support, and community-based prevention.</div>
              <div class="sub-partner-box"><strong>Partners:</strong> DA, Cooperatives, Barangays</div>'''
    new_d2 = '''              <div class="sub-lead-name">📍 City Agriculture & Cooperative Office</div>
              <div class="sub-act-desc">Rural women protection, livelihood, cooperative support, and community-based prevention.</div>
              <div class="sub-partner-box"><strong>Partners:</strong> DA, Cooperatives, MSMES, Barangays, CSOs</div>'''
    content = content.replace(old_d2.replace('\n', '\r\n'), new_d2.replace('\n', '\r\n'))
    if old_d2 in content: content = content.replace(old_d2, new_d2)

    # 6. Update Day 3
    old_d3 = '''        <!-- DAY 3 (3 Activities: PDAO & OSCA, GAD Office, CSWDO) -->
        <article class="day-card active-day">
          <div class="card-top-bar">
            <span class="day-pill">DAY 3</span>
            <span class="date-text">NOV 27</span>
            <span class="weekday-text">FRI</span>
          </div>
          <div class="card-body-3act">
            <!-- Sub 1 -->
            <div class="sub-act-item-3">
              <div class="sub-act-header">ACTIVITY 1</div>
              <div class="sub-lead-name">📍 PDAO &amp; OSCA</div>
              <div class="sub-act-desc">Protection of women with disabilities &amp; senior women; inclusive referral and access to support.</div>
              <div class="sub-partner-box"><strong>Partners:</strong> CSWDO, Health Office, PNP</div>
            </div>
            <!-- Sub 2 (New Activity) -->
            <div class="sub-act-item-3">
              <div class="sub-act-header">ACTIVITY 2</div>
              <div class="sub-lead-name">📍 GAD Office</div>
              <div class="sub-act-desc">Namnama (PWD Film Viewing)</div>
              <div class="sub-partner-box"><strong>Partners:</strong> Isabela Artist Club (ISAC), Women with Disabilities Group</div>
            </div>
            <!-- Sub 3 (Shifted Activity 2) -->
            <div class="sub-act-item-3">
              <div class="sub-act-header">ACTIVITY 3</div>
              <div class="sub-lead-name">📍 CSWDO</div>
              <div style="display: flex; flex-direction: column; gap: 3px;">
                <div class="sub-act-desc">Survivor-centered care management, psychosocial first aid, women and children referral mapping.</div>
                <div style="font-family: 'Montserrat', sans-serif; font-size: 24px; font-weight: 800; color: #9a3412; background: #ffedd5; border: 1.5px solid #fed7aa; border-radius: 5px; padding: 2px 8px; align-self: flex-start;">Project S.U.N.S.H.I.N.E. M&amp;E</div>
              </div>
              <div class="sub-partner-box"><strong>Partners:</strong> Health Office, PNP-WCPD, NGAs, CSOs</div>
            </div>
            <div class="card-venue-box">
              <svg viewBox="0 0 16 16"><path d="M8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10zm0-7a3 3 0 1 1 0-6 3 3 0 0 1 0 6z"/></svg>
              <span><strong>Venue:</strong> F. L. Dy Colliseum, District III, Cauayan City, Isabela</span>
            </div>
          </div>
        </article>'''

    new_d3 = '''        <!-- DAY 3 (4 Activities: PDAO & OSCA, GAD Office, CSWDO, City Population Office) -->
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
                <div style="font-family: 'Montserrat', sans-serif; font-size: 20px; font-weight: 800; color: #9a3412; background: #ffedd5; border: 1.5px solid #fed7aa; border-radius: 4px; padding: 1px 6px; align-self: flex-start;">Project S.U.N.S.H.I.N.E. M&amp;E</div>
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

    content = content.replace(old_d3.replace('\n', '\r\n'), new_d3.replace('\n', '\r\n'))
    if old_d3 in content: content = content.replace(old_d3, new_d3)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filepath}")

update_a3('18-day-campaign-calendar-a3.html')
update_a3('18-day-campaign-calendar.html')

