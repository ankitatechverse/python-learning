# --------------------------
# Walrus Operator
# --------------------------

"""
It’s := introduced in Python 3.8.
It allows you to assign a value to a variable while using it in an expression.
Can’t use it at the top level (like x := 5 by itself). Must be inside an expression.
Use for clarity, not cleverness — overuse makes code confusing.
"""

# without
value = input("Enter something: ")
if value != "":
    print(f"You typed: {value}")

# with walrus operator
if (value := input("Enter something: ")) != "":
    print(f"You typed: {value}")


# Example 1: While Loop
# Old way:
line = input("Enter text: ")
while line != "":
    print(f"You said: {line}")
    line = input("Enter text: ")

# Walrus way:
while (line := input("Enter text: ")) != "":
    print(f"You said: {line}")

# Example 2: Filtering in Comprehensions
# Old way:

results = []
for num in range(10):
    square = num * num
    if square > 10:
        results.append(square)
print(results)

# Walrus way:
results = [square for num in range(10) if (square := num * num) > 10]
print(results)

# Example 3: Avoiding Duplicate Function Calls
# Old way:
name="Gennie"
if len(name) > 5:
    print(len(name))
# Walrus way:
if (name_length := len(name)) > 5:
    print(name_length)