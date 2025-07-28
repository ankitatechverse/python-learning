# --------------------------
# Tupples
# --------------------------

# --- Rules ---
"""
1. Tuples are ordered & indexed like lists.
2. Immutable → you can’t change items once created.
3. Single-element tuples need a trailing comma.
4. Can contain other mutable objects (like lists).
5. Good for hashable keys (e.g., dictionary keys).
"""

# 1. Single-element tuple
single = (5,)
print(type(single))  # <class 'tuple'>

not_tuple = (5)
print(type(not_tuple))  # <class 'int'>  (NO comma → not a tuple)

# 2. Accessing & Slicing
fruits = ("apple", "banana", "cherry", "date")

print(fruits[0])      # "apple"
print(fruits[-1])     # "date"
print(fruits[1:3])    # ("banana", "cherry")
print(fruits[::-1])   # reverse → ("date", "cherry", "banana", "apple")

#3 Iterating
for fruit in fruits:
    print(fruit)

#4 Nesting
nested = ((1, 2), (3, 4))
print(nested[0][1])  # 2

#5 Unpacking
person = ("Genius", 25, "India")
name, age, country = person
print(name, age, country)  # Genius 25 India

#6 Immutability
t = (1, 2, 3)
# t[0] = 5   # ❌ TypeError: 'tuple' object does not support item assignment
# But: You can create a new tuple:

t = t + (4, 5)
print(t)  # (1, 2, 3, 4, 5)

