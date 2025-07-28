# --------------------------
# Dictionaries 
# --------------------------

# --- Rules ---
""" 
A dictionary is:
- A collection of key-value pairs.
- Mutable (you can add, update, or delete).
- Keys are unique and must be immutable (e.g., strings, numbers, tuples)."""

# In short:
"""
Dictionaries themselves are mutable → you can add, update, or remove keys/values.
Dictionary keys must be immutable (so they don’t change after being created).
Dictionary values can be mutable (list, set, another dict) or immutable.
"""

person = {
    "name": "Genius",
    "age": 25,
    "country": "India"
}
print(person["name"])  # Genius

# 1. Creating Dictionaries
person = {"name": "Genius", "age": 25}
user = dict(name="John", age=30)
empty = {}

# 2. Accessing Values
print(person["name"])       # Genius
print(person.get("city"))   # None (doesn’t crash if key missing)
print(person.get("city", "Unknown"))  # Default value → "Unknown"

# 3. Adding & Updating
person["city"] = "Mumbai"  # Add new key
person["age"] = 26         # Update value
print(person)

# 4. Removing
person.pop("city")        # Remove by key
del person["age"]         # Delete by key
person.clear()            # Empty the dictionary

# 5. Iterating

person = {"name": "Genius", "age": 25}

for key in person:
    print(key, person[key])   # name Genius, age 25

for key, value in person.items():
    print(key, value)         # name Genius, age 25

# 6. Dictionary Methods
person = {"name": "Genius", "age": 25}
print(person.keys())     # dict_keys(['name', 'age'])
print(person.values())   # dict_values(['Genius', 25])
print(person.items())    # dict_items([('name', 'Genius'), ('age', 25)])

# 7. Nesting (Dict inside Dict)
users = {
    "user1": {"name": "Alice", "age": 20},
    "user2": {"name": "Bob", "age": 25}
}
print(users["user1"]["name"])  # Alice

# 8. Dictionary Comprehension
squares = {x: x**2 for x in range(1, 6)}
print(squares)  # {1:1, 2:4, 3:9, 4:16, 5:25}





