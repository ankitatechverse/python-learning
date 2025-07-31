# --------------------------
# OOPs, Classes, and Objects
# --------------------------

# --- Rules ---
"""
Class → A blueprint for creating objects.
Object → An instance of a class (real data created from the blueprint).

Think:
Class = Design of a Car
Object = Actual car built from that design
"""
#Syntax:-

class ClassName:
    def __init__(self, param1, param2):  # Constructor
        self.param1 = param1
        self.param2 = param2

    def some_method(self):
        print(f"Working with {self.param1} and {self.param2}")

obj = ClassName("value1", "value2")
obj.some_method()

#Key Concepts:-
"""
Constructor (__init__):-
  Runs automatically when an object is created.
  Initializes attributes.
"""

class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

car1 = Car("Tesla", 120)
print(car1.brand)     # Tesla
car1.speed = 150      # Modify
print(car1.speed)     # 150

# Class vs Instance Methods:-
# 1. Instance Method:-
"""
=> Default method type in a class.
=> First parameter is always self (the object itself).
Can access:
=> Instance attributes (self.attr)
Class attributes
=> Called on an object (instance).
"""

# Example:
class Car:
    wheels = 4  # Class attribute

    def __init__(self, brand, speed):
        self.brand = brand        # Instance attribute
        self.speed = speed

    def drive(self):              # Instance method
        print(f"{self.brand} is driving at {self.speed} km/h with {Car.wheels} wheels.")

car1 = Car("Tesla", 120)
car1.drive()  # Tesla is driving at 120 km/h with 4 wheels.

# 2. class Method:-
"""
1. Defined with @classmethod decorator.
2. First parameter is cls (the class itself, not an object).
3. Can access/modify class-level attributes (shared by all instances).
4. Called on the class itself (or on an object, but still receives the class).
"""
# Example:
class Car:
    wheels = 4

    def __init__(self, brand):
        self.brand = brand

    @classmethod
    def change_wheels(cls, count):   # Class method
        cls.wheels = count
        print(f"All cars now have , {cls.wheels} wheels.")

Car.change_wheels(8)  # Change for all cars

car1 = Car("Tesla")
car2 = Car("BMW")
car1.wheels = 6
print(car1.wheels)  # 6
print(car2.wheels)  # 6

#Alternative Constructor Example:-
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @classmethod
    def from_string(cls, data):  # Alternative constructor
        name, marks = data.split('-')
        return cls(name, int(marks))

s1 = Student.from_string("Alice-90")
print(s1.name, s1.marks)  # Alice 90

#3 Static Methods (for context)
"""
Defined with @staticmethod.
No self or cls.
Behaves like a regular function, but grouped inside a class for organization.
"""

class MathHelper:
    @staticmethod
    def add(a, b):
        return a + b

print(MathHelper.add(5, 3))  # 8

"""
Instance Method → When you need to work with object-specific data.
Class Method → When you need to work with class-wide data or need alternative constructors.
Static Method → When you need a utility function that doesn’t touch instance or class state.
"""

# Rules:-
"""
Class method → Always has cls. Works with class attributes, creates alternative constructors.
Instance method → Always has self. Works with object attributes.
Static method → No self or cls. Just a helper function inside class.
"""








