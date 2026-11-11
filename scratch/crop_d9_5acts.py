from PIL import Image
import os
import shutil

art_dir = r"C:\Users\CODEX\.gemini\antigravity\brain\b7c2e81a-36ee-4a46-9056-c62523c3de30"

im9 = Image.open('FABMAT/09-day-09.png')
# size: 2480 x 3508
c9_acts = im9.crop((180, 1300, 2300, 2900))
c9_acts.save('scratch/crop_d9_5acts_poster.png')
shutil.copy('scratch/crop_d9_5acts_poster.png', os.path.join(art_dir, 'crop_d9_5acts_poster.png'))

print("Crop of Day 9 with all 5 activities saved!")

