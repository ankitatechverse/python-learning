# --------------------------
# Define a function
# --------------------------

# --- Rules ---
"""
1. Functions are defined with def name():.
2. They can take parameters and return values using return.
3. Function names should be lowercase with underscores (PEP8 style).
"""

"""Examples:-"""

# Basic Function
def greet():
    print("Hello, Genius!")

greet()

# Function with Return
def add(a, b):
    return a + b

result = add(5, 7)
print(result)  # 12

# Function Arguments: 4 Types
# --- Rules ---
"""
1. Positional args must come before keyword args.
2. Default args must come after positional args.
3. *args collects extra positional args.
4. **kwargs collects extra keyword args.
5. Order: positional → default → *args → **kwargs.
6. Default values are evaluated once at function definition.
7. Use return to send a value back; if no return, it returns None.
"""

##Positional Arguments
# You must pass arguments in the same order they are defined.
def person_info(name, age):
    print(f"My name is {name} and I am {age} years old.")

person_info("Genius", 25)  
# My name is Genius and I am 25 years old.

##Keyword Arguments
# You can pass arguments by name, ignoring order.
def person_info(name, age):
    print(f"My name is {name} and I am {age} years old.")

person_info(age=25, name="Genius")  
# My name is Genius and I am 25 years old.

##Default Arguments
#If you don’t pass a value, it uses the default.

def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()          # Hello, Guest!
greet("Genius")  # Hello, Genius!

##Variable-Length Arguments 
###A. *args → Multiple Positional
def add_numbers(*args):
    print(args)          # Tuple of values
    print(sum(args))     # Sum them

add_numbers(1, 2, 3, 4)  
# (1, 2, 3, 4)
# 10

###B. **kwargs → Multiple Keyword
def print_details(**kwargs):
    print(kwargs)  # Dictionary of key-value pairs
    for key, value in kwargs.items():
        print(f"{key} = {value}")

print_details(name="Genius", age=25, city="Mumbai")
# {'name': 'Genius', 'age': 25, 'city': 'Mumbai'}
# name = Genius
# age = 25
# city = Mumbai


# Combining All
def mix_example(a, b=10, *args, **kwargs):
    print(f"a={a}, b={b}")
    print("args:", args)
    print("kwargs:", kwargs)

mix_example(1, 20, 30, 40, city="Mumbai", country="India")
# a=1, b=20
# args: (30, 40)
# kwargs: {'city': 'Mumbai', 'country': 'India'}



