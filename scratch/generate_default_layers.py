import json
import os

with open("scratch/schedule_data.json", "r", encoding="utf-8") as f:
    schedule_data = json.load(f)

# Build a dictionary of default layers for each day
days_layers = {}

for day in schedule_data:
    day_id = day["id"]
    badge = day["badge"]
    date_str = day["date_str"]
    icon_file = day.get("icon_filename", "PRE-CAMPAIGN.png")
    layout = day.get("layout_type")

    layers = []

    # 1. Background layer (locked)
    layers.append({
        "id": f"bg_{day_id}",
        "name": "Background Template",
        "type": "background",
        "x": 0,
        "y": 0,
        "width": 2480,
        "height": 3508,
        "src": "FABMAT/fabmat_template.png",
        "locked": True,
        "visible": True,
        "opacity": 1.0
    })

    # 2. Hero Icon layer
    # Determine icon size based on layout
    icon_w = 640
    if layout in ["pre_campaign", "single_activity", "online_only"]:
        icon_w = 720
    elif layout == "standard_activities":
        num_acts = len(day.get("activities", []))
        icon_w = 640 if num_acts <= 2 else 540
    elif layout in ["day3_dual_group", "hybrid_inperson_online", "day18_hybrid"]:
        icon_w = 520

    layers.append({
        "id": f"icon_{day_id}",
        "name": f"Hero Icon ({badge})",
        "type": "image",
        "x": 190,
        "y": 1310,
        "width": icon_w,
        "height": icon_w,
        "src": f"icons/{icon_file}",
        "locked": False,
        "visible": True,
        "opacity": 1.0
    })

    # 3. Day Badge
    badge_x = 190 + icon_w + 50
    badge_w = 2290 - badge_x
    layers.append({
        "id": f"badge_{day_id}",
        "name": "Day Badge",
        "type": "text",
        "x": badge_x,
        "y": 1420,
        "width": badge_w,
        "height": "auto",
        "text": badge,
        "fontFamily": "Gotham Ultra",
        "fontSize": 140,
        "lineHeight": 1.0,
        "color": "#FFFFFF",
        "strokeColor": "#FF6D00",
        "strokeWidth": 22,
        "textAlign": "left",
        "textTransform": "uppercase",
        "locked": False,
        "visible": True,
        "opacity": 1.0
    })

    # 4. Date Line
    layers.append({
        "id": f"date_{day_id}",
        "name": "Date Line",
        "type": "text",
        "x": badge_x,
        "y": 1580,
        "width": badge_w,
        "height": "auto",
        "text": date_str,
        "fontFamily": "Gotham Bold",
        "fontSize": 64,
        "lineHeight": 1.15,
        "color": "#FFFFFF",
        "strokeColor": "#FF6D00",
        "strokeWidth": 14,
        "textAlign": "left",
        "textTransform": "uppercase",
        "locked": False,
        "visible": True,
        "opacity": 1.0
    })

    # 5. Activities & Content based on layout type
    if layout == "pre_campaign":
        layers.append({
            "id": f"title_{day_id}",
            "name": "Main Title",
            "type": "text",
            "x": 190,
            "y": 1960,
            "width": 2100,
            "height": "auto",
            "text": day["title"],
            "fontFamily": "Gotham Ultra",
            "fontSize": 104,
            "lineHeight": 1.16,
            "color": "#FFFFFF",
            "strokeColor": "#FF6D00",
            "strokeWidth": 20,
            "textAlign": "center",
            "textTransform": "none",
            "locked": False,
            "visible": True,
            "opacity": 1.0
        })
        layers.append({
            "id": f"subtitle_{day_id}",
            "name": "Subtitle",
            "type": "text",
            "x": 190,
            "y": 2240,
            "width": 2100,
            "height": "auto",
            "text": day["subtitle"],
            "fontFamily": "Gotham Medium Italic",
            "fontSize": 72,
            "lineHeight": 1.15,
            "color": "#FFFFFF",
            "strokeColor": "#FF6D00",
            "strokeWidth": 14,
            "textAlign": "center",
            "textTransform": "none",
            "locked": False,
            "visible": True,
            "opacity": 1.0
        })
        layers.append({
            "id": f"lead_{day_id}",
            "name": "Lead Office",
            "type": "text",
            "x": 190,
            "y": 2440,
            "width": 2100,
            "height": "auto",
            "text": f"LEAD OFFICE:  {day['lead_office']}",
            "fontFamily": "Gotham Bold",
            "fontSize": 52,
            "lineHeight": 1.15,
            "color": "#FFFFFF",
            "strokeColor": "#FF6D00",
            "strokeWidth": 12,
            "textAlign": "left",
            "textTransform": "none",
            "locked": False,
            "visible": True,
            "opacity": 1.0
        })

    elif layout == "single_activity":
        title_text = day.get("title") or day.get("main_activity", "")
        fsize = 88 if len(title_text) > 80 else 104
        layers.append({
            "id": f"title_{day_id}",
            "name": "Main Activity Title",
            "type": "text",
            "x": 190,
            "y": 1960,
            "width": 2100,
            "height": "auto",
            "text": title_text,
            "fontFamily": "Gotham Ultra",
            "fontSize": fsize,
            "lineHeight": 1.16,
            "color": "#FFFFFF",
            "strokeColor": "#FF6D00",
            "strokeWidth": 20,
            "textAlign": "center",
            "textTransform": "none",
            "locked": False,
            "visible": True,
            "opacity": 1.0
        })
        if day.get("special_badge"):
            layers.append({
                "id": f"special_{day_id}",
                "name": "Special Badge",
                "type": "text",
                "x": 190,
                "y": 2220,
                "width": 2100,
                "height": "auto",
                "text": day["special_badge"],
                "fontFamily": "Gotham Bold",
                "fontSize": 62,
                "lineHeight": 1.15,
                "color": "#FFFFFF",
                "strokeColor": "#FF6D00",
                "strokeWidth": 14,
                "textAlign": "center",
                "textTransform": "uppercase",
                "locked": False,
                "visible": True,
                "opacity": 1.0
            })
        if day.get("lead_office"):
            layers.append({
                "id": f"lead_{day_id}",
                "name": "Lead Office",
                "type": "text",
                "x": 190,
                "y": 2380,
                "width": 2100,
                "height": "auto",
                "text": f"LEAD OFFICE:  {day['lead_office']}",
                "fontFamily": "Gotham Bold",
                "fontSize": 52,
                "lineHeight": 1.15,
                "color": "#FFFFFF",
                "strokeColor": "#FF6D00",
                "strokeWidth": 12,
                "textAlign": "left",
                "textTransform": "none",
                "locked": False,
                "visible": True,
                "opacity": 1.0
            })

    elif layout == "standard_activities":
        acts = day.get("activities", [])
        start_y = 1940
        spacing = 310 if len(acts) == 2 else 240
        fsize = 68 if len(acts) == 2 else 56
        for i, act in enumerate(acts):
            curr_y = start_y + (i * spacing)
            layers.append({
                "id": f"act_{day_id}_{i+1}",
                "name": f"Activity {i+1} Title",
                "type": "text",
                "x": 190,
                "y": curr_y,
                "width": 2100,
                "height": "auto",
                "text": f"{act['num']}. {act['description']}",
                "fontFamily": "Gotham Ultra",
                "fontSize": fsize,
                "lineHeight": 1.16,
                "color": "#FFFFFF",
                "strokeColor": "#FF6D00",
                "strokeWidth": 16,
                "textAlign": "left",
                "textTransform": "none",
                "locked": False,
                "visible": True,
                "opacity": 1.0
            })
            layers.append({
                "id": f"act_lead_{day_id}_{i+1}",
                "name": f"Activity {i+1} Lead Office",
                "type": "text",
                "x": 260,
                "y": curr_y + (130 if len(acts) == 2 else 95),
                "width": 2030,
                "height": "auto",
                "text": f"LEAD OFFICE: {act['lead_office']}",
                "fontFamily": "Gotham Bold",
                "fontSize": 48 if len(acts) > 2 else 52,
                "lineHeight": 1.15,
                "color": "#FFFFFF",
                "strokeColor": "#FF6D00",
                "strokeWidth": 12,
                "textAlign": "left",
                "textTransform": "none",
                "locked": False,
                "visible": True,
                "opacity": 1.0
            })

    elif layout == "online_only":
        layers.append({
            "id": f"track_{day_id}",
            "name": "Advocacy Track",
            "type": "text",
            "x": 190,
            "y": 1960,
            "width": 2100,
            "height": "auto",
            "text": day.get("advocacy_track", "ONLINE ADVOCACY"),
            "fontFamily": "Gotham Ultra",
            "fontSize": 76,
            "lineHeight": 1.15,
            "color": "#FFFFFF",
            "strokeColor": "#FF6D00",
            "strokeWidth": 16,
            "textAlign": "center",
            "textTransform": "uppercase",
            "locked": False,
            "visible": True,
            "opacity": 1.0
        })
        layers.append({
            "id": f"desc_{day_id}",
            "name": "Advocacy Description",
            "type": "text",
            "x": 190,
            "y": 2100,
            "width": 2100,
            "height": "auto",
            "text": day.get("description", ""),
            "fontFamily": "Gotham Bold",
            "fontSize": 96,
            "lineHeight": 1.25,
            "color": "#FFFFFF",
            "strokeColor": "#FF6D00",
            "strokeWidth": 18,
            "textAlign": "center",
            "textTransform": "none",
            "locked": False,
            "visible": True,
            "opacity": 1.0
        })

    elif layout == "day3_dual_group":
        g1 = day.get("group1", {})
        g2 = day.get("group2", {})
        start_y = 1920
        # G1 activities
        for i, act in enumerate(g1.get("activities", [])):
            curr_y = start_y + (i * 180)
            layers.append({
                "id": f"act_d3_{i+1}",
                "name": f"Activity {act['num']} Title",
                "type": "text",
                "x": 190,
                "y": curr_y,
                "width": 2100,
                "height": "auto",
                "text": f"{act['num']}. {act['description']}",
                "fontFamily": "Gotham Ultra",
                "fontSize": 48,
                "lineHeight": 1.15,
                "color": "#FFFFFF",
                "strokeColor": "#FF6D00",
                "strokeWidth": 14,
                "textAlign": "left",
                "textTransform": "none",
                "locked": False,
                "visible": True,
                "opacity": 1.0
            })
            layers.append({
                "id": f"act_d3_lead_{i+1}",
                "name": f"Activity {act['num']} Lead Office",
                "type": "text",
                "x": 250,
                "y": curr_y + 70,
                "width": 2040,
                "height": "auto",
                "text": f"LEAD OFFICE: {act['lead_office']}",
                "fontFamily": "Gotham Bold",
                "fontSize": 42,
                "lineHeight": 1.15,
                "color": "#FFFFFF",
                "strokeColor": "#FF6D00",
                "strokeWidth": 10,
                "textAlign": "left",
                "textTransform": "none",
                "locked": False,
                "visible": True,
                "opacity": 1.0
            })
        # G2 activity
        g2_act = g2.get("activity", {})
        if g2_act:
            curr_y = start_y + (3 * 180)
            layers.append({
                "id": f"act_d3_4",
                "name": f"Activity 4 Title",
                "type": "text",
                "x": 190,
                "y": curr_y,
                "width": 2100,
                "height": "auto",
                "text": f"{g2_act['num']}. {g2_act['description']}",
                "fontFamily": "Gotham Ultra",
                "fontSize": 48,
                "lineHeight": 1.15,
                "color": "#FFFFFF",
                "strokeColor": "#FF6D00",
                "strokeWidth": 14,
                "textAlign": "left",
                "textTransform": "none",
                "locked": False,
                "visible": True,
                "opacity": 1.0
            })
            layers.append({
                "id": f"act_d3_lead_4",
                "name": f"Activity 4 Lead Office",
                "type": "text",
                "x": 250,
                "y": curr_y + 70,
                "width": 2040,
                "height": "auto",
                "text": f"LEAD OFFICE: {g2_act['lead_office']}",
                "fontFamily": "Gotham Bold",
                "fontSize": 42,
                "lineHeight": 1.15,
                "color": "#FFFFFF",
                "strokeColor": "#FF6D00",
                "strokeWidth": 10,
                "textAlign": "left",
                "textTransform": "none",
                "locked": False,
                "visible": True,
                "opacity": 1.0
            })

    elif layout in ["hybrid_inperson_online", "day18_hybrid"]:
        inp = day.get("in_person", {})
        onl = day.get("online", {})
        act_title = inp.get("main_activity")
        if not act_title and "activities" in inp:
            act_title = " / ".join([a["description"] for a in inp["activities"]])
        layers.append({
            "id": f"inperson_title_{day_id}",
            "name": "In-Person Activity",
            "type": "text",
            "x": 190,
            "y": 1950,
            "width": 2100,
            "height": "auto",
            "text": act_title or "Campaign Learning Day",
            "fontFamily": "Gotham Ultra",
            "fontSize": 74,
            "lineHeight": 1.16,
            "color": "#FFFFFF",
            "strokeColor": "#FF6D00",
            "strokeWidth": 16,
            "textAlign": "center",
            "textTransform": "none",
            "locked": False,
            "visible": True,
            "opacity": 1.0
        })
        if inp.get("lead_office"):
            layers.append({
                "id": f"inperson_lead_{day_id}",
                "name": "Lead Office",
                "type": "text",
                "x": 190,
                "y": 2150,
                "width": 2100,
                "height": "auto",
                "text": f"LEAD OFFICE:  {inp['lead_office']}",
                "fontFamily": "Gotham Bold",
                "fontSize": 52,
                "lineHeight": 1.15,
                "color": "#FFFFFF",
                "strokeColor": "#FF6D00",
                "strokeWidth": 12,
                "textAlign": "left",
                "textTransform": "none",
                "locked": False,
                "visible": True,
                "opacity": 1.0
            })
        if onl:
            layers.append({
                "id": f"online_track_{day_id}",
                "name": "Online Advocacy Track",
                "type": "text",
                "x": 190,
                "y": 2260,
                "width": 2100,
                "height": "auto",
                "text": f"{onl.get('advocacy_track', 'ONLINE ADVOCACY')}: {onl.get('description', '')}",
                "fontFamily": "Gotham Bold",
                "fontSize": 52,
                "lineHeight": 1.2,
                "color": "#FFFFFF",
                "strokeColor": "#FF6D00",
                "strokeWidth": 12,
                "textAlign": "center",
                "textTransform": "none",
                "locked": False,
                "visible": True,
                "opacity": 1.0
            })

    # 6. Partners & Venue (if present)
    partners_val = day.get("partners")
    if not partners_val and day.get("group1"):
        partners_val = day["group1"].get("partners")
    if partners_val:
        layers.append({
            "id": f"partners_{day_id}",
            "name": "Partners Block",
            "type": "text",
            "x": 190,
            "y": 2660,
            "width": 2100,
            "height": "auto",
            "text": f"PARTNERS:  {partners_val}",
            "fontFamily": "Gotham Bold",
            "fontSize": 50,
            "lineHeight": 1.15,
            "color": "#FFFFFF",
            "strokeColor": "#FF6D00",
            "strokeWidth": 12,
            "textAlign": "left",
            "textTransform": "none",
            "locked": False,
            "visible": True,
            "opacity": 1.0
        })

    venue_val = day.get("venue")
    if not venue_val and day.get("group1"):
        venue_val = day["group1"].get("venue")
    if venue_val:
        layers.append({
            "id": f"venue_{day_id}",
            "name": "Venue Block",
            "type": "text",
            "x": 190,
            "y": 2770,
            "width": 2100,
            "height": "auto",
            "text": f"VENUE:  {venue_val}",
            "fontFamily": "Gotham Bold",
            "fontSize": 50,
            "lineHeight": 1.15,
            "color": "#FFFFFF",
            "strokeColor": "#FF6D00",
            "strokeWidth": 12,
            "textAlign": "left",
            "textTransform": "none",
            "locked": False,
            "visible": True,
            "opacity": 1.0
        })

    days_layers[day_id] = layers

# Save to scratch
out_json = "scratch/default_layers_by_day.json"
with open(out_json, "w", encoding="utf-8") as f:
    json.dump(days_layers, f, indent=2, ensure_ascii=False)

print(f"✓ Created {out_json} with {len(days_layers)} days.")

