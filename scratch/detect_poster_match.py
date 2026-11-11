import os
from PIL import Image
import numpy as np

BASE_DIR = r"c:\Users\CODEX\Desktop\18 day calendar of activity\18 day calendar of activity"
p1 = Image.open(os.path.join(BASE_DIR, "scratch", "perfect_canvas_crop.png"))
arr1 = np.array(p1)

# Find where the poster starts horizontally in p1 (non-dark border)
# Background of workbench is #121212 (around [18, 18, 18])
is_poster = (arr1[:, :, 0] > 35) | (arr1[:, :, 1] > 35) | (arr1[:, :, 2] > 35)
cols_with_poster = np.where(is_poster.any(axis=0))[0]
if len(cols_with_poster) > 0:
    min_x = cols_with_poster[0]
    max_x = cols_with_poster[-1]
    print(f"Poster detected at x in [{min_x}, {max_x}], width = {max_x - min_x + 1}")
    poster_cropped = p1.crop((min_x, 0, max_x + 1, p1.height))
    poster_cropped.save(os.path.join(BASE_DIR, "scratch", "editor_isolated_poster.png"))
    
    # Check mean color and visual balance
    arr_post = np.array(poster_cropped)
    print("Poster mean color:", arr_post.mean(axis=(0,1)))
    print("Poster unique colors:", len(np.unique(arr_post.reshape(-1, arr_post.shape[-1]), axis=0)))

