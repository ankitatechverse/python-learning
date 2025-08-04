# --------------------------
# asyncio
# --------------------------

"""
1. A Python library for writing asynchronous (non-blocking) code.
2. Lets you run many tasks at the same time (concurrency) without threads.
3. Perfect for I/O-heavy work (e.g., APIs, DB calls, file reads) — not for CPU-heavy work.

“Instead of waiting for one task to finish (like downloading a file), I can switch to another task in the meantime.”
"""

import time

def fetch_data():
    time.sleep(2)   # Blocking (doing nothing for 2s)
    return "Data"

print(fetch_data())

# Async (non-blocking) code:
import asyncio

# async def fetch_data():
#     await asyncio.sleep(2)   # Non-blocking (yields control)
#     return "Data"

# async def main():
#     results = await asyncio.gather(fetch_data(), fetch_data(), fetch_data())
#     print(results)

# asyncio.run(main())


# Full Example: Multiple API Calls
import random

# async def fetch_data(name):
#     print(f"Fetching {name}...")
#     await asyncio.sleep(random.randint(1, 3))  # Simulate network delay
#     print(f"Done {name}")
#     return f"Data from {name}"

# async def main():
#     tasks = [fetch_data("API1"), fetch_data("API2"), fetch_data("API3")]
#     results = await asyncio.gather(*tasks)
#     print("Results:", results)

# asyncio.run(main())

# Full Example: Multiple API Calls


# async def fetch_data(name):
#     print(f"Fetching {name}...")
#     await asyncio.sleep(random.randint(1, 3))  # Simulate network delay
#     print(f"Done {name}")
#     return f"Data from {name}"

# async def main():
#     tasks = [fetch_data("API1"), fetch_data("API2"), fetch_data("API3")]
#     results = await asyncio.gather(*tasks)
#     print("Results:", results)

# asyncio.run(main())

# # Running Tasks in Parallel
# async def task(name, delay):
#     await asyncio.sleep(delay)
#     return f"{name} finished"

# async def main():
#     tasks = [task("A", 2), task("B", 1), task("C", 3)]
#     for future in asyncio.as_completed(tasks):
#         result = await future
#         print(result)

# asyncio.run(main())

import asyncio
import random

async def fetch_api(name):
    print(f"Fetching {name}...")
    await asyncio.sleep(random.randint(1, 3))  # simulate API delay
    print(f"Done {name}")
    return f"{name} data"

async def main():
    # Run all at the same time
    results = await asyncio.gather(fetch_api("API1"), fetch_api("API2"), fetch_api("API3"))
    print(results)

asyncio.run(main())


async def create_user():
    await asyncio.sleep(1)
    print("User created")
    return 123  # user ID

async def send_email(user_id):
    await asyncio.sleep(1)
    print(f"Email sent to user {user_id}")

async def log_event(user_id):
    await asyncio.sleep(1)
    print(f"Event logged for user {user_id}")

async def main():
    user_id = await create_user()
    await send_email(user_id)
    await log_event(user_id)

asyncio.run(main())



