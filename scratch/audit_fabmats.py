import os
import glob
import re
import json

def clean_text(t):
    if not t:
        return ""
    t = re.sub(r'<[^>]+>', ' ', t)
    t = re.sub(r'&amp;', '&', t)
    t = re.sub(r'&ndash;', '–', t)
    t = re.sub(r'&mdash;', '—', t)
    t = re.sub(r'&quot;', '"', t)
    t = re.sub(r'&#39;', "'", t)
    t = re.sub(r'&ldquo;', '“', t)
    t = re.sub(r'&rdquo;', '”', t)
    t = re.sub(r'&bull;', '•', t)
    t = re.sub(r'\s+', ' ', t)
    return t.strip()

# 1. Parse Calendar (18-day-campaign-calendar-a3.html)
with open('18-day-campaign-calendar-a3.html', 'r', encoding='utf-8') as f:
    cal_html = f.read()

# Split calendar by articles
cal_articles = re.findall(r'<article class="day-card[^"]*">(.*?)</article>', cal_html, re.DOTALL)
print(f"Found {len(cal_articles)} articles in calendar.")

calendar_days = {}

for art in cal_articles:
    # check if special title card
    if 'special-title-card' in art or 'special-main-title' in art:
        day_key = "00-pre-campaign"
        date_m = re.search(r'class="special-title-date">([^<]+)<', art)
        title_m = re.search(r'class="special-main-title">([^<]+)<', art)
        sub_m = re.search(r'class="special-sub-implementors">([^<]+)<', art)
        lead_m = re.search(r'class="special-lead-val">([^<]+)<', art)
        partner_m = re.search(r'class="special-partner-row">(.*?)</div>', art, re.DOTALL)
        venue_m = re.search(r'class="special-title-venue">(.*?)</div>', art, re.DOTALL)
        
        calendar_days[day_key] = {
            "day": "PRE-CAMPAIGN",
            "date": clean_text(date_m.group(1)) if date_m else "",
            "title": clean_text(title_m.group(1)) if title_m else "",
            "subtitle": clean_text(sub_m.group(1)) if sub_m else "",
            "lead": clean_text(lead_m.group(1)) if lead_m else "",
            "partners": clean_text(partner_m.group(1)) if partner_m else "",
            "venue": clean_text(venue_m.group(1)) if venue_m else "",
            "raw": art
        }
        continue

    day_pill_m = re.search(r'class="day-pill">([^<]+)<', art)
    date_text_m = re.search(r'class="date-text">([^<]+)<', art)
    weekday_m = re.search(r'class="weekday-text">([^<]+)<', art)
    
    if not day_pill_m:
        continue
    
    dp = clean_text(day_pill_m.group(1))
    # day key e.g. "01-day-01"
    day_num = re.search(r'\d+', dp)
    if day_num:
        num = int(day_num.group(0))
        day_key = f"{num:02d}-day-{num:02d}"
    else:
        day_key = dp
        
    date_str = clean_text(date_text_m.group(1)) if date_text_m else ""
    weekday_str = clean_text(weekday_m.group(1)) if weekday_m else ""
    
    # Partner box
    partner_boxes = re.findall(r'class="[^"]*partner-box[^"]*">(.*?)</div>', art, re.DOTALL)
    partners = " | ".join([clean_text(p) for p in partner_boxes])
    
    # Venue box
    venue_boxes = re.findall(r'class="[^"]*venue-box[^"]*">(.*?)</div>', art, re.DOTALL)
    venues = " | ".join([clean_text(v) for v in venue_boxes])
    
    # Activities
    # check for sub-act-item or single-act-desc
    acts = []
    # multi activities
    sub_items = re.findall(r'class="sub-act-item[^"]*">(.*?)</div>\s*(?=<div class="sub-act-item|<div class="card-partner-box|<div class="card-venue-box|</div>\s*</div>)', art, re.DOTALL)
    if sub_items:
        for si in sub_items:
            h_m = re.search(r'class="sub-act-header">([^<]+)<', si)
            l_m = re.search(r'class="sub-lead-name">([^<]+)<', si)
            d_m = re.search(r'class="sub-act-desc">([^<]+)<', si)
            p_m = re.search(r'class="sub-partner-box">(.*?)</div>', si, re.DOTALL)
            acts.append({
                "header": clean_text(h_m.group(1)) if h_m else "",
                "lead": clean_text(l_m.group(1)) if l_m else "",
                "desc": clean_text(d_m.group(1)) if d_m else "",
                "partner": clean_text(p_m.group(1)) if p_m else ""
            })
    # single act
    single_lead_m = re.search(r'class="single-lead-name">([^<]+)<', art)
    single_desc_m = re.search(r'class="single-act-desc[^"]*">(.*?)</div>', art, re.DOTALL)
    if not single_desc_m:
        single_desc_m = re.search(r'class="single-act-desc[^"]*">(.*?)</p>', art, re.DOTALL)
    if single_lead_m or single_desc_m:
        acts.append({
            "header": "MAIN ACTIVITY",
            "lead": clean_text(single_lead_m.group(1)) if single_lead_m else "",
            "desc": clean_text(single_desc_m.group(1)) if single_desc_m else ""
        })
        
    calendar_days[day_key] = {
        "day_pill": dp,
        "date": f"{date_str} {weekday_str}",
        "partners": partners,
        "venues": venues,
        "activities": acts,
        "raw": art
    }

