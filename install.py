import os
from pathlib import Path
import shutil

current_dir = os.path.dirname(os.path.abspath(__file__))
home_dir = Path.home()
configs_dir = Path(current_dir) / "configs"

print("📂 Copying configs")

for dir in configs_dir.iterdir():
    shutil.copytree(Path(dir), home_dir / dir.name, dirs_exist_ok=True)


print("✅ Everything installed successfully")