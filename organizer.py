import os
import shutil
import json
import hashlib
from tkinter import Tk
from tkinter.filedialog import askdirectory

# =========================================================
# UNDO LOG FILE
# =========================================================

UNDO_LOG = "undo_log.json"

# =========================================================
# CATEGORY DEFINITIONS
# =========================================================

CATEGORY_MAP = {

    # =====================================================
    # DOCUMENTS
    # =====================================================

    "Documents": [
        ".pdf", ".doc", ".docx",
        ".ppt", ".pptx",
        ".xls", ".xlsx",
        ".txt", ".csv"
    ],

    # =====================================================
    # IMAGES
    # =====================================================

    "Images": [
        ".jpg", ".jpeg",
        ".png", ".gif",
        ".bmp", ".webp"
    ],

    # =====================================================
    # VIDEOS
    # =====================================================

    "Videos": [
        ".mp4", ".mkv",
        ".avi", ".mov"
    ],

    # =====================================================
    # MUSIC
    # =====================================================

    "Music": [
        ".mp3", ".wav",
        ".aac"
    ],

    # =====================================================
    # ARCHIVES
    # =====================================================

    "Archives": [
        ".zip", ".rar",
        ".7z", ".iso"
    ],

    # =====================================================
    # PROGRAMS
    # =====================================================

    "Programs": [
        ".exe", ".msi",
        ".bat"
    ]
}

# =========================================================
# GET CATEGORY
# =========================================================

def get_category(extension):

    for category, extensions in CATEGORY_MAP.items():

        if extension in extensions:

            return category

    return "Others"

# =========================================================
# SAVE UNDO LOG
# =========================================================

def save_undo_log(log_data):

    with open(UNDO_LOG, "w") as file:

        json.dump(log_data, file, indent=4)

# =========================================================
# LOAD UNDO LOG
# =========================================================

def load_undo_log():

    if os.path.exists(UNDO_LOG):

        with open(UNDO_LOG, "r") as file:

            return json.load(file)

    return []

# =========================================================
# FORMAT FILE SIZE
# =========================================================

def format_size(size):

    if size < 1024:

        return f"{size} B"

    elif size < 1024 * 1024:

        return f"{round(size / 1024, 2)} KB"

    else:

        return f"{round(size / (1024 * 1024), 2)} MB"

# =========================================================
# GENERATE FILE HASH
# =========================================================

def get_file_hash(file_path):

    hash_object = hashlib.md5()

    try:

        with open(file_path, "rb") as file:

            while chunk := file.read(4096):

                hash_object.update(chunk)

        return hash_object.hexdigest()

    except:

        return None

# =========================================================
# ORGANIZE FUNCTION
# =========================================================

