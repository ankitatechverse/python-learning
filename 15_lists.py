# --------------------------
# List
# --------------------------

# --- Rules ---
"""
1. Mutable → You can change them (add, remove, update).
2. Ordered → Items maintain insertion order.
3. Can contain duplicates → Same value can appear multiple times.
4. Can hold mixed data types.
5. Indexing & slicing works like strings.Use copy() or list() to avoid accidental reference sharing.
"""

"""Examples:-"""

# Creating lists
numbers = [1, 2, 3, 4]
mixed = [1, "Python", 3.14, True]

print(numbers)  # [1, 2, 3, 4]
print(mixed)    # [1, 'Python', 3.14, True]

# 1. Accessing & Slicing
fruits = ["apple", "banana", "cherry", "date"]
print(fruits[0])     # "apple"
print(fruits[-1])    # "date"
print(fruits[1:3])   # ["banana", "cherry"]
print(fruits[::-1])  # reverse → ["date", "cherry", "banana", "apple"]

# 2. Adding & Removing
fruits = ["apple", "banana"]

fruits.append("cherry")       # Add at end
fruits.insert(1, "mango")     # Insert at index
print(fruits)  # ['apple', 'mango', 'banana', 'cherry']

fruits.remove("banana")       # Remove by value
popped = fruits.pop()         # Remove last item
print(popped)   # 'cherry'
del fruits[0]                 # Delete by index
print(fruits)   # ['mango']

# 3. Updating
fruits = ["apple", "banana", "cherry"]
fruits[1] = "blueberry"
print(fruits)  # ['apple', 'blueberry', 'cherry']

# 4. Iterating
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

# With index
for i, fruit in enumerate(fruits):
    print(i, fruit)

# 5. Sorting & Reversing
numbers = [3, 1, 4, 2]
numbers.sort()         # In-place sort
print(numbers)         # [1, 2, 3, 4]

numbers.sort(reverse=True)
print(numbers)         # [4, 3, 2, 1]

numbers.reverse()      # Just reverse
print(numbers)         # [1, 2, 3, 4] (reversed again)

# 6. List Comprehensions
squares = [x**2 for x in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]

# 7. Copying
list1 = [1, 2, 3]
list2 = list1          # ❌ Points to same list
list3 = list1.copy()   # ✅ Makes a shallow copy

list1.append(4)
print(list2)  # [1, 2, 3, 4] (changes affect list2)
print(list3)  # [1, 2, 3]   (independent)

# 8. Nested Lists

matrix = [[1, 2], [3, 4], [5, 6]]
print(matrix[0][1])  
# Output:- 2 
# matrix[i] → Picks the i-th row (sublist).
# matrix[i][j] → Picks the j-th element inside that row.




