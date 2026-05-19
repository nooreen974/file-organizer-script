# Smart File Organizer

A beginner-friendly Python automation tool that automatically organizes messy folders into structured categories and extension-based folders.

This project was built to simplify file management by automatically sorting files, detecting duplicate content, cleaning empty folders, and allowing users to undo organization operations safely.

The tool is designed for:

* Students
* Beginners learning Python
* System cleanup
* Automation practice
* File management utilities

## Features

* Organize files by:

  * Extension Wise
  * Category Wise

* Automatic folder creation

* Duplicate filename handling

* Duplicate content detection using hashing

* Undo last organization operation

* Empty folder cleanup

* File size display

* Clean terminal table output

* Human-readable summary report

## Categories Supported

* Documents
* Images
* Videos
* Music
* Archives
* Programs
* Others

## Example Folder Structure

### Extension Wise Mode

```text id="bgumhy"
Documents/
├── PDF_Files/
├── DOCX_Files/
├── PPTX_Files/

Images/
├── PNG_Files/
├── JPG_Files/
```

## Technologies Used

* Python
* os
* shutil
* hashlib
* json
* tkinter

## Installation

Make sure Python is installed on your system.

Check Python version:

```bash id="rm7gkr"
python --version
```

## How To Run

Open terminal or command prompt inside the project folder and run:

```bash id="z9d7u8"
python organizer.py
```

## Program Menu

```text id="9k1fyy"
1. Organize Folder
2. Undo Last Operation
```

## How To Use

### Organize Folder

1. Run the script
2. Select:

   * Organize Folder
3. Choose the folder you want to organize
4. Select organization mode:

   * Extension Wise
   * Category Wise
5. Choose whether to delete empty folders
6. Files will automatically be organized

### Undo Last Operation

If you want to restore files back to original locations:

1. Run the script again
2. Select:

   * Undo Last Operation

The script restores moved files using the undo log.

## Example Output

```text id="ax7azq"
EXTENSION GROUP : PDF_Files

FILE NAME                               | SIZE       | CATEGORY       | ORIGINAL PATH
------------------------------------------------------------------------------------------------
resume.pdf                              | 1.2 MB     | Documents      | D:/files
notes.pdf                               | 850 KB     | Documents      | D:/downloads
```

## Future Improvements

* GUI desktop application
* Drag & drop support
* Real-time monitoring
* Export reports
* Cloud backup support

## Author

**Nooreen Siddiqui**
