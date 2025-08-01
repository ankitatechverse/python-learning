# --------------------------
# Time-related utilities
# --------------------------

"""
Python gives you two main ways to handle time:
The time module (low-level, works with timestamps).
The datetime module (high-level, human-friendly).
"""
# Using the time module
import time
print(time.time())  # Seconds since 

# 1. Pause / Sleep
print("Start")
time.sleep(2)   # Pause for 2 seconds
print("End")

# 2. Get Readable Local Time
print(time.ctime())   # Current local time

# 3. Convert to Struct (Detailed Time Info)
t = time.localtime()  # Get structured local time
print(t)
print(t.tm_year, t.tm_mon, t.tm_mday)  # Access specific parts

# 4. Format Time
t = time.localtime()
print(time.strftime("%Y-%m-%d %H:%M:%S", t))  # Format: 2025-07-29 14:30:21

# 5. Parse String → Struct Time
time_str = "2025-07-29 14:30:21"
t = time.strptime(time_str, "%Y-%m-%d %H:%M:%S")
print(t)

# 6. Get Performance Timing
start = time.perf_counter()
# Your code here
end = time.perf_counter()
print(f"Execution time: {end - start} seconds")