print(f"Parsed {len(calendar_days)} calendar days: {list(calendar_days.keys())}")

# 2. Parse FABMAT HTMLs (scratch/final_html/*.html)
fabmat_files = sorted(glob.glob('scratch/final_html/*.html'))
fabmats = {}

for fpath in fabmat_files:
    fname = os.path.basename(fpath).replace('.html', '')
    with open(fpath, 'r', encoding='utf-8') as f:
        f_html = f.read()
    
    day_pill_m = re.search(r'class="day-pill">([^<]+)<', f_html)
    date_text_m = re.search(r'class="date-text">([^<]+)<', f_html)
    
    # Detail values (Partner, Venue)
    det_vals = re.findall(r'class="detail-val-col">([^<]+)<', f_html)
    if not det_vals:
        # try multiline or with html tags
        det_vals = re.findall(r'class="detail-val-col">(.*?)</div>', f_html, re.DOTALL)
        det_vals = [clean_text(v) for v in det_vals]
        
    # Activity items
    act_items = re.findall(r'<div class="act-item">(.*?)</div>\s*(?=<div class="act-item"|<div class="bottom-block"|</div>\s*</div>)', f_html, re.DOTALL)
    parsed_acts = []
    for ai in act_items:
        # number
        num_m = re.search(r'class="act-num">([^<]+)<', ai)
        title_m = re.search(r'class="act-title">(.*?)</div>', ai, re.DOTALL)
        lead_m = re.search(r'class="act-lead">(.*?)</div>', ai, re.DOTALL)
        parsed_acts.append({
            "num": clean_text(num_m.group(1)) if num_m else "",
            "title": clean_text(title_m.group(1)) if title_m else "",
            "lead": clean_text(lead_m.group(1)) if lead_m else ""
        })
        
    fabmats[fname] = {
        "day_pill": clean_text(day_pill_m.group(1)) if day_pill_m else "",
        "date": clean_text(date_text_m.group(1)) if date_text_m else "",
        "details": det_vals,
        "activities": parsed_acts,
        "raw": f_html
    }

print(f"Parsed {len(fabmats)} FABMAT files: {list(fabmats.keys())}")

# Compare each day
print("\n" + "="*80)
print("AUDIT COMPARISON BETWEEN CALENDAR AND FABMAT")
print("="*80)

for day_key in sorted(calendar_days.keys()):
    cal = calendar_days[day_key]
    fab = fabmats.get(day_key)
    print(f"\n>>> CHECKING {day_key.upper()} <<<")
    if not fab:
        print(f"  [CRITICAL ERROR] No FABMAT file found for {day_key}!")
        continue
    
    print(f"  Calendar Day/Date: {cal.get('day_pill', cal.get('day'))} | {cal.get('date')}")
    print(f"  FABMAT Day/Date:   {fab.get('day_pill')} | {fab.get('date')}")
    
    # Details (Partners & Venue)
    print(f"  Calendar Partners: {cal.get('partners')}")
    print(f"  Calendar Venue(s): {cal.get('venues', cal.get('venue'))}")
    print(f"  FABMAT Details:    {fab.get('details')}")
    
    # Activities count
    cal_act_count = len(cal.get('activities', []))
    fab_act_count = len(fab.get('activities', []))
    print(f"  Calendar Activity Count: {cal_act_count}")
    print(f"  FABMAT Activity Count:   {fab_act_count}")
    
    if cal_act_count != fab_act_count and day_key != "00-pre-campaign":
        print(f"  [DISCREPANCY: ACTIVITY COUNT] Calendar has {cal_act_count}, FABMAT has {fab_act_count}!")
    
    for i, a in enumerate(cal.get('activities', [])):
        print(f"    [Cal Act {i+1}] Header: {a.get('header')} | Lead: {a.get('lead')}")
        print(f"                   Desc:   {a.get('desc')}")
    for i, a in enumerate(fab.get('activities', [])):
        print(f"    [Fab Act {i+1}] Num:    {a.get('num')} | Lead: {a.get('lead')}")
        print(f"                   Title:  {a.get('title')}")

