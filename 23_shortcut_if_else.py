# --------------------------
# Shortcut If-Else
# --------------------------

"""
value_if_true if condition else value_if_false
"""

# --- Rules ---
"""
1. When the logic is simple (one-liner decisions).
2. For assigning values based on conditions quickly.
"""

# Example 1: Basic
age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)


# Example 2: Using in Print
num = 5
print("Even" if num % 2 == 0 else "Odd")

# Example 3: Nested Shorthand
x = 0
result = "Positive" if x > 0 else "Negative" if x < 0 else "Zero"
print(result)


