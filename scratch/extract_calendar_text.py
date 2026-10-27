import re
import html

with open('18-day-campaign-calendar-a3.html', 'r', encoding='utf-8') as f:
    content = f.read()

def clean(text):
    text = re.sub(r'<[^>]+>', ' ', text)
    text = html.unescape(text)
    return ' '.join(text.split())

# Parse articles using regex pattern
articles = re.findall(r'<article class="day-card\s+([^"]*)">(.*?)</article>', content, re.DOTALL)
print(f"Total articles found: {len(articles)}")

for cls, body in articles:
    day_pill = re.search(r'<span class="day-pill">([^<]+)</span>', body)
    date_text = re.search(r'<span class="date-text">([^<]+)</span>', body)
    weekday_text = re.search(r'<span class="weekday-text">([^<]+)</span>', body)
    
    if not day_pill:
        if "special-title-card" in cls:
            print("\n[SPECIAL PRE-CAMPAIGN CARD]")
            print("  Title:", clean(re.search(r'<div class="special-main-title">([^<]+)</div>', body).group(1)))
        continue
        
    dp = clean(day_pill.group(1))
    dt = clean(date_text.group(1))
    wt = clean(weekday_text.group(1))
    print(f"\n{'='*20} {dp} | {dt} | {wt} {'='*20}")
    
    venue_m = re.search(r'<div class="card-venue-box">.*?<span>(.*?)</span>', body, re.DOTALL)
    venue = clean(venue_m.group(1)) if venue_m else ""
    
    if "card-body-single" in body:
        lead_m = re.search(r'<span class="single-lead-name">(.*?)</span>', body, re.DOTALL)
        lead = clean(lead_m.group(1)) if lead_m else ""
        desc_m = re.search(r'<p class="single-act-desc[^"]*">(.*?)</p>', body, re.DOTALL)
        desc = clean(desc_m.group(1)) if desc_m else ""
        part_m = re.search(r'<div class="single-partner-box">(.*?)</div>', body, re.DOTALL)
        part = clean(part_m.group(1)) if part_m else ""
        
        # Check special event inside single act (e.g. Day 14)
        sp_event_m = re.search(r'<div class="special-event-badge">(.*?)</div>', body, re.DOTALL)
        sp_event = clean(sp_event_m.group(1)) if sp_event_m else ""
        
        print(f"  Lead Office: {lead}")
        print(f"  Main Activity: {desc}")
        if sp_event:
            print(f"  Special Event: {sp_event}")
        print(f"  Partners: {part}")
        if venue:
            print(f"  Venue: {venue}")
            
    elif "weekend-advocacy-day" in cls or "advocacy-content" in body:
        # Check if in-person + online (Day 11, 17, 18) or purely online (Day 5, 12)
        # Check if there is an in-person block
        in_person_lead = re.search(r'<div class="weekend-lead-title">\s*<span>(.*?)</span>', body, re.DOTALL)
        in_person_act = re.search(r'<div class="weekend-act-title">\s*<span>(.*?)</span>', body, re.DOTALL)
        in_person_venue = re.search(r'<div class="weekend-venue-box">.*?<span>(.*?)</span>', body, re.DOTALL)
        in_person_part = re.search(r'<div class="weekend-partner-box">(.*?)</div>', body, re.DOTALL)
        
        if in_person_lead or in_person_act:
            print("  In-Person Activity:")
            if in_person_lead:
                print(f"    Lead Office: {clean(in_person_lead.group(1))}")
            if in_person_act:
                print(f"    Main Activity: {clean(in_person_act.group(1))}")
            if in_person_part:
                print(f"    Partners: {clean(in_person_part.group(1))}")
            if in_person_venue:
                print(f"    Venue: {clean(in_person_venue.group(1))}")
            print("  Online Activity:")
        
        adv_badge = re.search(r'<div class="advocacy-badge">([^<]+)</div>', body)
        adv = clean(adv_badge.group(1)) if adv_badge else "ONLINE ADVOCACY"
        adv_desc = re.search(r'<div class="advocacy-desc">(.*?)</div>', body, re.DOTALL)
        desc = clean(adv_desc.group(1)) if adv_desc else ""
        print(f"    Advocacy Track: {adv}")
        print(f"    Description: {desc}")
        
    else:
        # Multi activity cards
        items = re.findall(r'<div class="(?:sub-act-item-\d+|sub-act-item)">(.*?)</div>\s*(?=(?:<div class="(?:sub-act-item|\bcard-venue-box\b)|$))', body, re.DOTALL)
        for idx, it in enumerate(items, 1):
            hdr_m = re.search(r'<div class="sub-act-header">([^<]+)</div>', it)
            hdr = clean(hdr_m.group(1)) if hdr_m else f"Activity {idx}"
            date_pill = re.search(r'<span class="act3-date-pill">([^<]+)</span>', it)
            dp_str = f" (Dates: {clean(date_pill.group(1))})" if date_pill else ""
            lead_m = re.search(r'<div class="sub-lead-name">([^<]+)</div>', it)
            lead = clean(lead_m.group(1)).replace("📍", "").strip() if lead_m else ""
            desc_m = re.search(r'<div class="sub-act-desc">([^<]+)</div>', it)
            desc = clean(desc_m.group(1)) if desc_m else ""
            part_m = re.search(r'<div class="sub-partner-box">(.*?)</div>', it, re.DOTALL)
            part = clean(part_m.group(1)) if part_m else ""
            
            # Special initiative like Day 3 Project SUNSHINE M&E
            sp_init = re.search(r'Project S\.U\.N\.S\.H\.I\.N\.E\. Monitoring and Evaluation', it)
            
            print(f"  Activity {idx}{dp_str}:")
            print(f"    Lead Office: {lead}")
            print(f"    Description: {desc}")
            if sp_init:
                print("    Special Initiative: Project S.U.N.S.H.I.N.E. Monitoring and Evaluation")
            print(f"    Partners: {part}")
        if venue:
            print(f"  Venue: {venue}")
