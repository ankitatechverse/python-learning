# --------------------------
# MRO - Method Resolution Order
# --------------------------

"""
MRO = Method Resolution Order.
It’s the order Python searches for a method when you call it on an object.
It matters when multiple classes in the inheritance chain define the same method.
Python uses the C3 linearization algorithm to determine the MRO.
"""

# Key Takeaway
"""
Single inheritance: super() feels like “call my parent”.
Multiple inheritance: super() = “call the next class in the MRO.”
"""


class A:
    def show(self): print("A")

class B(A):
    def show(self): 
      print("B") 
      super().show()

class C(A):
    def show(self): print("C")

class D(B, C):  # Multiple inheritance
    pass

d = D()
d.show()  
print(D.mro())




