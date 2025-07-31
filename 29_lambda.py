# --------------------------
# Lambda Function
# --------------------------

# --- Rules ---
"""
A lambda is a small anonymous function in Python.
Instead of using def to create a function, you can create a one-liner with lambda.

1. Single expression only (no multiple statements).
2. Automatically returns the expression — no return needed.
3. Great for short, throwaway functions (especially with map, filter, sorted).
4. Don’t overuse — if function is complex, use def.

# When to Use Lambda:-
=> One-line operations.
=> Inline functions for map(), filter(), sorted().
=> Quick custom keys in sorting/grouping.

#Syntax:
lambda arguments: expression
=>lambda → keyword
=>arguments → input parameters (can be 0 or more)
=>expression → single expression (automatically returned)
"""

# 1. Basic Example
add = lambda a, b: a + b
print(add(5, 3))

# 2. No Arguments
say_hello = lambda: "Hello Genius"
print(say_hello())

# 3. One Argument
square = lambda x: x ** 2
print(square(6))

# 4. With Conditional (Ternary)
is_even = lambda x: "Even" if x % 2 == 0 else "Odd"
print(is_even(7))

# 5. Sorting with Lambda
numbers = [(1, 'one'), (3, 'three'), (2, 'two')]
sorted_list = sorted(numbers, key=lambda x: x[0])
print(sorted_list)

# 6. Using map() with Lambda
nums = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 2, nums))
print(squared)

# 7. Using filter() with Lambda
nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)


# 8. Using reduce() with Lambda
from functools import reduce
nums = [1, 2, 3, 4]
sum_all = reduce(lambda a, b: a + b, nums)
print(sum_all)






