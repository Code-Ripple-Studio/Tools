import os
from pathlib import Path

folder_path = r"D:\Downloads"
file_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx'],
    'Scripts': ['.py', '.js', '.sh'],
    'Videos' : ['.mp4', '.avi', '.mov']
}

path = Path(folder_path)

for file in path.iterdir():
    if file.is_file():
        ext = file.suffix.lower()
        for folder, extensions in file_types.items():
            if ext in extensions:
                dest = path / folder
                dest.mkdir(exist_ok=True)
                file.rename(dest / file.name)
                print(f"Moved {file.name} → {folder}/")
                break

print("✅ Done! Files organized!")
