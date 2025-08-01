# --------------------------
# Super Methods in Inheritance
# --------------------------

# Rules
"""
1. Re-use parent class code (don’t duplicate).
2. Initialize parent class attributes in child class (__init__).
3. Support multiple inheritance (it respects Python’s MRO – Method Resolution Order).
"""

# 1. Basic Example – Calling Parent Method
class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greet(self):
        print("Hello from Child")
        super().greet()  # Call Parent's greet
        

c = Child()
c.greet()

# 2. Using super() in Constructors
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, marks):
        super().__init__(name)  # Call Parent __init__
        self.marks = marks

s = Student("Alice", 95)
print(s.name, s.marks)

#3. Use *args and **kwargs
class Parent:
    def __init__(self, name, age, city, country, phone, email):
        self.name = name
        self.age = age
        self.city = city
        self.country = country
        self.phone = phone
        self.email = email

class Child(Parent):
    def __init__(self, student_id, *args, **kwargs):
        super().__init__(*args, **kwargs)  # Pass all remaining args to Parent
        self.student_id = student_id

c = Child(101, "Alice", 25, "New York", "USA", "1234567890", "alice@example.com")
print(c.__dict__)
print(c.name, c.age, c.city, c.country, c.phone, c.email, c.student_id)


