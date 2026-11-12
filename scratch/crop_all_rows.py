from PIL import Image

img = Image.open('18-Day_Campaign_Calendar_A3.png')
print('A3 size:', img.size)

# Let's crop Row 2 (December Days 7-12)
# y: 1450 to 2450
crop_r2 = img.crop((100, 1500, 4860, 2450))
crop_r2.save('scratch/crop_a3_row2.png')

# Let's crop Row 3 (December Days 13-18)
# y: 2450 to 3450
crop_r3 = img.crop((100, 2450, 4860, 3450))
crop_r3.save('scratch/crop_a3_row3.png')

print("Cropped Row 2 and Row 3 successfully")

