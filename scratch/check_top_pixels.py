from PIL import Image
import numpy as np

img = Image.open('scratch/editor_preview.png')
print('Size:', img.size)
arr = np.array(img)
# Let's inspect the top 50 pixels
print('Top 50 pixels text presence:', arr[10:40, 20:500].mean())

