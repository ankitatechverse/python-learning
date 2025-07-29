# --------------------------
# Files
# --------------------------

# --- Rules ---
"""
1. Always close files (or use with).
2. Use correct mode ('r', 'w', 'a' etc.).
3. For non-text files, always use binary ('b').
4. Use encoding='utf-8' for cross-platform text handling.

open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)

** Main Parameters:
=> file → File path (e.g., "data.txt").
=> mode → How you want to open it (read/write/append etc.).
=> encoding → For text files (UTF-8 is common).
=> newline → Controls how newlines are handled.
=> errors → What to do on encoding errors ('ignore', 'replace').
"""


# Example 1:-  Reading Files
file = open("sample.txt", "r")
print(file.read()) # Read whole file
file.close()

# Read Specific Bytes
file = open("sample.txt", "r")
print(file.read(10)) # First 10 characters
file.close()

# Read Line by Line
file = open("sample.txt", "r")
print(file.readline())      # First line
print(file.readline())      # Next line
file.close()

# Using with (Best Practice)
with open("sample.txt", "r") as f:
    data = f.read()
    print(data)
# No need to call f.close()

  