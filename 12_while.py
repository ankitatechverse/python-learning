# --------------------------
# WHILE LOOP
# --------------------------

# --- Rules ---
"""
1.Runs as long as the condition is True.
2.Be careful to update variables inside the loop to prevent infinite loops.
3.Use break to stop early, continue to skip current iteration.
"""

"""Examples:-"""

# Basic while loop
count = 1
while count <= 5:
    print(count)
    count += 1

#Using break (exit loop early)
print("Break example")
count = 1
while count <= 10:
    if count == 6:
        print("Breaking at 6")
        break   # exits loop immediately
    print(count)
    count += 1


#Using continue (skip iteration)
print("continue example")
count = 0
while count < 10:
    count += 1
    if count % 2 == 0:
        continue  # skip even numbers
    print(count)

