# --------------------------
# Generator
# --------------------------

# Rules
"""
A function that uses yield instead of return.
Produces values lazily → one at a time, only when needed.
Saves memory (doesn’t store all results at once).
next(generator) gets the next value.

You can loop directly:
def numbers():
    yield 1
    yield 2
    yield 3
for val in numbers():
    print(val)

Once exhausted, you can’t reuse a generator (need to recreate it).
Reading huge files.
Processing infinite sequences (e.g., Fibonacci numbers).
"""

# Normal function:
def numbers():
    return [1, 2, 3]
print(numbers())  # [1, 2, 3]

# Generator function:
def numbers():
    yield 1
    yield 2
    yield 3

gen = numbers()
print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3

# 2. Generator Expression (like list comprehension)
# Instead of:
nums = [x*x for x in range(10)]  # Creates full list in memory

# Use a generator expression:
nums = (x*x for x in range(10))  # Uses parentheses
print(next(nums))  # 0
print(next(nums))  # 1
