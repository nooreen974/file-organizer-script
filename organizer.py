import os
import shutil

# Folder to organize
folder_path = "test_folder"

# File type folders
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".txt", ".docx"],
    "Music": [".mp3", ".wav"],
    "Videos": [".mp4", ".mkv"],
    "Python_Files": [".py"]
}

# Get all files
files = os.listdir(folder_path)

# Loop through every file
for file in files:

    # Full file path
    file_path = os.path.join(folder_path, file)

    # Skip folders
    if os.path.isdir(file_path):
        continue

    # Check file extensions
    for folder_name, extensions in file_types.items():

        if file.lower().endswith(tuple(extensions)):

            # Create destination folder path
            destination_folder = os.path.join(folder_path, folder_name)

            # Create folder if not exists
            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)

            # Destination file path
            destination_path = os.path.join(destination_folder, file)

            # Move file
            shutil.move(file_path, destination_path)

            print(f"{file} moved to {folder_name}")

            break

print("File organization completed!")
