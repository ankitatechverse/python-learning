# --------------------------
# Multithreading
# --------------------------

"""
Multithreading = Running multiple threads within the same process.
Each thread can run independent tasks at the same time.
In Python, you use the threading module.

Think of it as workers sharing the same kitchen (memory space).

Best for I/O-bound tasks (network calls, file reads/writes, waiting for data).
Not good for CPU-heavy tasks in Python due to the GIL (Global Interpreter Lock) — only one thread can execute Python bytecode at a time.
If you need CPU parallelism, use multiprocessing, not threads.

When to Use?
1. Web scraping (parallel HTTP requests).
2. Reading/writing multiple files.
3. Handling multiple network connections (e.g., chat server).
"""
# Rules:-
"""
Always use .join() to wait for threads.
Use locks (threading.Lock) when modifying shared data.
Don’t use threads for CPU-bound work — GIL makes it pointless.
"""

# 1. Basic Example:-
import threading
import time

def worker(name):
    print(f"Thread {name} starting")
    time.sleep(2)
    print(f"Thread {name} finished")

# Create threads
t1 = threading.Thread(target=worker, args=("A",))
t2 = threading.Thread(target=worker, args=("B",))

# Start threads
t1.start()
t2.start()

# Wait for them to finish
t1.join()
t2.join()

print("All threads done!")

# ThreadPoolExecutor (Easier Way)
from concurrent.futures import ThreadPoolExecutor
import time

def worker(name):
    print(f"{name} starting")
    time.sleep(2)
    print(f"{name} finished")

with ThreadPoolExecutor(max_workers=3) as executor:
    executor.map(worker, ["A", "B", "C"])

# Threads with Shared Data
import threading

counter = 0
lock = threading.Lock()

def increment():
    global counter
    for _ in range(100000):
        with lock:  # Prevents race condition
            counter += 1

t1 = threading.Thread(target=increment)
t2 = threading.Thread(target=increment)

t1.start()
t2.start()
t1.join()
t2.join()

print(counter)  # Without lock: unpredictable, With lock: 200000
