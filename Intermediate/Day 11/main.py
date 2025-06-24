# Coding With Kien - 365 Days of Python Programming
# Intermediate - Day 11

# File Organizer based on Extension
import os
import shutil

def organize_files(directory):
    """
    Organizes files in a directory into subdirectories based on file extension.
    """
    if not os.path.isdir(directory):
        print(f"Error: Directory '{directory}' not found.")
        return

    for filename in os.listdir(directory):
        # Skip directories
        if os.path.isdir(os.path.join(directory, filename)):
            continue

        file_extension = filename.split('.')[-1].lower() if '.' in filename else 'no_extension'
        
        # Create a folder for the extension if it doesn't exist
        extension_folder = os.path.join(directory, file_extension)
        if not os.path.exists(extension_folder):
            os.makedirs(extension_folder)
            print(f"Created folder: {extension_folder}")
            
        # Move the file
        source_path = os.path.join(directory, filename)
        destination_path = os.path.join(extension_folder, filename)
        shutil.move(source_path, destination_path)
        print(f"Moved '{filename}' to '{extension_folder}'")

# --- Example Usage ---
# Create a dummy directory and some files to test
test_dir = "test_organization_folder"
if not os.path.exists(test_dir):
    os.makedirs(test_dir)

# Create dummy files
files_to_create = ["document.pdf", "image.jpg", "photo.png", "archive.zip", "data.txt", "script.py", "no_extension_file"]
for f in files_to_create:
    with open(os.path.join(test_dir, f), 'w') as temp_file:
        temp_file.write("dummy content")

print(f"Organizing files in '{test_dir}'...\n")
organize_files(test_dir)
print("\nOrganization complete.") 