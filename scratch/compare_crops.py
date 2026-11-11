import os
from PIL import Image

BASE_DIR = r"c:\Users\CODEX\Desktop\18 day calendar of activity\18 day calendar of activity"
preview_path = os.path.join(BASE_DIR, "scratch", "editor_preview.png")

img = Image.open(preview_path)

# Canvas in editor: x: 490..1440, y: 85..1030
canvas_crop = img.crop((490, 85, 1440, 1030))
canvas_crop.save(os.path.join(BASE_DIR, "scratch", "perfect_canvas_crop.png"))

# Real poster resized to same height (945px)
real_poster = Image.open(os.path.join(BASE_DIR, "FABMAT", "00-pre-campaign.png"))
real_resized = real_poster.resize((round(real_poster.width * 945 / real_poster.height), 945), Image.Resampling.LANCZOS)
real_resized.save(os.path.join(BASE_DIR, "scratch", "real_poster_comparison.png"))

print("Canvas crop size:", canvas_crop.size)
print("Real resized poster size:", real_resized.size)

