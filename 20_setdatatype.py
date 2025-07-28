# --------------------------
# Set Data Type in Python
# --------------------------

# --- Rules ---
"""A set is:
Unordered (no index positions).
Mutable (you can add/remove items).
Unique (no duplicates)."""

# When to Use Sets?
"""
Removing duplicates from a list.
Checking membership fast (faster than lists).
Performing mathematical operations like union & intersection.s
"""

my_set = {1, 2, 3, 3}
print(my_set)  # {1, 2, 3}  (duplicates removed)

# 1. Creating Sets
# Using curly braces
nums = {1, 2, 3}

# Using set() function
empty = set()    # {} would create a dict, not a set
mixed = {1, "Python", True}

# 2. Adding & Removing Elements
fruits = {"apple", "banana"}

fruits.add("cherry")       # Add single
print(fruits)  # {'apple', 'banana', 'cherry'}

fruits.update(["mango", "grape"])  # Add multiple
print(fruits)

fruits.remove("banana")    # Remove (error if not present)
fruits.discard("xyz")      # Remove safely (no error)
popped = fruits.pop()      # Remove random element
print(popped)

fruits.clear()            # Clear all elements

# 3. Set Operations
# Sets are great for math-like operations:
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)   # Union → {1, 2, 3, 4, 5}
print(a & b)   # Intersection → {3}
print(a - b)   # Difference → {1, 2}
print(a ^ b)   # Symmetric Difference → {1, 2, 4, 5}

# 4. Membership
nums = {1, 2, 3}
print(2 in nums)   # True
print(5 in nums)   # False

# 5. Copying
a = {1, 2, 3}
b = a.copy()
a.add(4)
print(a)  # {1, 2, 3, 4}
print(b)  # {1, 2, 3}

# 6. Frozen Set (Immutable Set)
# If you want a set you can’t modify:
frozen = frozenset([1, 2, 3])
# frozen.add(4)  # ❌ Error



