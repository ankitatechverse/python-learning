# --------------------------
# IF / ELSE STATEMENTS
# --------------------------

# --- Rules ---
""""
1. if checks the first condition.
2. elif checks additional conditions (optional).
3. else runs if none of the above match.
4. Indentation (4 spaces) is mandatory in Python.
5. Conditions can use and, or, not.
"""

"""Examples:-"""
age = int(input("Enter your age: "))
if age < 18:
  print("You are a minor.")
elif 18 <= age < 60:
  print("You are an adult.")
else:
  print("You are a senior citizen.")
