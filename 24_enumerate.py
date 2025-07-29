# --------------------------
# Enumerate
# --------------------------

"""
It’s a built-in Python function that adds a counter (index) to an iterable (like list, tuple, string) 
and returns it as an enumerate object.

enumerate(iterable, start=0)
- iterable → The list, tuple, or string you want to loop through.
- start → The starting index (default is 0).
"""

# --- Rules ---
"""
1. Cleaner than manually tracking indexes.
2. Makes code short and readable.
3. Works with any iterable (lists, tuples, strings, etc.).
"""

# Example 1:- Basic Usage
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(index, fruit)

# Example 2:- Custom Starting Index
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)

# Example 3:- Using with Strings
for index, char in enumerate("hello"):
    print(index, char)

# Example 4:-  Getting Enumerate as a List
result = list(enumerate(fruits))
print(result)


subjects = ["Math", "Science", "History", "English"]
for index, subject in enumerate(subjects, start=1):
    print(index, subject)





