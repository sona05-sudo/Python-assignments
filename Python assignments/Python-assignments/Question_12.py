# Write a program in Python to check a triangle is equilateral,scalene or isosclees.

s1 = float(input("Enter side1: "))
s2 = float(input("Enter side2: "))
s3 = float(input("Enter side3: "))

if s1 == s2 == s3:
    print("The given triangle is equilateral.")
elif s1 == s2 or s1 == s3 or s2 ==s3:
    print("The given triangle is isosceles.")
else:
    print("The given triangle is scalene.")    

"""
output:
Enter side1: 6.8
Enter side2: 2.4
Enter side3: 7
The given triangle is scalene.
"""