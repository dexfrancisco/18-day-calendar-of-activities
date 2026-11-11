import shutil
import os

artifact_dir = r"C:\Users\CODEX\.gemini\antigravity\brain\b7c2e81a-36ee-4a46-9056-c62523c3de30"
base_dir = r"c:\Users\CODEX\Desktop\18 day calendar of activity\18 day calendar of activity"

shutil.copy2(os.path.join(base_dir, "scratch", "clean_editor_preview.png"), os.path.join(artifact_dir, "editor_studio_preview.png"))
shutil.copy2(os.path.join(base_dir, "scratch", "studio_badge_crop.png"), os.path.join(artifact_dir, "studio_badge_crop.png"))

print("✓ Copied updated preview and studio badge to artifacts directory.")

