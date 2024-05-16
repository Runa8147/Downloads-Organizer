import os
import shutil

# Set the path to your Downloads folder
downloads_path = os.path.expanduser("~/Downloads")

# Create a dictionary to map file extensions to folder names
extension_folders = {
    ".pdf": "PDFs",
    ".doc": "Documents",
    ".docx": "Documents",
    ".pptx": "Documents",
    ".html": "Webpage",
    ".htm": "Webpage",
    ".ppt": "Documents",
    ".txt": "Text Files",
    ".jpg": "Images",
    ".jpeg":"Images",
    ".png": "Images",
    ".gif": "Images",
    ".webp":"Images",
    ".mp3": "Music",
    ".wav": "Music",
    ".m4a": "Music",
    ".mp4": "Videos",
    ".avi": "Videos",
    ".zip": "Archives",
    ".rar": "Archives",
    ".exe": "apps",
    ".py":"pythons",
    ".xlsx":"sheets",
    ".xls":"sheets",
    ".xlsm":"sheets"
    }

# Loop through each file in the Downloads folder
for filename in os.listdir(downloads_path):
    # Get the file extension
    extension = os.path.splitext(filename)[1].lower()
    
    # Check if the file extension is in the dictionary
    if extension in extension_folders:
        # Get the folder name for the file extension
        folder_name = extension_folders[extension]
        
        # Create the folder if it doesn't exist
        folder_path = os.path.join(downloads_path, folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        
        # Move the file to the folder
        source_path = os.path.join(downloads_path, filename)
        destination_path = os.path.join(folder_path, filename)
        shutil.move(source_path, destination_path)
        print(f"Moved {filename} to {folder_name}")