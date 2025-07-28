# Create a calculator capable of performing addition, subtraction, multiplication and division operations
#  on two numbers. Your program should format the output in a readable manner!

x= 10
y=5

z= x + y
print(f"Addition of {x} and {y} is: {z}")
z= x - y
print(f"Subtraction of {x} and {y} is: {z}")
z= x * y
print(f"Multiplication of {x} and {y} is: {z}")
z= x / y
print(f"Division of {x} and {y} is: {z:.2f}")  # Format to 2 decimal places
z= x // y
print(f"Floor Division of {x} and {y} is: {z}")
z= x % y
print(f"Modulus of {x} and {y} is: {z}")
z= x ** y
print(f"Exponentiation of {x} and {y} is: {z}")
