from PIL import Image

im2 = Image.open('FABMAT/02-day-02.png')
# Crop activities area
c2 = im2.crop((200, 1900, 2280, 2600))
c2.save('scratch/inspect_fabmat_d2.png')

im3 = Image.open('FABMAT/03-day-03.png')
c3 = im3.crop((200, 1900, 2280, 2600))
c3.save('scratch/inspect_fabmat_d3.png')

im4 = Image.open('FABMAT/04-day-04.png')
c4 = im4.crop((200, 1900, 2280, 2300))
c4.save('scratch/inspect_fabmat_d4.png')

print("Crops of Day 2, 3, 4 saved!")

