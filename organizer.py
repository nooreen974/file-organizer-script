import os
import shutil
import platform
import subprocess
from tkinter import Tk
from tkinter.filedialog import askdirectory

# Hide tkinter window
Tk().withdraw()

# Select folder
folder_path = askdirectory(title="Select Folder To Organize")

# Check selection
if not folder_path:
    print("No folder selected!")
    exit()
    
delete_empty = input(
    "Delete empty folders? (yes/no or y/n): "
).strip().lower()

# Walk through all folders and subfolders
for root, dirs, files in os.walk(folder_path):

    # Skip already organized folders
    if root.endswith("_Files"):
        continue

    # Process files
    for file in files:

        # Full file path
        file_path = os.path.join(root, file)

        # Get extension
        extension = os.path.splitext(file)[1].lower()

        # Skip files without extension
        if extension == "":
            continue

        # Folder name
        folder_name = extension[1:].upper() + "_Files"

        # Destination folder in main selected directory
        destination_folder = os.path.join(folder_path, folder_name)

        # Create folder if missing
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)

        # Destination file path
        destination_path = os.path.join(destination_folder, file)

        # Move file
        shutil.move(file_path, destination_path)

        print(f"{file} moved to {folder_name}")

print("File organization completed!")

# Delete empty folders if user wants
if delete_empty in ["yes", "y"]:

    print("\nChecking for empty folders...\n")

    for root, dirs, files in os.walk(folder_path, topdown=False):

        # Skip main folder
        if root == folder_path:
            continue

        try:

            # Check if folder empty
            if not os.listdir(root):

                print(f"Deleting empty folder: {root}")

                os.rmdir(root)

                print(f"Successfully deleted: {root}")

        except Exception as error:

            print(f"Could not delete folder: {root}")

            print(f"Reason: {error}")

# Open organized folder automatically
print("\nOpening organized folder...")

try:

    if platform.system() == "Windows":
        os.startfile(folder_path)

    elif platform.system() == "Darwin":
        subprocess.run(["open", folder_path])

    else:
        subprocess.run(["xdg-open", folder_path])

except Exception as error:

    print(f"Could not open folder automatically.")

    print(f"Reason: {error}")
