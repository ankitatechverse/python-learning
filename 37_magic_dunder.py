# --------------------------
# Magic Dunder Methods
# --------------------------

"""
Magic methods = special methods in Python that start and end with double underscores (__method__).
They change how objects behave for built-in operations (like +, len(), str() etc.).
Dunder = “Double UNDERscore”.
"""

#Rules:-
"""
Always implement __repr__ for debugging.
Use __str__ for user-friendly output.
Don’t overuse (keep behavior intuitive).
"""

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):  # For print()
        return f"{self.name} scored {self.marks}"

    def __repr__(self):  # For debugging
        return f"Student({self.name!r}, {self.marks!r})"

    def __eq__(self, other):  # Compare students
        return self.marks == other.marks

    def __lt__(self, other):  # Sorting
        return self.marks < other.marks

    def __add__(self, other):  # Add marks
        return self.marks + other.marks

s1 = Student("Alice", 85)
s2 = Student("Bob", 90)

print(s1)             # __str__: Alice scored 85
print(repr(s1))       # __repr__: Student('Alice', 85)
print(s1 == s2)       # __eq__: False
print(s1 + s2)        # __add__: 175
print(s1 < s2)        # __lt__: True
