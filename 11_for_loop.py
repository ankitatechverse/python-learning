# --------------------------
# FOR LOOP
# --------------------------

# --- Rules ---
"""
1. for loops iterate over a sequence (like a list, string, or range).
2. range(start, stop, step) is often used for numeric loops.
3.Use enumerate() when you need index + value.
"""

"""Examples:-"""

# Looping over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Using range()
for i in range(1, 6):  # 1 to 5
    print(i)

# Loop with index
for index, fruit in enumerate(fruits):
    print(index, fruit)

# Nested loops
for i in range(1, 4):  # Outer loop
    for j in range(1, 4):  # Inner loop
        print(f"i: {i} j:{j}")

