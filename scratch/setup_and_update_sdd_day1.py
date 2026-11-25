import os
import glob

BASE_DIR = r"c:\Users\CODEX\Desktop\18 day calendar of activity\18 day calendar of activity"
SRC_DIR = os.path.join(BASE_DIR, "scratch", "final_html")
DST_DIR = os.path.join(BASE_DIR, "scratch", "final_html_sdd")

os.makedirs(DST_DIR, exist_ok=True)

html_files = sorted(glob.glob(os.path.join(SRC_DIR, "*.html")))
assert len(html_files) == 19, f"Expected 19 HTML files in {SRC_DIR}, found {len(html_files)}"

for src_path in html_files:
    fname = os.path.basename(src_path)
    dst_path = os.path.join(DST_DIR, fname)
    with open(src_path, "r", encoding="utf-8") as f:
        content = f.read()
    updated = content.replace("url('/FABMAT/fabmat_template.png')", "url('/FABMAT%20with%20SDD/fabmat_template.png')")
    assert "url('/FABMAT%20with%20SDD/fabmat_template.png')" in updated, f"Background URL not updated in {fname}"
    with open(dst_path, "w", encoding="utf-8") as f:
        f.write(updated)

print(f"Copied and updated background URL for {len(html_files)} HTML files into scratch/final_html_sdd/")

# Update 01-day-01.html with inline SDD on Activity 1
day1_path = os.path.join(DST_DIR, "01-day-01.html")
with open(day1_path, "r", encoding="utf-8") as f:
    day1_html = f.read()

sdd_css = """        .sdd-inline {
            display: inline-block;
            color: #FFFFFF;
            font-family: 'Gotham Ultra', sans-serif;
            font-size: 34px;
            letter-spacing: 0.8px;
            line-height: 1.15;
            margin-left: 20px;
            white-space: nowrap;
            vertical-align: baseline;
            paint-order: stroke fill;
            -webkit-text-stroke: 10px #FF6D00;
        }
        </style>"""

assert "</style>" in day1_html, "Missing </style> in 01-day-01.html"
day1_html = day1_html.replace("        </style>", sdd_css, 1)

old_act1 = '<div class="stroke-act-desc act-desc">Wellness and Essential Care Distribution for Project S.U.N.S.H.I.N.E Beneficiaries.</div>'
new_act1 = '<div class="stroke-act-desc act-desc">Wellness and Essential Care Distribution for Project S.U.N.S.H.I.N.E Beneficiaries.<span class="sdd-inline">MALES: 176 | FEMALES: 44 | TOTAL: 220</span></div>'
assert old_act1 in day1_html, "Activity 1 description not found in 01-day-01.html"
day1_html = day1_html.replace(old_act1, new_act1, 1)

with open(day1_path, "w", encoding="utf-8") as f:
    f.write(day1_html)

print("Updated scratch/final_html_sdd/01-day-01.html with inline SDD on Activity 1")
