# Write a program in Python to swap two numbers without using third variable
num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))

num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2

print(f"After swapping the numbers are: num1 = {num1}, num2 = {num2}")

"""output: 
Enter the first number:55
Enter the second number:89
After swapping the numbers are: num1 = 89, num2 = 55 """