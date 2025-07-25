# --------------------------
# MATCH (Python 3.10+)
# --------------------------

# --- Rules ---
"""
1. match works like switch in other languages.
2. case patterns are checked top to bottom.
3. _ (underscore) acts as default (like else).
4. Can match values, types, even patterns (tuples, lists).
"""

"""Examples:-"""

command = input("Enter command: ")

match command:
    case "start":
        print("System starting...")
    case "stop":
        print("System stopping...")
    case "restart":
        print("System restarting...")
    case _:
        print("Unknown command.")
