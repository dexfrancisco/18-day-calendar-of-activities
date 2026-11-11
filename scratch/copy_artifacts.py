import shutil
import os

artifact_dir = r"C:\Users\CODEX\.gemini\antigravity\brain\b7c2e81a-36ee-4a46-9056-c62523c3de30"
base_dir = r"c:\Users\CODEX\Desktop\18 day calendar of activity\18 day calendar of activity"

src_preview = os.path.join(base_dir, "scratch", "editor_preview.png")
dst_preview = os.path.join(artifact_dir, "editor_studio_preview.png")
shutil.copy2(src_preview, dst_preview)

src_thumb = os.path.join(base_dir, "scratch", "editor_thumb.png")
dst_thumb = os.path.join(artifact_dir, "editor_studio_thumb.png")
shutil.copy2(src_thumb, dst_thumb)

src_canvas = os.path.join(base_dir, "scratch", "editor_crop_canvas.png")
dst_canvas = os.path.join(artifact_dir, "editor_canvas_crop.png")
shutil.copy2(src_canvas, dst_canvas)

print("✓ Copied preview, thumb, and canvas crop to artifacts directory.")

