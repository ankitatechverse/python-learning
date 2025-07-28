# --------------------------
# Recursion
# --------------------------

# --- Rules ---
"""
1. Recursion means: A function calls itself to solve smaller versions of a problem.
2. It continues until it hits a base case, which stops the loop.
3. Always define a base case.
4. Recursive call must move toward the base case.
5. Python has a recursion limit (usually ~1000). Use sys.setrecursionlimit() to change it (carefully).
"""

def factorial(n):
    if n == 0:
        return 1              # 🔹 Base case
    else:
        return n * factorial(n - 1)  # 🔁 Recursive call

print(factorial(5))  # 120 → 5 * 4 * 3 * 2 * 1

# 🧠 How it works (visual for factorial(3)):
"""
factorial(3)
→ 3 * factorial(2)
      → 2 * factorial(1)
            → 1 * factorial(0)
                  → 1 (base case)
Then it returns back:
factorial(0) = 1
factorial(1) = 1 * 1 = 1
factorial(2) = 2 * 1 = 2
factorial(3) = 3 * 2 = 6
"""

# 1. Sum of numbers (n + n-1 + ... + 1)
def recursive_sum(n):
    if n == 1:
        return 1
    return n + recursive_sum(n - 1)

print(recursive_sum(5))  # 15

# 2. Reverse a string
def reverse(s):
    if len(s) == 0:
        return ""
    return s[-1] + reverse(s[:-1])

print(reverse("hello"))  # "olleh"

# 3. Fibonacci series
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(6))  # 8 (0, 1, 1, 2, 3, 5, 8)



