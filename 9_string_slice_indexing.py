# --------------------------
# INDEXING
# --------------------------

# --- Rules of INDEXING ---
""""
# 1. Index starts at 0 (left to right).
# 2. Negative indexes start at -1 (right to left).
# 3. Accessing an out-of-range index raises IndexError.
"""

"""Examples:-"""

text = "Python"
print(text[0])    # First char: P
print(text[1])    # Second char: y
print(text[-1])   # Last char: n
print(text[-2])   # Second last char: o



# --------------------------
# SLICING
# --------------------------

# --- Rules of SLICING ---
"""
1. Syntax: text[start:end:step]
2. start → inclusive, end → exclusive.
3. step defines skipping (e.g., step=2 means every 2nd character).
4. Leaving start or end empty uses defaults (start=0, end=len(text)).
5. Negative step reverses the string.
""" 

"""Examples:-"""

word = "Programming"
print(len(word))   # Length: 11
print(word[0:6])   # From index 0 to (n-1)5 → "Progra"
print(word[3:])    # From index 3 to end → "gramming"
print(word[:6])    # From start to index 5 → "Progra"
print(word[-4:-3]) # From (length-4) to (length-3) → "mi"
print(word[::2])   # Every 2nd char → "Pormig"
print(word[::-1])  # Reverse string → "gnimmargorP"



# --------------------------
# ADVANCED SLICING
# --------------------------
alpha = "ABCDEFGHIJ"

print(alpha[2:8:2])   # From index 2 to 7, every 2nd → "CEG"
print(alpha[-5:-1])   # From -5 to -2 → "FGHI"
print(alpha[::-2])    # Reverse, every 2nd → "JHFDB"

# --------------------------
# MODIFYING STRINGS (WORKAROUND)
# --------------------------
# Strings are immutable, so you cannot directly assign:
# text[0] = "J"  # ❌ TypeError
# Instead, create a new one:
text = "Python"
new_text = "J" + text[1:]
print(new_text)  # "Jython"




