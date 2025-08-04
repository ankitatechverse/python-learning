# --------------------------
# Multiprocessing
# --------------------------

"""
Threads share one Python process, but due to the GIL (Global Interpreter Lock), only one thread can execute Python code at a time.
Multiprocessing creates separate processes, each with its own Python interpreter & memory.
This means true parallel execution — perfect for CPU-heavy tasks (math, image processing, ML).

Think:
Threads = multiple cooks sharing one kitchen (but only one cooks at a time).
Processes = multiple kitchens, each with its own cook.
"""

# Rules:-
"""
Always use if __name__ == "__main__": on Windows (prevents recursive process spawn).
Use join() to wait for processes to finish.
Use Pool for batch work.
Use Manager or Queue to share data safely.
"""

# Threading vs Multiprocessing vs Async
"""
Threading: Good for I/O-bound, but GIL stops CPU parallelism.
Multiprocessing: Good for CPU-bound, true parallelism, separate memory.
Asyncio: Best for I/O-bound, lightweight, single-threaded but concurrent.
"""


from multiprocessing import Process
import os
import time

def worker(name):
    print(f"Worker {name} (PID {os.getpid()}) starting")
    time.sleep(2)
    print(f"Worker {name} finished")

if __name__ == "__main__":  # Required on Windows!
    p1 = Process(target=worker, args=("A",))
    p2 = Process(target=worker, args=("B",))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("All processes done!")

# Sharing Data Between Processes
from multiprocessing import Process, Value
import time

def increment(counter):
    for _ in range(1000):
        with counter.get_lock():  # prevent race
            counter.value += 1

if __name__ == "__main__":
    counter = Value('i', 0)  # shared integer
    processes = [Process(target=increment, args=(counter,)) for _ in range(5)]
    for p in processes: p.start()
    for p in processes: p.join()
    print("Final counter:", counter.value)



