# --------------------------
# == vs is
# --------------------------

# --- Rules ---
"""
== → Value equality → Checks if the contents/values are the same.
is → Identity equality → Checks if both variables point to the exact same object in memory.

1. is → identity check (same object in memory).
2. == → value equality (contents).
3. Use is for None checks: if x is None.
4. Don’t use is for strings/numbers unless you specifically want to check identity (rare).
"""

# 1. Basic Example
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # True (values are same)
print(a is b)  # False (different objects in memory)

# 2. is for Singletons (Special Case)
# Use is for unique objects like None, True, False.
x = None
print(x is None)  # ✅ Correct
print(x == None)  # Works, but not Pythonic

# 3. Immutable Types & Interning
# Python reuses some small immutable objects (like small integers & short strings) for efficiency.
# This means is might seem to work sometimes by coincidence.

a = 256
b = 256
print(a is b)  # True (Python caches small ints)

a = 257
b = 257
print(a is b)  # False (not cached)


# Same for short strings:
x = "hello"
y = "hello"
print(x is y)  # True (string interning)
# But:
x = "hello world!"
y = "hello world!"
print(x is y)  # Might be False (longer strings may not be interned)

# 4. Mutable Types
# For lists, dicts, sets — even if values are equal, is will almost always be False unless you explicitly assign one to another.
list1 = [1, 2]
list2 = [1, 2]
print(list1 == list2)  # True
print(list1 is list2)  # False

list3 = list1
print(list1 is list3)  # True (same object)

# 5. Comparing Custom Objects
# By default, == uses is (identity) for custom objects unless you override __eq__.
class A:
    pass

obj1 = A()
obj2 = A()

print(obj1 == obj2)  # False (no __eq__ defined)
print(obj1 is obj2)  # False (different objects)
print(obj1 is obj1)  # True






