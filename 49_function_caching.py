# --------------------------
# Function Caching
# --------------------------

"""
function caching in Python is all about storing (caching) results of function calls, so if you call the same function with the same inputs again, Python can return the cached value instead of recalculating.
This saves time for expensive operations (e.g., API calls, heavy computations).

When to Use Caching:-
1. Functions with repeated inputs.
2. Expensive computations (math, DB queries, API calls).
3. Pure functions (same input → same output).

When NOT to Use
1. If function depends on changing data (e.g., current time, random values).
2. If inputs are large/unhashable (e.g., lists/dicts — cache requires hashable arguments).
"""

# 1. Basic Example:-
from functools import lru_cache
import time

@lru_cache(maxsize=None)  # Unlimited cache
def slow_function(n):
    time.sleep(2)  # Simulate heavy work
    return n * n

print(slow_function(4))  # Takes 2 seconds
print(slow_function(4))  # Instant (cached)

# 2.Parameters

"""
@lru_cache(maxsize=128)
maxsize: How many results to store (oldest results are dropped if exceeded).
None: Unlimited cache.
"""

# 3.Clearing Cache
slow_function.cache_clear()
print(slow_function(5))  # Takes 2 seconds

# 4.Real Example: Fibonacci
# Without caching:
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

# With caching:
@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

print(fib(35))  # Much faster!
print(fib(35))  # Much faster!




