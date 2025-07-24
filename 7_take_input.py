"""
Examples of taking user input in Python with type casting and validation.
"""

# --- 1. Simple String Input ---
input_str = input("Enter a Name: ")
print("Hello", input_str)


# --- 2. Input is always a string ---
num = input("Enter a number: ")
print(num, type(num))  # e.g., 25 <class 'str'>


# --- 3. Converting to Specific Types ---

# If you want an integer
age = int(input("Enter your age: "))
print(age, type(age))  # e.g., 25 <class 'int'>

# If you want a decimal
price = float(input("Enter price: "))
print(price, type(price))  # e.g., 99.5 <class 'float'>

# If you want a boolean (True/False)
is_active = input("Is active? (yes/no): ").strip().lower() == "yes"
print(is_active)  # True or False


# --- 4. Why Casting is Important ---
# Strings can't do math directly
num1 = input("Enter number: ")
num2 = input("Enter number: ")
print(num1 + num2)  # "5" + "6" = "56"  (string concatenation)

# Correct way: cast to int
num1 = int(input("Enter number: "))
num2 = int(input("Enter number: "))
print(num1 + num2)  # 5 + 6 = 11


# --- 5. Handling Invalid Input ---
try:
    num = int(input("Enter a number: "))
    print(f"You entered {num}")
except ValueError:
    print("Invalid number. Please try again.")


# --- Rules for Taking Input ---
"""
1. Whatever the user types is ALWAYS a string.
2. Even if you type 25, Python sees it as "25" (string).
3. If you need a number, always cast it using int() or float().
4. Use .strip() and .lower() when handling text inputs to avoid errors.
"""
