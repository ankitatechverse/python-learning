# --------------------------
# Import a Module
# --------------------------

# --- Rules ---
"""
1. Use meaningful names for modules.
2. Use aliases (as) for long names.
3. Use specific imports if you only need a few functions.
4. Avoid from module import * unless absolutely necessary.
"""

# Example 1:- Import the Whole Module
import math
print(math.sqrt(16))  # Output: 4.0


# Example 2:- Import with an Alias
import math as m
print(m.sqrt(25))  # Output: 5.0


# Example 3:- Import Specific Functions
from math import sqrt, pi
print(sqrt(9))   # Output: 3.0
print(pi)        # Output: 3.141592653589793

# Example 4:- Import Everything (Not Recommended)
from math import *
print(sqrt(36))  # Output: 6.0
# Avoid this because it may cause naming conflicts.


