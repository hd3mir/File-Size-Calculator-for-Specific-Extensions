import os

def calculate_file_size_and_count(folder_path, extensions):
    file_sizes = {ext: (0, 0) for ext in extensions}
    total_size_kb = 0  # To store total size in KB
    
    for root, _, files in os.walk(folder_path, followlinks=True):
        for file in files:
            try:
                _, file_extension = os.path.splitext(file)
                file_extension = file_extension.lower()

                if file_extension in extensions:
                    file_path = r"\\?\\" + os.path.join(root, file)  # Long path support
                    if not os.path.exists(file_path):  
                        print(f"Warning: {file_path} not found, skipping.")
                        continue

                    file_bytes = os.path.getsize(file_path)
                    file_kb = file_bytes / 1024  # KB
                    file_mb = file_kb / 1024  # MB
                    file_gb = file_mb / 1024  # GB

                    file_count, total_size_kb_for_ext = file_sizes[file_extension]
                    file_sizes[file_extension] = (file_count + 1, total_size_kb_for_ext + file_kb)

                    total_size_kb += file_kb  # Add the file size to total size in KB

            except (PermissionError, FileNotFoundError, OSError) as e:
                print(f"Error: Could not access {file}. {e}")

    return file_sizes, total_size_kb

folder_path = r"D:\\"  # Root directory
extensions = {
    ".mp4", ".pptx", ".docx", ".png", ".flv", ".mts", ".mpg", ".m4v", ".wav",
    ".avi", ".mov", ".jpg", ".jpeg", ".pdf", ".wpt", ".set", ".rte", ".doc",
    ".mp3", ".xlsx"
}

file_sizes, total_size_kb = calculate_file_size_and_count(folder_path, extensions)

# Output in KB, MB, and GB
for ext, (file_count, total_kb) in file_sizes.items():
    total_mb = total_kb / 1024  # Convert to MB
    total_gb = total_mb / 1024  # Convert to GB
    print(f"{ext}: {file_count} files, total size: {total_kb:.2f} KB ({total_mb:.2f} MB, {total_gb:.4f} GB)")

# Print the overall total size
total_mb = total_size_kb / 1024  # Convert to MB
total_gb = total_mb / 1024  # Convert to GB
print(f"\nTotal size of all files: {total_size_kb:.2f} KB ({total_mb:.2f} MB, {total_gb:.4f} GB)")
