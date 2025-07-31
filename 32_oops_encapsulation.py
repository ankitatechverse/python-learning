# --------------------------
# Encapsulation
# --------------------------

"""
Encapsulation = Hiding data inside a class and controlling how it’s accessed or changed.Instead of letting anyone modify values directly, you wrap them with controlled methods (like a gatekeeper).
Think: You don’t put fuel straight into the engine — you use a fuel cap.The cap controls how fuel gets in (safely, properly).

Why Use It?
=> Protect data (stop invalid values).
=> Add logic when setting/getting (e.g., validation, logging).
=> Make your class safe and easy to use.

Rules:-
=> Use _variable or __variable for internal attributes.
=> Use getter/setter methods if you need validation or custom logic.
=> Prefer @property for Pythonic, clean code.
=> Never expose internal data directly if it must stay valid.
"""

#1. The Problem Without Encapsulation:-
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks  # anyone can set anything

s = Student("Alice", 95)
s.marks = 9999  # OOPS - invalid!
print(s.marks)  # 9999

#2. Encapsulation: Step 1 – Make it “Private”
class Student:
    def __init__(self, name, marks):
        self.name = name
        self._marks = marks  # single underscore = "protected"

s = Student("Alice", 95)
print(s._marks)  # You can still access, but by convention, you shouldn't

#3. Encapsulation: Step 2 – Getters & Setters
class Student:
    def __init__(self, name, marks):
        self.name = name
        self._marks = marks

    def get_marks(self):         # Getter
        return self._marks

    def set_marks(self, value):  # Setter
        if 0 <= value <= 100:    # validation
            self._marks = value
        else:
            print("Invalid marks!")

s = Student("Alice", 95)
print(s.get_marks())   # 95
s.set_marks(105)       # Invalid marks!
print(s.get_marks())   # Still 95

#4. Pythonic Way: @property (Recommended)

class Student:
    def __init__(self, name, marks):
        self.name = name
        self._marks = marks

    @property
    def marks(self):  # Getter
        return self._marks

    @marks.setter
    def marks(self, value):  # Setter
        if 0 <= value <= 100:
            self._marks = value
        else:
            print("Invalid marks!")

s = Student("Alice", 95)
print(s.marks)    # 95   (no need for get_marks())
s.marks = 85      # sets via setter
print(s.marks)    # 85
s.marks = 150     # Invalid marks!

"""
All Cases Together:-
Case 1: Direct public attribute → Fast but unsafe.
Case 2: Getter/Setter methods → Safe but verbose.
Case 3: @property → Best of both: clean + safe.
"""

