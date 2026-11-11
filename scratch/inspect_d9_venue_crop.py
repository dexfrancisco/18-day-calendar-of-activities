from PIL import Image
import os
import shutil

art_dir = r"C:\Users\CODEX\.gemini\antigravity\brain\b7c2e81a-36ee-4a46-9056-c62523c3de30"

im9 = Image.open('FABMAT/09-day-09.png')
# Crop the bottom block of Day 9
c9_btm = im9.crop((180, 2600, 2300, 2900))
c9_btm.save('scratch/crop_d9_isabela_venue.png')
shutil.copy('scratch/crop_d9_isabela_venue.png', os.path.join(art_dir, 'crop_d9_isabela_venue.png'))

print("Crop of Day 9 Isabela Convention Center venue saved!")

