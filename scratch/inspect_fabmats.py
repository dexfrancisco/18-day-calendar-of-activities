from PIL import Image
import numpy as np

# Load FABMAT/09-day-09.png
im9 = Image.open('FABMAT/09-day-09.png')
print('FABMAT/09-day-09.png size:', im9.size)

# Let's crop where "End VAWC Action Forum" should be (middle block)
# safe-zone is at top: 1310. Hero icon is 580px. Top row height ~ 600px.
# Middle block starts around y = 1310 + 600 + 20 = 1930px.
crop_title = im9.crop((200, 1900, 2280, 2250))
crop_title.save('scratch/inspect_fabmat_d9_title.png')

# Crop where venue should be (around y = 2400 to 2600)
crop_venue = im9.crop((200, 2400, 2280, 2650))
crop_venue.save('scratch/inspect_fabmat_d9_venue.png')

# Load FABMAT/10-day-10.png
im10 = Image.open('FABMAT/10-day-10.png')
print('FABMAT/10-day-10.png size:', im10.size)

# Crop where MOVE forum should be
crop_d10_acts = im10.crop((200, 1900, 2280, 2600))
crop_d10_acts.save('scratch/inspect_fabmat_d10_acts.png')

print("Inspection crops saved!")

