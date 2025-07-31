# --------------------------
# DICT/DIR/HELP Methods:-
# --------------------------

# Rules
"""
dir() → Full list of attributes & methods (exploration).
__dict__ → Instance variables only (good for debugging/serialization).
help() → Documentation (class, function, module).
"""

# 1. dir() – See What an Object Has
class Car:
    def __init__(self, brand):
        self.brand = brand
    def drive(self):
        print(f"{self.brand} is driving.")

c = Car("Tesla")
print(dir(c))

#2 __dict__ – See Object’s Data (Attributes Only)
print(c.__dict__)

#3 help() – Get Documentation
help(Car)        # Shows class info
help(c.drive)    # Shows method info
help(str)        # Built-in types


