# --------------------------
# Doc String
# --------------------------

# --- Rules ---
"""
1. Always use triple double quotes.
2. First line: Short summary (one-liner).
3. Leave a blank line, then detailed description (if needed).
4. Document parameters, return values, and exceptions.
5. Keep it clear & concise (like explaining to another dev).
6. Documentation: Makes code easier for others (and you) to understand.
"""

def greet(name):
    """
    Greets the user with their name.
    
    Args:
        name (str): The name of the user.
    
    Returns:
        str: A greeting message.
    """
    return f"Hello, {name}!"

print(greet.__doc__)

# 2. Module-Level Docstring
# Put at the top of your Python file:
"""
This module handles user authentication.
It includes functions for login, logout, and password reset.
"""

# 3. Class & Method Docstrings
class Calculator:
    """Performs basic math operations."""

    def add(self, a, b):
        """
        Adds two numbers.
        Args:
            a (int/float): First number.
            b (int/float): Second number.
        Returns:
            int/float: Sum of a and b.
        """
        return a + b
    
# 4. Accessing Docstrings
print(Calculator.__doc__)       # Class docstring
print(Calculator.add.__doc__)   # Method docstring

# 5. Multi-line Docstrings
# Use triple quotes (""" or '''):
def divide(a, b):
    """
    Divides a by b.
    
    Raises:
        ZeroDivisionError: If b is zero.
    """
    return a / b



