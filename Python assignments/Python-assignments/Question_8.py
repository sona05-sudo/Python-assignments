#Write a Python Program to find the gravitational force acting between two objects.
N = 6.67430e-11

m1 = float(input("Enter the mass of the first object (in kg): "))
m2 = float(input("Enter the mass of the second object (in kg): "))
d = float(input("Enter the distance between them (in meters): "))
G = N * (m1 * m2) / d ** 2
print(f"The gravitational pull between them is: {G:.2e} N")

"""output: 
Enter the mass of the first object (in kg): 46
Enter the mass of the second object (in kg): 34
Enter the distance between them (in meters): 15
The gravitational pull between them is: 4.64e-10 N
"""