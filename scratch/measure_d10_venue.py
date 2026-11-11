from PIL import Image
import numpy as np

img = Image.open('FABMAT/10-day-10.png').convert('RGBA')
arr = np.array(img)

# Crop venue area: x from 180 to 2280, y from 2600 to 2980
crop = img.crop((180, 2600, 2280, 2980))
crop.save('scratch/crop_d10_venue.png')

# Measure bottom-most non-background pixel below y = 2600
# Background in that region is orange gradient, text stroke is pure #FF6D00 or white #FFFFFF
# Let's inspect rows from y=2950 upwards to find text
print(f"Crop saved to scratch/crop_d10_venue.png, size: {crop.size}")

