# --------------------------
# Operator Overloading Example
# --------------------------


# 1. Example: Complex Number Addition
class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    # String representation
    def __str__(self):
        return f"{self.real} + {self.imag}i"

    # Addition
    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    # Subtraction
    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    # Multiplication
    def __mul__(self, other):
        real_part = self.real * other.real - self.imag * other.imag
        imag_part = self.real * other.imag + self.imag * other.real
        return Complex(real_part, imag_part)

    # Equality check
    def __eq__(self, other):
        return self.real == other.real and self.imag == other.imag

c1 = Complex(2, 3)
c2 = Complex(2, 3)

print("c1:", c1)              # 2 + 3i
print("c2:", c2)              # 1 + 4i

print("Addition:", c1 + c2)   # 3 + 7i
print("Subtraction:", c1 - c2) # 1 - 1i
print("Multiplication:", c1 * c2) # (2*1 - 3*4) + (2*4 + 3*1)i = -10 + 11i

print("Equality:", c1 == c2)  # False



