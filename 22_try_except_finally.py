# --------------------------
# try-except-finally
# --------------------------
"""
When Python code hits an error, it normally stops (crashes).
try-except lets you handle errors gracefully — you decide what happens instead of letting Python crash.

try → Place code that may raise an error.
except → Handle the error if it happens.
finally → Runs always, whether there’s an error or not (good for cleanup — like closing files or DB connections)

"""

# --- Rules ---
"""
1. Always put risky code in try.
2. Use specific except blocks (like ValueError, ZeroDivisionError) instead of a generic except.
3. finally always runs — perfect for cleanup tasks.
4. Use raise to throw custom or built-in errors when needed.
5. Custom errors should inherit from Exception.
"""

#1: Simple Try-Except
try:
    x = int(input("Enter a number for example 1: "))
    print(10 / x)
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("Invalid input. Please enter a number.")
finally:
    print("This will always run (cleanup code).")


#2: Multiple Exceptions
try:
    num = int("hello")  # This will fail
    print(10 / num)
except ValueError:
    print("Error: Cannot convert to int.")
except ZeroDivisionError:
    print("Error: Division by zero.")


#3: Catch All Exceptions
try:
    x = 10 / 0
except Exception as e:
    print("Something went wrong:", e)

""" Tip: Don’t overuse except Exception — it hides specific errors. Always prefer specific errors first."""

#4: finally Example
try:
    file = open("test.txt", "w")
    file.write("Hello!")
except Exception as e:
    print("Error:", e)
finally:
    file.close()  # Ensures file closes no matter what
    print("File closed.")


#5: Raising Custom Errors
def withdraw(amount):
    if amount > 1000:
        raise ValueError("Amount too high! Max limit is 1000.")
    return amount

try:
    print(withdraw(1500))
except ValueError as e:
    print("Custom Error:", e)

#6: Creating a Custom Exception Class
class MyCustomError(Exception):
    """Custom error for specific situations"""
    pass

def process_data(data):
    if not data:
        raise MyCustomError("Data cannot be empty!")

try:
    process_data("")
except MyCustomError as e:
    print("Caught custom error:", e)




