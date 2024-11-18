# Write a program in Python to compute simple Interest.

p = int(input("Enter the principal amount:"))
r = float(input("Enter the rate of interest:"))
t = int(input("Enter the no of years:"))
si = (p * r * t)/100
print("The simple interest comes out to be: ₹",si)
amount = p + si
print("The total amount to be returned is: ₹",amount)

""" output: The simple interest comes out to be: ₹ 5500
        The total amount to be returned is: ₹ 55500"""
