## Installation

Make sure Python is installed on your system.

Check Python version:

```bash
python --version
```

## How To Run

Open terminal or command prompt inside the project folder and run:

```bash
python organizer.py
```

## Program Menu

```text
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

```text
EXTENSION GROUP : PDF_Files

FILE NAME                               | SIZE       | CATEGORY       | ORIGINAL PATH
------------------------------------------------------------------------------------------------
resume.pdf                              | 1.2 MB     | Documents      | D:/files
notes.pdf                               | 850 KB     | Documents      | D:/downloads
```
