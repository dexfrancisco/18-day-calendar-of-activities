import re
import html
import os

def clean_text(text):
    if not text:
        return ""
    text = re.sub(r'<[^>]+>', ' ', text)
    text = html.unescape(text)
    return ' '.join(text.split())

def extract_calendar():
    with open('18-day-campaign-calendar-a3.html', 'r', encoding='utf-8') as f:
        content = f.read()

    lines = []
    lines.append("=" * 80)
    lines.append("18-DAY ORANGE CAMPAIGN: CALENDAR OF ACTIVITIES")
    lines.append("18-DAY CAMPAIGN TO END VIOLENCE AGAINST WOMEN AND THEIR CHILDREN")
    lines.append("City Government of Cauayan, Isabela • November 25 – December 12, 2026")
    lines.append('"Project S.U.N.S.H.I.N.E. for Safe, Inclusive and Technology-Responsive Communities"')
    lines.append("=" * 80)
    lines.append("")

    lines.append("=" * 80)
    lines.append("18-DAY ACTIVITY MATRIX (INCLUDING PRE-CAMPAIGN VALIDATION)")
    lines.append("=" * 80)

    # Pre-campaign card
    pre_card = re.search(r'<article class="day-card special-title-card">(.*?)</article>', content, re.DOTALL)
    if pre_card:
        c = pre_card.group(1)
        date_m = re.search(r'<div class="special-title-date">(.*?)</div>', c, re.DOTALL)
        title_m = re.search(r'<div class="special-main-title">(.*?)</div>', c, re.DOTALL)
        sub_m = re.search(r'<div class="special-sub-implementors">(.*?)</div>', c, re.DOTALL)
        lead_m = re.search(r'<span class="special-lead-val">(.*?)</span>', c, re.DOTALL)
        part_m = re.search(r'<div class="special-partner-row">(.*?)</div>', c, re.DOTALL)
        venue_m = re.search(r'<div class="special-title-venue">.*?<span>(.*?)</span>', c, re.DOTALL)
        
        lines.append("-" * 80)
        lines.append("PRE-CAMPAIGN INDEPENDENT VALIDATION")
        lines.append("-" * 80)
        if date_m: lines.append(f"Dates: {clean_text(date_m.group(1))}")
        if title_m: lines.append(f"Title: {clean_text(title_m.group(1))}")
        if sub_m: lines.append(f"Subtitle: {clean_text(sub_m.group(1))}")
        if lead_m: lines.append(f"Lead Office: {clean_text(lead_m.group(1))}")
        if part_m: lines.append(clean_text(part_m.group(1)))
        if venue_m: lines.append(clean_text(venue_m.group(1)))
        lines.append("")

    # Regular day cards
    articles = re.findall(r'<article class="day-card\s+([^"]*)">(.*?)</article>', content, re.DOTALL)

    for cls, body in articles:
        if "special-title-card" in cls:
            continue
        
        day_pill = re.search(r'<span class="day-pill">([^<]+)</span>', body)
        date_text = re.search(r'<span class="date-text">([^<]+)</span>', body)
        weekday_text = re.search(r'<span class="weekday-text">([^<]+)</span>', body)
        
        dp = clean_text(day_pill.group(1)) if day_pill else ""
        dt = clean_text(date_text.group(1)) if date_text else ""
        wt = clean_text(weekday_text.group(1)) if weekday_text else ""
        
        lines.append("-" * 80)
        lines.append(f"{dp} | {dt}, 2026 | {wt}")
        lines.append("-" * 80)
        
        venues = [clean_text(v) for v in re.findall(r'<div class="card-venue-box[^>]*>.*?<span>(.*?)</span>', body, re.DOTALL)]
        card_partners = [clean_text(p) for p in re.findall(r'<div class="card-partner-box[^>]*>(.*?)</div>', body, re.DOTALL)]
        
        # Check if Day 11, 17, 18 hybrid split (has both in-person and online advocacy)
        if "weekend-badge" in body and ("single-lead-block" in body or "single-lead-name" in body):
            lines.append("In-Person Activity:")
            lead_m = re.search(r'<span class="single-lead-name"[^>]*>(.*?)</span>', body, re.DOTALL)
            part_m = re.search(r'<div class="single-partner-box"[^>]*>(.*?)</div>', body, re.DOTALL)
            
            if lead_m: lines.append(f"  Lead Office: {clean_text(lead_m.group(1))}")
            
            acts = re.findall(r'<p class="single-act-desc[^"]*"[^>]*>(.*?)</p>', body, re.DOTALL)
            badges = re.findall(r'<span class="act-tag-badge"[^>]*>(.*?)</span>', body, re.DOTALL)
            if len(acts) > 1:
                for a_idx, act_text in enumerate(acts, 1):
                    lbl = clean_text(badges[a_idx-1]) if a_idx-1 < len(badges) else f"Activity {a_idx}"
                    lines.append(f"  {lbl}: {clean_text(act_text)}")
            elif len(acts) == 1:
                lines.append(f"  Main Activity: {clean_text(acts[0])}")

            if part_m: lines.append(f"  {clean_text(part_m.group(1))}")
            for v in venues: lines.append(f"  {v}")
            
            lines.append("Online Activity:")
            lines.append("  Advocacy Track: ONLINE ADVOCACY")
            adv_text_m = re.search(r'<div class="weekend-advocacy-text"[^>]*>(.*?)</div>', body, re.DOTALL)
            if adv_text_m:
                lines.append(f"  Description: {clean_text(adv_text_m.group(1))}")
                
        elif "card-body-single" in body:
            lead_m = re.search(r'<span class="single-lead-name"[^>]*>(.*?)</span>', body, re.DOTALL)
            act_m = re.search(r'<p class="single-act-desc[^"]*"[^>]*>(.*?)</p>', body, re.DOTALL)
            part_m = re.search(r'<div class="single-partner-box"[^>]*>(.*?)</div>', body, re.DOTALL)
            badge_m = re.search(r'<div style="[^"]*background: #ffedd5;[^"]*">(.*?)</div>', body, re.DOTALL)
            
            if lead_m: lines.append(f"Lead Office: {clean_text(lead_m.group(1))}")
            if act_m: lines.append(f"Main Activity: {clean_text(act_m.group(1))}")
            if badge_m: lines.append(f"Special Badge / Event: {clean_text(badge_m.group(1))}")
            if part_m: lines.append(clean_text(part_m.group(1)))
            for v in venues: lines.append(v)
            
        elif "card-body-weekend" in body:
            lines.append("Advocacy Track: ONLINE ADVOCACY")
            adv_text_m = re.search(r'<div class="weekend-advocacy-text"[^>]*>(.*?)</div>', body, re.DOTALL)
            if adv_text_m:
                lines.append(f"Description: {clean_text(adv_text_m.group(1))}")
                
        elif dp == "DAY 3":
            # Day 3 specifically with 4 activities and 2 venues & 2 partner boxes
            for act_num in range(1, 5):
                act_block_m = re.search(rf'<div class="sub-act-item-4">.*?ACTIVITY {act_num}</div>(.*?)</div>\s*(?=<div class="(?:sub-act-item-4|card-partner-box|card-venue-box)|</div>\s*</article>)', body, re.DOTALL)
                if act_block_m:
                    sub_content = act_block_m.group(1)
                    lead_m = re.search(r'<div class="sub-lead-name">(.*?)</div>', sub_content, re.DOTALL)
                    desc_m = re.search(r'<div class="sub-act-desc">(.*?)</div>', sub_content, re.DOTALL)
                    
                    lines.append(f"Activity {act_num}:")
                    if lead_m: lines.append(f"  Lead Office: {clean_text(lead_m.group(1)).replace('📍', '').strip()}")
                    if desc_m: lines.append(f"  Description: {clean_text(desc_m.group(1))}")
                
                # Check partners & venue after act 3 and act 4
                if act_num == 3:
                    if len(card_partners) >= 1:
                        lines.append(f"Partners (Activities 1, 2, 3): {card_partners[0].replace('Partners:', '').strip()}")
                    if len(venues) >= 1:
                        lines.append(f"Venue (Activities 1, 2, 3): {venues[0].replace('Venue:', '').strip()}")
                elif act_num == 4:
                    if len(card_partners) >= 2:
                        lines.append(f"Partners (Activity 4): {card_partners[1].replace('Partners:', '').strip()}")
                    if len(venues) >= 2:
                        lines.append(f"Venue (Activity 4): {venues[1].replace('Venue:', '').strip()}")
        else:
            # Multi-activity cards (Day 1, 2, 9, 10, 13, 16)
            sub_items = re.findall(r'<div class="(?:sub-act-item-\d+|sub-act-item)">.*?<div class="sub-act-header">(.*?)</div>(.*?)(?=<div class="(?:sub-act-item|\bcard-partner-box\b|\bcard-venue-box\b)|$)', body, re.DOTALL)
            for idx, (header, sub_content) in enumerate(sub_items, 1):
                date_pill = re.search(r'<span class="act3-date-pill">(.*?)</span>', sub_content, re.DOTALL)
                dp_str = f" ({clean_text(date_pill.group(1))})" if date_pill else ""
                lead_m = re.search(r'<div class="sub-lead-name">(.*?)</div>', sub_content, re.DOTALL)
                desc_m = re.search(r'<div class="sub-act-desc">(.*?)</div>', sub_content, re.DOTALL)
                spec_init = re.search(r'<div style="[^"]*background: #ffedd5;[^"]*">(.*?)</div>', sub_content, re.DOTALL)
                
                lines.append(f"Activity {idx}{dp_str}:")
                if lead_m: lines.append(f"  Lead Office: {clean_text(lead_m.group(1)).replace('📍', '').strip()}")
                if desc_m: lines.append(f"  Description: {clean_text(desc_m.group(1))}")
                if spec_init: lines.append(f"  Special Initiative: {clean_text(spec_init.group(1))}")
            
            for p in card_partners:
                lines.append(p)
            for v in venues:
                lines.append(v)
                
        lines.append("")

    return "\n".join(lines)

if __name__ == '__main__':
    result = extract_calendar()
    with open('18-Day_Campaign_Calendar_Extracted_Text.txt', 'w', encoding='utf-8') as f:
        f.write(result)
    with open('Final Copy/18-Day_Campaign_Calendar_Extracted_Text.txt', 'w', encoding='utf-8') as f:
        f.write(result)
    print("Updated 18-Day_Campaign_Calendar_Extracted_Text.txt and Final Copy/")
