# --------------------------
# Access Modifiers
# --------------------------

"""
Access modifiers control the visibility of class variables & methods:

=> Public → Accessible everywhere.
=> Protected → Internal use, but can be accessed by child classes.
=> Private → Hidden from outside, can’t be directly accessed.
"""
# Rules:-
"""
Python doesn’t enforce strict privacy (it’s based on naming conventions).

Use:
Public → For normal attributes/methods.
Protected → For internal use (still accessible by subclasses).
Private → When you want to hide attributes (but can still access via name-mangling).
Private doesn’t mean truly private — just makes accidental access harder.
"""

#Access Modifiers in Python (By Naming Convention)
# (a) Public (Default)
"""
Accessible from anywhere (inside & outside class).
No underscore.
"""
class Car:
    def __init__(self, brand):
        self.brand = brand  # Public

c = Car("Tesla")
print(c.brand)  # ✅ Accessible

# (b) Protected (_single_underscore)
"""
Single underscore prefix _var.
Convention: “This is for internal use — don’t touch it from outside unless you know what you’re doing.”
Still accessible (Python does not enforce it), but it’s a soft warning.
"""
class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self._speed = speed  # Protected

c = Car("Tesla", 120)
print(c._speed)  # ⚠️ Possible but not recommended

# (c) Private (__double_underscore)
"""
Double underscore prefix __var.
Python does name mangling: changes __var to _ClassName__var.
Makes it hard to access accidentally from outside.
"""
class Car:
    def __init__(self, brand):
        self.__engine_number = "123ABC"  # Private

c = Car("Tesla")
# print(c.__engine_number)  # ❌ AttributeError
print(c._Car__engine_number)  # ✅ Hacky way (name-mangled)

class Parent:
    def __init__(self):
        self._protected = "I am protected"
        self.__private = "I am private"

class Child(Parent):
    def show(self):
        print(self._protected)   # ✅ Works
        # print(self.__private)  # ❌ Doesn't work

c = Child()
c.show()



