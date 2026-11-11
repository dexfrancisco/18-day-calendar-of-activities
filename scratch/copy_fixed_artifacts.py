import shutil
import os

artifact_dir = r"C:\Users\CODEX\.gemini\antigravity\brain\b7c2e81a-36ee-4a46-9056-c62523c3de30"
base_dir = r"c:\Users\CODEX\Desktop\18 day calendar of activity\18 day calendar of activity"

files_to_copy = [
    ("scratch/clean_editor_preview.png", "editor_studio_preview.png"),
    ("scratch/clean_canvas_crop.png", "clean_canvas_crop.png"),
    ("scratch/clean_top_crop.png", "clean_top_crop.png"),
    ("scratch/clean_dock_crop.png", "clean_dock_crop.png")
]

for src, dst in files_to_copy:
    src_path = os.path.join(base_dir, src)
    dst_path = os.path.join(artifact_dir, dst)
    if os.path.exists(src_path):
        shutil.copy2(src_path, dst_path)
        print(f"✓ Copied {src} -> {dst}")

