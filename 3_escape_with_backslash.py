# ==============================
# Python Escape Sequences Cheat Sheet
# =============================

# New line
print("Hello\nWorld")  # Moves text after \n to the next line

# Tab space
print("Hello\tWorld")  # Adds a horizontal tab between words

# Backslash
print("This is a backslash: \\")  # Prints a single backslash

# Double backslash
print("This is a double backslash: \\\\")  # Prints two backslashes

# Escaping quotes
print("She said \"Hello\"")  # Double quotes inside a double-quoted string
print('It\'s a beautiful day')  # Single quote inside a single-quoted string

# Carriage return (overwrites from start)
print("Hello\rWorld")  # "World" replaces "Hello"

# Backspace (removes previous character)
print("Hello\bWorld")  # Removes 'o' from Hello

# Unicode characters
print("Smile: \u263A")  # Prints ☺
print("Heart: \u2764")  # Prints ❤

# Octal and Hexadecimal
print("Octal: \110\145\154\154\157")  # "Hello" in octal
print("Hex: \x48\x65\x6C\x6C\x6F")   # "Hello" in hex

# Raw strings (no escaping)
print(r"C:\Users\Ankita\Documents")  # Prints path as is
print("C:\\Users\\Ankita\\Documents")

# Triple-quoted strings (multiline)
print("""This is
a multi-line
string with no escapes needed""")

