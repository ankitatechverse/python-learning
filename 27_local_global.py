# --------------------------
# Local/Global Variable
# --------------------------

# --- Rules ---
"""
1. A local variable is declared inside a function and can only be used inside that function.
2. Variables inside functions are local by default.
3. Use global to change global variables inside a function.
4. Use nonlocal to change variables in enclosing (but non-global) functions.
5. Be careful with global variables — too many globals make code messy.
"""

# Example 1:-  Local Variable
def my_func():
    x = 10  # Local variable
    print(x)

my_func()

# Example 2:-  Global Variable
x = 20  # Global variable

def my_func():
    print(x)  # Can access global variable inside function

my_func()
print(x)  # Works here too


# Example 3:- When Local & Global Variables Have Same Name
x = 50  # Global

def my_func():
    x = 10  # Local (hides global)
    print("Inside:", x)

my_func()
print("Outside:", x)

# Example 4:-  Changing a Global Variable Inside a Function
x = 5

def change_global():
    global x
    x = 100

change_global()
print(x)  # Output: 100

# Example 5:-  Nested Functions & nonlocal
def outer():
    x = 10
    def inner():
        nonlocal x
        x = 20
    inner()
    print(x)

outer()  # Output: 20




