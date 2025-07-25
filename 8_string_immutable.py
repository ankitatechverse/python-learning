# ---------------------------
# PYTHON STRING CHEAT SHEET
# ---------------------------

# --- Rules of Strings ---
"""
1. Strings are immutable → you cannot change them in place.
2. All modifications create a new string (concatenation, replace, etc.).
3. Indexing and slicing are allowed but return new strings, not modify originals.
4. Strings are iterable → you can loop over characters.
5. Strings can be compared (case-sensitive by default).
6. Use .strip() to remove spaces, .lower() or .casefold() for case-insensitive checks.
"""

"""Examples:-"""

# 1. One-page String Methods Cheat Sheet
s = "  Hello World !! "

# --- BASIC METHODS ---
print(s.strip())       # Remove spaces: "Hello World"
print(s.lstrip())      # Remove leading spaces: "Hello World  !!"
print(s.rstrip())     # Remove trailing spaces: "  Hello World  !!"
print(s.strip("!"))    # Remove spaces: "Hello World"
print(s.upper())       # Uppercase: "  HELLO WORLD  "
print(s.lower())       # Lowercase: "  hello world  "
print(s.title())       # Title case: "  Hello World  "
print(s.capitalize())  # First letter capitalized: "  hello world  "

# --- SEARCHING ---
print(s.find("World"))  # Index of substring: 8
print(s.startswith("  H"))  # True
print(s.endswith("y  "))    # True

# --- REPLACE & SPLIT ---
print(s.replace("World", "Python"))  # "  Hello Python  "
print(s.split())       # ['Hello', 'World']
print("-".join(["One", "Two"]))  # "One-Two"


# --- FORMATTING ---
name = "Genius"
age = 25
print(f"My name is {name} and I am {age} years old.")  # f-string
print("My name is {} and I am {}".format(name, age))  # format method

# --- CHECKING ---
print(s.isalpha())     # False (spaces)
print("hello".isalpha())  # True
print("123".isdigit())    # True
print(" ".isspace())      # True



#2. Visual Diagram: String Immutability
# Demonstrating String Immutability
s = "Hello"
print("Before Change:")
print("Value:", s)
print("Memory ID:", id(s))  # ID before modification

# Concatenating (creates new string)
s = s + " World"
print("\nAfter Concatenation:")
print("Value:", s)
print("Memory ID:", id(s))  # New ID (different object)

#Using .casefold() => .casefold() is like .lower() but more aggressive (better for case-insensitive comparison in international text).
s1 = "Straße"      # German sharp S
s2 = "strasse"
print(s1.lower() == s2)    # False
print(s1.casefold() == s2) # True
#For case-insensitive comparisons in multi-language text.



