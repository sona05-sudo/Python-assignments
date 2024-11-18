# Write a program in Python to find largest among three numbers.

num1 = int(input("Enter the 1st number: "))
num2 = int(input("Enter the 2nd number: "))
num3 = int(input("Enter the 3rd number: "))

if num1 > num2 and num1 > num3:
    print("num1 is greatest")
elif num2 > num1 and num2 > num3:
    print("num2 is greatest")
else:
    print("num3 is greatest")

    """output:
    Enter the 1st number: 30
    Enter the 2nd number: 56
    Enter the 3rd number: 21
    num2 is greatest
    """