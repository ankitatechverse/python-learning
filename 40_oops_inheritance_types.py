# --------------------------
# Inheritance
# --------------------------

"""
Single: One parent → One child
Multiple: One child → Many parents
Hierarchical: One parent → Many children
Hybrid: Mix (e.g., Diamond problem)
"""

# 1. Single Inheritance
# One parent → One child.
class Animal:
    def sound(self):
        print("Some generic animal sound.")

class Dog(Animal):  # Inherits from Animal
    def sound(self):
        print("Dog barks.")

dog = Dog()
dog.sound()   # Dog barks.

# 2. Multiple Inheritance
# One child → Inherits from multiple parents.
class Walk:
    def walk(self):
        print("Can walk.")

class Swim:
    def swim(self):
        print("Can swim.")

class Duck(Walk, Swim):  # Inherits from both Walk & Swim
    pass

duck = Duck()
duck.walk()   # Can walk.
duck.swim()   # Can swim.

# 3. Hierarchical Inheritance
# One parent → Multiple children.
class Animal:
    def sound(self):
        print("Some generic sound.")

class Dog(Animal):
    def sound(self):
        print("Dog barks.")

class Cat(Animal):
    def sound(self):
        print("Cat meows.")

dog = Dog()
cat = Cat()
dog.sound()  # Dog barks.
cat.sound()  # Cat meows.

# 4. Hybrid Inheritance
# Combination of multiple types (often looks like a diamond).
class LivingBeing:
    def breathe(self):
        print("Breathing...")

class Animal(LivingBeing):
    def sound(self):
        print("Some generic sound.")

class Bird(LivingBeing):
    def fly(self):
        print("Can fly.")

class Bat(Animal, Bird):  # Hybrid: Multiple + Hierarchical
    def sound(self):
        print("Bat screeches.")

bat = Bat()
bat.breathe()  # From LivingBeing
bat.fly()      # From Bird
bat.sound()    # Overridden in Bat

