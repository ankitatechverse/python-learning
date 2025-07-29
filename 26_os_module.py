# --------------------------
# OS Module
# --------------------------

# --- Rules ---
"""
1. It’s part of Python’s standard library (no need to install).
2. Used for file handling, directory management, environment variables, and system info.
3. Use os.path.join() instead of manually adding "/" or "\" for cross-platform code.
4. Always check os.path.exists() before deleting or renaming files.
5. For path operations, Python 3.4+ has a better alternative: pathlib (more modern).
"""

# Example 1:- Get Current Working Directory
import os
print(os.getcwd())

# Example 2:- 
os.mkdir("test_folder")          # Create a single directory
os.makedirs("a/b/c")            # Create nested directories
os.rmdir("test_folder")         # Remove a single directory
os.removedirs("a/b/c")          # Remove nested directories

