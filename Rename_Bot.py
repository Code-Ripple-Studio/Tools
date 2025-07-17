import os

folder_path = r"D:\DCIM"
prefix = "image_"

files = os.listdir(folder_path)

for index, file_name in enumerate(files):
    extension = os.path.splitext(file_name)[1]
    new_name = f"{prefix}{index + 1}{extension}"

    old_path = os.path.join(folder_path, file_name)
    new_path = os.path.join(folder_path, new_name)

    os.rename(old_path, new_path)
    print(f"Renamed: {file_name} ➜ {new_name}")

print(f"\n✅ Done! {len(files)} files renamed.")
