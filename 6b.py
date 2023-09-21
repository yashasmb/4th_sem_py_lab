import os  # Import the os module for file and directory operations.
import sys  # Import the sys module for system-related functionality.
import pathlib  # Import the pathlib module for working with file paths.
import zipfile  # Import the zipfile module for working with zip archives.

# Ask the user to input the directory name they want to backup.
dirName = input("Enter Directory name that you want to backup: ")

# Check if the entered directory exists.
if not os.path.isdir(dirName):
    print("Directory", dirName, "doesn't exist")
    sys.exit(0)  # Exit the program if the directory doesn't exist.

# Create a pathlib object for the specified directory.
curDirectory = pathlib.Path(dirName)

# Initialize a variable 'number' to keep track of the backup number.
number = 1

# Loop to find a unique backup zip filename.
while True:
    # Generate the backup zip filename using the directory name and a number.
    zipFilename = os.path.basename(curDirectory) + '_' + str(number) + '.zip'

    # Check if the zip filename already exists.
    if not os.path.exists(zipFilename):
        break  # Exit the loop if the filename is unique.

    number = number + 1  # Increment the number if the filename already exists.

# Print a message indicating that a backup zip file is being created.
print(f'Creating {zipFilename}...')

# Create a new zip archive with the specified filename in write mode.
with zipfile.ZipFile(zipFilename, mode="w") as archive:
    # Recursively iterate through all files and directories in the specified directory.
    for file_path in curDirectory.rglob("*"):
        # Write each file/directory to the zip archive with its relative path.
        archive.write(file_path, arcname=file_path.relative_to(curDirectory))

# Check if the zip archive file was successfully created.
if os.path.isfile(zipFilename):
    print("Archive", zipFilename, "created successfully")
else:
    print("Error in creating zip archive")
