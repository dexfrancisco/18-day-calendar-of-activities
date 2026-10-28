import os
import re
import subprocess

def apply_a3_improvements():
    with open('18-day-campaign-calendar-a3.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Remove pillars-grid
    pillars_regex = r'  <!-- TOP 4 PILLARS -->\s*<section class="pillars-grid">.*?</section>\s*'
    if re.search(pillars_regex, content, re.DOTALL):
        content = re.sub(pillars_regex, '', content, flags=re.DOTALL)
        print("Removed pillars-grid from A3 HTML.")
    else:
        print("WARNING: pillars-grid not found in A3 HTML!")

    # 2. Update Day 18 to include both Display of Orange Exhibits and Posting of Accomplishment Reports
    day18_old_regex = r'      <!-- DAY 18 -->.*?</article>'
    day18_new = '''      <!-- DAY 18 -->
      <article class="day-card active-day">
        <div class="card-top-bar">
          <span class="day-pill">DAY 18</span>
          <span class="date-text">DEC 12</span>
          <span class="weekday-text">SAT</span>
        </div>
        <div style="padding: 12px 14px; display: flex; flex-direction: column; gap: 10px; flex: 1; justify-content: space-between;">
          <!-- TOP: GAD In-Person Activities -->
          <div style="flex: 1.15; display: flex; flex-direction: column; justify-content: space-between; gap: 6px;">
            <div class="single-lead-block" style="padding: 6px 12px; gap: 3px;">
              <span class="lead-tag-row" style="font-size: 26px;">
                <svg viewBox="0 0 16 16" style="width: 22px; height: 22px;"><path d="M8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10zm0-7a3 3 0 1 1 0-6 3 3 0 0 1 0 6z"/></svg>
                LEAD OFFICE
              </span>
              <span class="single-lead-name" style="font-size: 34px;">GAD Office</span>
            </div>
            <div class="single-act-block" style="padding: 8px 12px; gap: 3px;">
              <span class="act-tag-badge" style="font-size: 22px; padding: 2px 10px;">ACTIVITY 1</span>
              <p class="single-act-desc" style="font-size: 29px; line-height: 1.22; font-weight: 700;">Display of Orange Exhibits</p>
            </div>
            <div class="single-act-block" style="padding: 8px 12px; gap: 3px;">
              <span class="act-tag-badge" style="font-size: 22px; padding: 2px 10px;">ACTIVITY 2</span>
              <p class="single-act-desc" style="font-size: 27px; line-height: 1.20; font-weight: 700;">Posting of Accomplishment Reports for the 18-day Campaign</p>
            </div>
          </div>

          <!-- BOTTOM: Online Advocacy -->
          <div style="flex: 0.85; background: radial-gradient(circle at center, #fffaf5 0%, #ffffff 100%); border: 2.5px solid #fed7aa; border-radius: 14px; padding: 14px 14px; display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; gap: 10px;">
            <div style="width: 68px; height: 68px; border-radius: 50%; background: #ffedd5; border: 3px solid #fdba74; display: flex; align-items: center; justify-content: center; box-shadow: 0 4px 12px rgba(234, 88, 12, 0.12);">
              <svg viewBox="0 0 24 24" style="width: 36px; height: 36px; fill: #ea580c;"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 14.5v-9l6 4.5-6 4.5z"/></svg>
            </div>
            <div class="weekend-badge" style="font-size: 26px; padding: 5px 22px;">ONLINE ADVOCACY</div>
            <div class="weekend-advocacy-text" style="font-size: 28px; line-height: 1.35;">Posting of Advocacy Videos, Safe Spaces Pledges Videos and Advocacy Posters</div>
          </div>
        </div>
      </article>'''

    content = re.sub(day18_old_regex, day18_new, content, flags=re.DOTALL)
    print("Updated Day 18 in A3.")

    # 3. Readjust CSS parameters
    # Header margin
    content = content.replace('margin-bottom: 14px;\n    z-index: 5;\n    padding: 0 40px;', 'margin-bottom: 20px;\n    z-index: 5;\n    padding: 0 40px;')
    # Calendar main gap
    content = content.replace('flex-direction: column;\n    gap: 14px;\n    flex: 1;', 'flex-direction: column;\n    gap: 18px;\n    flex: 1;')
    # Month header bar
    content = content.replace('font-size: 28px;\n    font-weight: 900;\n    letter-spacing: 2px;\n    padding: 7px 24px;', 'font-size: 32px;\n    font-weight: 900;\n    letter-spacing: 2.5px;\n    padding: 9px 28px;')
    # Month header bar svg
    content = content.replace('width: 24px;\n    height: 24px;', 'width: 28px;\n    height: 28px;')

    # Day 3 CSS improvements
    old_day3_css = '''.card-body-4act {
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
    gap: 1.5px;
    background: #fffcf8;
    border: 1.8px solid #fed7aa;
    border-left: 5px solid #ea580c;
    border-radius: 8px;
    padding: 4px 7px;
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

    new_day3_css = '''.card-body-4act {
    padding: 7px 9px;
    display: flex;
    flex-direction: column;
    gap: 4.5px;
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
    padding: 5px 9px;
  }

  .sub-act-item-4 .sub-act-header {
    padding: 2px 8px;
    font-size: 24.5px;
    border-radius: 5px;
    align-self: flex-start;
  }

  .sub-act-item-4 .sub-lead-name {
    font-size: 28px;
    font-weight: 800;
    color: #0f172a;
    line-height: 1.15;
  }

  .sub-act-item-4 .sub-act-desc {
    font-size: 25px;
    line-height: 1.20;
    color: #334155;
    font-weight: 600;
  }

  .sub-act-item-4 .sub-partner-box {
    font-size: 23px;
    padding: 3px 8px;
    border-radius: 5px;
    line-height: 1.16;
  }

  .card-body-4act .card-venue-box {
    padding: 5px 10px;
    font-size: 24.5px;
    gap: 6px;
    line-height: 1.18;
    border-radius: 8px;
  }

  .card-body-4act .card-venue-box svg {
    width: 22px;
    height: 22px;
  }

  .card-body-4act .card-venue-box strong {
    font-size: 24px;
  }'''

    content = content.replace(old_day3_css, new_day3_css)

    # Day 3 partner box in card-partner-box
    content = content.replace(
        '.card-body-4act .card-partner-box {\n    font-size: 20px;\n    padding: 3px 8px;\n    line-height: 1.15;\n    border-radius: 6px;\n  }',
        '.card-body-4act .card-partner-box {\n    font-size: 22px;\n    padding: 4.5px 9px;\n    line-height: 1.18;\n    border-radius: 7px;\n  }'
    )

    # Day 10 CSS improvements
    content = content.replace(
        '.card-body-5act {\n    padding: 6px 10px;\n    display: flex;\n    flex-direction: column;\n    gap: 4px;\n    flex: 1;\n    justify-content: space-between;\n  }',
        '.card-body-5act {\n    padding: 7px 11px;\n    display: flex;\n    flex-direction: column;\n    gap: 5px;\n    flex: 1;\n    justify-content: space-between;\n  }'
    )
    content = content.replace(
        '.sub-act-item-5 .sub-lead-name {\n    font-size: 30px;\n    line-height: 1.15;\n  }',
        '.sub-act-item-5 .sub-lead-name {\n    font-size: 31px;\n    line-height: 1.15;\n  }'
    )
    content = content.replace(
        '.sub-act-item-5 .sub-act-desc {\n    font-size: 28px;\n    line-height: 1.22;\n    color: #334155;\n    font-weight: 600;\n  }',
        '.sub-act-item-5 .sub-act-desc {\n    font-size: 28.5px;\n    line-height: 1.20;\n    color: #334155;\n    font-weight: 600;\n  }'
    )
    content = content.replace(
        '.card-body-5act .card-partner-box {\n    font-size: 23px;\n    padding: 5px 10px;\n    line-height: 1.18;\n  }',
        '.card-body-5act .card-partner-box {\n    font-size: 24.5px;\n    padding: 6px 11px;\n    line-height: 1.18;\n  }'
    )

    # Multi-activity general improvements (Day 1, 9, 16)
    content = content.replace(
        '.sub-act-item-2 .sub-lead-name {\n    font-size: 31.5px;\n    font-weight: 800;\n    color: #0f172a;\n    line-height: 1.18;\n  }',
        '.sub-act-item-2 .sub-lead-name {\n    font-size: 33px;\n    font-weight: 800;\n    color: #0f172a;\n    line-height: 1.18;\n  }'
    )
    content = content.replace(
        '.sub-act-item-2 .sub-act-desc {\n    font-size: 29px;\n    line-height: 1.26;\n    color: #334155;\n    font-weight: 600;\n  }',
        '.sub-act-item-2 .sub-act-desc {\n    font-size: 30px;\n    line-height: 1.26;\n    color: #334155;\n    font-weight: 600;\n  }'
    )

    # Single cards (Day 4, 6, 7, 8, 14, 15)
    content = content.replace(
        '.single-lead-name {\n    font-size: 34px;\n    font-weight: 800;\n    color: #0f172a;\n    line-height: 1.16;\n  }',
        '.single-lead-name {\n    font-size: 36px;\n    font-weight: 800;\n    color: #0f172a;\n    line-height: 1.16;\n  }'
    )
    content = content.replace(
        '.single-act-desc {\n    font-size: 31.5px;\n    line-height: 1.34;\n    color: #1e293b;\n    font-weight: 700;\n  }',
        '.single-act-desc {\n    font-size: 33px;\n    line-height: 1.35;\n    color: #1e293b;\n    font-weight: 700;\n  }'
    )

    # Save to both A3 files
    with open('18-day-campaign-calendar-a3.html', 'w', encoding='utf-8', newline='') as f:
        f.write(content)
    with open('18-day-campaign-calendar.html', 'w', encoding='utf-8', newline='') as f:
        f.write(content)

    print("Updated 18-day-campaign-calendar-a3.html and 18-day-campaign-calendar.html")

apply_a3_improvements()

