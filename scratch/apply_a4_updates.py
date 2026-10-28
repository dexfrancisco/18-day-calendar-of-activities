def update_a4(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update p1-grid-row1 grid
    content = content.replace(
        'grid-template-columns: 1.00fr 1.25fr 1.35fr 1.25fr;',
        'grid-template-columns: 0.95fr 1.22fr 1.33fr 1.38fr;'
    )

    # 2. Add .card-body-4act and .sub-act-item-4 CSS
    css_insert = '''  /* 4 ACTIVITIES CARD (Day 3 with 2 venues) */
  .card-body-4act {
    padding: 4px 6px;
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
    border: 1.5px solid #fed7aa;
    border-left: 5px solid #ea580c;
    border-radius: 7px;
    padding: 3px 7px;
  }

  .sub-act-item-4 .sub-act-header {
    background: #ffedd5;
    padding: 1.5px 6px;
    border-radius: 4px;
    font-family: 'Montserrat', sans-serif;
    font-size: 19px;
    font-weight: 900;
    color: #9a3412;
    text-transform: uppercase;
    letter-spacing: 0.3px;
    align-self: flex-start;
  }

  .sub-act-item-4 .sub-lead-name {
    font-size: 21px;
    font-weight: 800;
    color: #0f172a;
    line-height: 1.12;
  }

  .sub-act-item-4 .sub-act-desc {
    font-size: 19px;
    line-height: 1.16;
    color: #334155;
    font-weight: 600;
  }

  .sub-act-item-4 .sub-partner-box {
    background: #fdf4ff;
    border: 1px solid #f0abfc;
    border-radius: 5px;
    padding: 2.5px 6px;
    font-size: 18px;
    color: #701a75;
    font-weight: 700;
    line-height: 1.14;
  }

  .card-body-4act .card-venue-box {
    padding: 3px 6px;
    font-size: 19px;
    gap: 4px;
    line-height: 1.15;
    border-radius: 6px;
  }

  .card-body-4act .card-venue-box svg {
    width: 17px;
    height: 17px;
  }

  .card-body-4act .card-venue-box strong {
    font-size: 19px;
  }

  /* DAY 2 CARD (3 activities) */'''

    content = content.replace(
        '  /* DAY 2 CARD (3 activities) */',
        css_insert.replace('\n', '\r\n')
    )
    if '  /* DAY 2 CARD (3 activities) */' in content:
        content = content.replace('  /* DAY 2 CARD (3 activities) */', css_insert)

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
    old_d1 = '''            <div class="sub-act-item-2">
              <div class="sub-act-header">ACTIVITY 2</div>
              <div class="sub-lead-name">📍 GAD Office & Mayor</div>
              <div class="sub-act-desc">Opening Program, Orange Campaign Kickoff, Orange Run, Policy Call to Action, Project S.U.N.S.H.I.N.E. public launch.</div>
              <div class="sub-partner-box"><strong>Partners:</strong> All City Offices, Barangays, Partners</div>
            </div>'''
    new_d1 = '''            <div class="sub-act-item-2">
              <div class="sub-act-header">ACTIVITY 2</div>
              <div class="sub-lead-name">📍 GAD Office & Mayor</div>
              <div class="sub-act-desc">Opening Program, Orange Campaign Kickoff, Orange Run, Policy Call to Action, Project S.U.N.S.H.I.N.E. public launch.</div>
              <div class="sub-partner-box"><strong>Partners:</strong> All City Offices, Barangays, PNP, BFP, BJMP, Academe, CSOs</div>
            </div>'''
    content = content.replace(old_d1.replace('\n', '\r\n'), new_d1.replace('\n', '\r\n'))
    if old_d1 in content: content = content.replace(old_d1, new_d1)

    # 5. Update Day 2
    old_d2 = '''            <div class="sub-act-item-3">
              <div class="sub-act-header">ACTIVITY 2</div>
              <div class="sub-lead-name">📍 City Agriculture & Cooperative</div>
              <div class="sub-act-desc">Rural women protection, livelihood, cooperative support & community prevention.</div>
              <div class="sub-partner-box"><strong>Partners:</strong> DA, Cooperatives, Barangays</div>
            </div>'''
    new_d2 = '''            <div class="sub-act-item-3">
              <div class="sub-act-header">ACTIVITY 2</div>
              <div class="sub-lead-name">📍 City Agriculture & Cooperative</div>
              <div class="sub-act-desc">Rural women protection, livelihood, cooperative support & community prevention.</div>
              <div class="sub-partner-box"><strong>Partners:</strong> DA, Cooperatives, MSMES, Barangays, CSOs</div>
            </div>'''
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
            <div class="sub-act-item-3">
              <div class="sub-act-header">ACTIVITY 1</div>
              <div class="sub-lead-name">📍 PDAO & OSCA</div>
              <div class="sub-act-desc">Protection of women with disabilities & senior women; inclusive referral and support.</div>
              <div class="sub-partner-box"><strong>Partners:</strong> CSWDO, Health Office, PNP</div>
            </div>
            <div class="sub-act-item-3">
              <div class="sub-act-header">ACTIVITY 2</div>
              <div class="sub-lead-name">📍 GAD Office</div>
              <div class="sub-act-desc">Namnama (PWD Film Viewing)</div>
              <div class="sub-partner-box"><strong>Partners:</strong> Isabela Artist Club (ISAC), Women with Disabilities Group</div>
            </div>
            <div class="sub-act-item-3">
              <div class="sub-act-header">ACTIVITY 3</div>
              <div class="sub-lead-name">📍 CSWDO</div>
              <div class="sub-act-desc">Survivor-centered care management, psychosocial first aid, referral mapping. <strong>Project S.U.N.S.H.I.N.E. M&E</strong></div>
              <div class="sub-partner-box"><strong>Partners:</strong> Health Office, PNP-WCPD, NGAs, CSOs</div>
            </div>
            <div class="card-venue-box">
              <svg viewBox="0 0 16 16"><path d="M8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10zm0-7a3 3 0 1 1 0-6 3 3 0 0 1 0 6z"/></svg>
              <span><strong>Venue:</strong> F. L. Dy Colliseum, District III</span>
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

    content = content.replace(old_d3.replace('\n', '\r\n'), new_d3.replace('\n', '\r\n'))
    if old_d3 in content: content = content.replace(old_d3, new_d3)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filepath}")

update_a4('18-day-campaign-calendar-a4-page1.html')
update_a4('18-day-campaign-calendar-a4.html')