def organize_folder():

    # Hide tkinter window
    Tk().withdraw()

    # Select folder
    folder_path = askdirectory(
        title="Select Folder To Organize"
    )

    # No folder selected
    if not folder_path:

        print("\nNo folder selected!")

        return

    # =====================================================
    # ORGANIZATION MODE
    # =====================================================

    print("\nChoose Organization Mode:\n")

    print("1. Extension Wise")
    print("2. Category Wise")

    mode = input(
        "\nEnter choice (1 or 2): "
    ).strip()

    # =====================================================
    # DELETE EMPTY FOLDERS OPTION
    # =====================================================

    delete_empty = input(
        "\nDelete empty folders? (y/n): "
    ).strip().lower()

    # =====================================================
    # STATISTICS
    # =====================================================

    file_count = {}

    group_total_size = {}

    total_moved = 0

    duplicate_skipped = 0

    undo_log = []

    current_extension_group = ""

    # =====================================================
    # HASH DATABASE
    # =====================================================

    hash_database = {}

    # =====================================================
    # WALK THROUGH FILES
    # =====================================================

    for root, dirs, files in os.walk(folder_path):

        for file in files:

            file_path = os.path.join(root, file)

            # Skip undo log
            if file == UNDO_LOG:

                continue

            # Skip folders
            if os.path.isdir(file_path):

                continue

            # Get extension
            extension = os.path.splitext(file)[1].lower()

            # Skip files without extension
            if extension == "":

                continue

            # =================================================
            # CHECK DUPLICATE CONTENT
            # =================================================

            file_hash = get_file_hash(file_path)

            if file_hash in hash_database:

                duplicate_skipped += 1

                print("\n")

                print("=" * 100)

                print("DUPLICATE FILE DETECTED")

                print("=" * 100)

                print(
                    f"{'CURRENT FILE':<20} : "
                    f"{file}"
                )

                print(
                    f"{'SAME AS':<20} : "
                    f"{hash_database[file_hash]}"
                )

                print(
                    f"{'ACTION':<20} : "
                    f"Skipped"
                )

                continue

            else:

                hash_database[file_hash] = file

            # =================================================
            # GET CATEGORY
            # =================================================

            category_name = get_category(extension)

            # =================================================
            # EXTENSION MODE
            # =================================================

            if mode == "1":

                extension_folder = (
                    extension[1:].upper()
                    + "_Files"
                )

                destination_folder = os.path.join(
                    folder_path,
                    category_name,
                    extension_folder
                )

            # =================================================
            # CATEGORY MODE
            # =================================================

            else:

                extension_folder = category_name

                destination_folder = os.path.join(
                    folder_path,
                    category_name
                )

            # =================================================
            # CREATE FOLDER
            # =================================================

            os.makedirs(
                destination_folder,
                exist_ok=True
            )

            # =================================================
            # DESTINATION PATH
            # =================================================

            destination_path = os.path.join(
                destination_folder,
                file
            )

            # Skip already organized files
            if file_path == destination_path:

                continue

            # =================================================
            # HANDLE DUPLICATES
            # =================================================

            counter = 1

            original_name, extension_part = os.path.splitext(file)

            while os.path.exists(destination_path):

                new_name = (
                    f"{original_name}_{counter}"
                    f"{extension_part}"
                )

                destination_path = os.path.join(
                    destination_folder,
                    new_name
                )

                counter += 1

            # =================================================
            # PRINT NEW EXTENSION GROUP
            # =================================================

            if extension_folder != current_extension_group:

                current_extension_group = extension_folder

                print("\n")

                print("=" * 120)

                print(
                    f"EXTENSION GROUP : "
                    f"{extension_folder}"
                )

                print("=" * 120)

                print(
                    f"{'FILE NAME':<40} | "
                    f"{'SIZE':<10} | "
                    f"{'CATEGORY':<15} | "
                    f"{'ORIGINAL PATH'}"
                )

                print("-" * 120)

            # =================================================
            # MOVE FILE
            # =================================================

            shutil.move(
                file_path,
                destination_path
            )

            # =================================================
            # FORMAT FILE NAME
            # =================================================

            display_name = file

            if len(display_name) > 40:

                display_name = (
                    display_name[:37] + "..."
                )

            # =================================================
            # FORMAT PATH
            # =================================================

            display_path = root

            if len(display_path) > 40:

                display_path = (
                    "..."
                    + display_path[-37:]
                )

            # =================================================
            # FILE SIZE
            # =================================================

            file_size = os.path.getsize(
                destination_path
            )

            size_display = format_size(
                file_size
            )

            # =================================================
            # PRINT CLEAN OUTPUT
            # =================================================

            print(
                f"{display_name:<40} | "
                f"{size_display:<10} | "
                f"{category_name:<15} | "
                f"{display_path}"
            )

            # =================================================
            # SAVE TOTAL SIZE
            # =================================================

            if extension_folder not in group_total_size:

                group_total_size[extension_folder] = 0

            group_total_size[extension_folder] += file_size

            # =================================================
            # SAVE UNDO DATA
            # =================================================

            undo_log.append({

                "source": file_path,

                "destination": destination_path
            })

            # =================================================
            # STATISTICS
            # =================================================

            if extension_folder not in file_count:

                file_count[extension_folder] = 0

            file_count[extension_folder] += 1

            total_moved += 1

    # =====================================================
    # SAVE UNDO LOG
    # =====================================================

    save_undo_log(undo_log)

    # =====================================================
    # SUMMARY REPORT
    # =====================================================

    print("\n")

    print("=" * 90)

    print("FILE ORGANIZATION COMPLETED")

    print("=" * 90)

    print(
        f"\n{'EXTENSION GROUP':<25} | "
        f"{'FILES':<10} | "
        f"{'TOTAL SIZE'}"
    )

    print("-" * 90)

    for folder_name, count in sorted(file_count.items()):

        total_size_display = format_size(
            group_total_size[folder_name]
        )

        print(
            f"{folder_name:<25} | "
            f"{count:<10} | "
            f"{total_size_display}"
        )

    print("\n")

    print(f"Total Files Moved      : {total_moved}")

    print(f"Duplicate Files Skipped : {duplicate_skipped}")

    # =====================================================
    # DELETE EMPTY FOLDERS
    # =====================================================

    if delete_empty in ["y", "yes"]:

        print("\n")

        print("=" * 90)

        print("EMPTY FOLDER CLEANUP")

        print("=" * 90)

        print(
            f"\n{'STATUS':<15} | "
            f"{'FOLDER PATH'}"
        )

        print("-" * 90)

        for root, dirs, files in os.walk(
            folder_path,
            topdown=False
        ):

            # Skip main folder
            if root == folder_path:

                continue

            try:

                # Delete empty folder
                if not os.listdir(root):

                    os.rmdir(root)

                    display_root = root

                    if len(display_root) > 60:

                        display_root = (
                            "..."
                            + display_root[-57:]
                        )

                    print(
                        f"{'DELETED':<15} | "
                        f"{display_root}"
                    )

            except Exception as error:

                print(
                    f"{'FAILED':<15} | "
                    f"{root}"
                )

                print(
                    f"Reason: {error}"
                )

# =========================================================
# UNDO FUNCTION
# =========================================================

def undo_last_operation():

    undo_log = load_undo_log()

    if not undo_log:

        print("\nNo undo history found.")

        return

    print("\n")

    print("=" * 90)

    print("UNDOING LAST OPERATION")

    print("=" * 90)

    print(
        f"\n{'STATUS':<15} | "
        f"{'FILE'}"
    )

    print("-" * 90)

    for item in reversed(undo_log):

        try:

            if os.path.exists(item["destination"]):

                # Create original folder
                os.makedirs(
                    os.path.dirname(item["source"]),
                    exist_ok=True
                )

                # Restore file
                shutil.move(
                    item["destination"],
                    item["source"]
                )

                display_name = os.path.basename(
                    item["source"]
                )

                if len(display_name) > 45:

                    display_name = (
                        display_name[:42]
                        + "..."
                    )

                print(
                    f"{'RESTORED':<15} | "
                    f"{display_name}"
                )

        except Exception as error:

            print(
                f"{'FAILED':<15} | "
                f"{item['destination']}"
            )

            print(
                f"Reason: {error}"
            )

    print("\nUndo completed successfully.")

# =========================================================
# MAIN MENU
# =========================================================

print("\n")

print("=" * 90)

print("SMART FILE ORGANIZER")

print("=" * 90)

print("\n1. Organize Folder")
print("2. Undo Last Operation")

choice = input(
    "\nEnter your choice: "
).strip()

# =========================================================
# MENU OPTIONS
# =========================================================

if choice == "1":

    organize_folder()

elif choice == "2":

    undo_last_operation()

else:

    print("\nInvalid option selected.")
