from PIL import Image
import os
import shutil

art_dir = r"C:\Users\CODEX\.gemini\antigravity\brain\b7c2e81a-36ee-4a46-9056-c62523c3de30"

# 1. Day 9
im9 = Image.open('FABMAT/09-day-09.png')
# Crop hero icon + day/date + title
c9_top = im9.crop((180, 1300, 2300, 2200))
c9_top.save('scratch/crop_d9_fresh_top.png')
shutil.copy('scratch/crop_d9_fresh_top.png', os.path.join(art_dir, 'crop_d9_fresh_top.png'))

# Crop venue area
c9_venue = im9.crop((180, 2300, 2300, 2650))
c9_venue.save('scratch/crop_d9_fresh_venue.png')
shutil.copy('scratch/crop_d9_fresh_venue.png', os.path.join(art_dir, 'crop_d9_fresh_venue.png'))

# 2. Day 10
im10 = Image.open('FABMAT/10-day-10.png')
# Crop hero icon + day/date + activities
c10_top = im10.crop((180, 1300, 2300, 2400))
c10_top.save('scratch/crop_d10_fresh_top.png')
shutil.copy('scratch/crop_d10_fresh_top.png', os.path.join(art_dir, 'crop_d10_fresh_top.png'))

print("Fresh crops generated!")

