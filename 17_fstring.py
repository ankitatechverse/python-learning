# --------------------------
# F-Strings
# --------------------------

# --- Rules ---
"""
1. Prefix string with f or F.
2. Anything inside { } is evaluated as Python code.
3. You can format numbers/dates with : (mini-format spec).
4. Works with variables, expressions, functions, and even nested f-strings.
5. Introduced in Python 3.6.
"""

name = "Genius"
age = 25
print(f"My name is {name} and I am {age} years old.")
# My name is Genius and I am 25 years old.

#1. Variables inside f-strings
x = 10
y = 5
print(f"Sum of {x} and {y} is {x + y}")  # Sum of 10 and 5 is 15

#2. Expressions inside f-strings
print(f"Next year I’ll be {age + 1}")
# Next year I’ll be 26

#3. Function calls inside f-strings
def greet(name):
    return f"Hello, {name}!"

print(f"{greet('Genius')}")
# Hello, Genius!

#4 Formatting Numbers
pi = 3.14159265
print(f"Pi rounded: {pi:.2f}")     # Pi rounded: 3.14
print(f"With padding: {pi:8.3f}")  # '   3.142' (width 8, 3 decimals)

#5 Date & Time Formatting
from datetime import datetime
today = datetime.now()
print(f"Today is {today:%Y-%m-%d}")
# Today is 2025-07-28

#6 Debugging (Python 3.8+)
value = 42
print(f"{value=}")  # value=42

#7 Multi-line f-strings
name = "Genius"
age = 25
info = f"""
Name: {name}
Age: {age}
"""
print(info)








