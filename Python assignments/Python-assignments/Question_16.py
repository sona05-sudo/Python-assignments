# Write a program in Python to find the roots of Quadratic equation.
import cmath  # Importing cmath to handle complex numbers

# Function to find the roots of a quadratic equation
def find_roots(a, b, c):
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c
    
    # Calculate the two roots using the quadratic formula
    root1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
    root2 = (-b - cmath.sqrt(discriminant)) / (2 * a)
    
    return root1, root2

# Input: Coefficients of the quadratic equation
a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))

# Ensure that 'a' is not zero
if a == 0:
    print("Coefficient 'a' cannot be zero for a quadratic equation.")
else:
    # Find the roots
    root1, root2 = find_roots(a, b, c)
    
    # Output: Display the roots
    print(f"The roots of the quadratic equation are: {root1} and {root2}")
