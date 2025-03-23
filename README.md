# File-Size-Calculator-for-Specific-Extensions
File Size Calculator for Specific Extensions

## How to Use
1.  Download or clone this repository.
2.  Modify the folder_path in the Python script to the desired directory.
3.  Add or remove file extensions in the extensions set to suit your needs.
4.  Run the script, and it will display the results in the console, showing the number of files and their total size in KB, MB, and GB.
## Example Output
.mp4: 50 files, total size: 10485760.00 KB (10240.00 MB, 10.0000 GB)                        
.docx: 12 files, total size: 2097152.00 KB (2048.00 MB, 2.0000 GB)                     
.set: 2 files, total size: 850.00 KB (0.83 MB, 0.0008 GB)

Total size of all files: 12600062.00 KB (12354.93 MB, 12.0871 GB)



# File Size Calculator for Specific Extensions

This Python script helps calculate the file count and total size for specified file extensions in a given directory. The results are shown in **KB**, **MB**, and **GB** units. This script supports long file paths and handles possible errors such as access permissions or file not found issues.

## Features

- Recursively walks through the directory to find files with specified extensions.
- Supports multiple file extensions (e.g., `.mp4`, `.docx`, `.png`, etc.).
- Displays the count and total size for each file extension.
- Converts the total size into **KB**, **MB**, and **GB**.
- Handles long file paths using Python's `\\?\` prefix.
- Prints a total file size summary for all found files.

## Requirements

- Python 3.x
- No external dependencies required.

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/hd3mir/file-size-calculator.git
