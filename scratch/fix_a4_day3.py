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

a4_day3_old_real = '''        <!-- DAY 3 (4 Activities: PDAO & OSCA, GAD Office, CSWDO, City Population Office) -->
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

a4_day3_new_real = '''        <!-- DAY 3 (4 Activities: PDAO & OSCA, GAD Office, CSWDO, City Population Office) -->
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
            </div>
            <div class="sub-act-item-4">
              <div class="sub-act-header">ACTIVITY 2</div>
              <div class="sub-lead-name">📍 GAD Office</div>
              <div class="sub-act-desc">Namnama (PWD Film Viewing)</div>
            </div>
            <div class="sub-act-item-4">
              <div class="sub-act-header">ACTIVITY 3</div>
              <div class="sub-lead-name">📍 CSWDO</div>
              <div class="sub-act-desc">Survivor-centered care management, psychosocial first aid, referral mapping. <strong>Project S.U.N.S.H.I.N.E. M&E</strong></div>
            </div>
            <div class="card-partner-box">
              <strong>Partners:</strong> CSWDO, Health Office, PNP, PNP-WCPD, NGAs, CSOs, ISAC, Women with Disabilities Group
            </div>
            <div class="card-venue-box">
              <svg viewBox="0 0 16 16"><path d="M8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10zm0-7a3 3 0 1 1 0-6 3 3 0 0 1 0 6z"/></svg>
              <span><strong>Venue:</strong> F. L. Dy Colliseum, District III</span>
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

for fp in ['18-day-campaign-calendar-a4-page1.html', '18-day-campaign-calendar-a4.html']:
    update_file(fp, [(a4_day3_old_real, a4_day3_new_real)])
