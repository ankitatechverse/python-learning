# --------------------------
# Shutil module tests
# --------------------------

"""
Part of Python’s standard library (no install needed).
Name = shell utilities (think: things you’d do in a terminal like cp, mv, rm).
Provides functions for copying, moving, removing, and compressing files/directories.
"""

# Copying
import shutil

# Copy a single file
shutil.copy("source.txt", "destination.txt")  

# Copy file with metadata (permissions, timestamps)
shutil.copy2("source.txt", "destination.txt")

# Copy entire folder
shutil.copytree("example", "example2")


# Moving & Renaming
shutil.move("example/2_wish_according_time.py", "example2/12_simple_calculator.py")

# Deleting
shutil.rmtree("example2")  # Delete folder & all its content

# Disk Usage
total, used, free = shutil.disk_usage("/")
print(f"Total: {total}, Used: {used}, Free: {free}")

# Archiving (Zip/Tar)
# Create a ZIP archive
# shutil.make_archive("backup", "zip", "my_folder")

# Extract (use shutil.unpack_archive)
# shutil.unpack_archive("backup.zip", "extracted_folder")

