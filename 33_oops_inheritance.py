# --------------------------
# Inheritance
# --------------------------

"""
Inheritance = One class (child) reuses the properties & methods of another class (parent).
It helps avoid code duplication and extend behavior.

Think: A Car class is general. A Tesla class can inherit from Car and add extra features like auto_pilot().
"""
# Rules:-
"""
1. Child class inherits all public & protected members of parent.
2. Private attributes (__attr) are not inherited directly.
3. Overriding = redefining a parent method in the child.
4. super() lets you call parent methods/constructors.
5. MRO decides method lookup order in multiple inheritance.
"""

# 1. Basic Inheritance
class Car:  # Parent
    def __init__(self, brand):
        self.brand = brand

    def drive(self):
        print(f"{self.brand} is driving.")

class Tesla(Car):  # Child
    def auto_pilot(self):
        print(f"{self.brand} is driving in autopilot mode.")

# Usage
t = Tesla("Tesla Model S")
t.drive()        # Inherited method
t.auto_pilot()   # Child method

# 2. Overriding Methods

class Car:
    def drive(self):
        print("Driving...")

class Tesla(Car):
    def drive(self):  # Override
        print("Driving silently with electricity.")

car = Car()
tesla = Tesla()

car.drive()    # Driving...
tesla.drive()  # Driving silently with electricity.

# 3. Using super() (Call Parent Method)
class Car:
    def __init__(self, brand):
        self.brand = brand
    def drive(self):
        print(f"{self.brand} is driving.")

class Tesla(Car):
    def __init__(self, brand, battery):
        super().__init__(brand)   # Call parent's __init__
        self.battery = battery
    def drive(self):
        super().drive()           # Use parent drive()
        print("...and it's electric!")

t = Tesla("Tesla", "100kWh")
t.drive()

#4. Multiple Inheritance
class Engine:
    def start(self):
        print("Engine started.")

class Wheels:
    def rotate(self):
        print("Wheels rotating.")

class Car(Engine, Wheels):  # Inherits both
    pass

c = Car()
c.start()     # From Engine
c.rotate()    # From Wheels

#5. Checking Inheritance
print(issubclass(Tesla, Car))  # True
print(isinstance(t, Tesla))    # True
print(isinstance(t, Car))      # True

#6. Abstract Parent (Force Child to Implement)
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def drive(self):
        pass

class Car(Vehicle):
    def drive(self):
        print("Car is driving.")

# v = Vehicle()  # ERROR: Can't create abstract class
c = Car()
c.drive()

#7 Real-World Example: Student System
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def details(self):
        return f"{self.name} scored {self.marks}"

class GraduateStudent(Student):
    def __init__(self, name, marks, thesis):
        super().__init__(name, marks)
        self.thesis = thesis
    def details(self):
        return super().details() + f" (Thesis: {self.thesis})"

s1 = GraduateStudent("Alice", 85, "AI Research")
print(s1.details())


