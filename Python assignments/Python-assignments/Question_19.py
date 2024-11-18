# Write a program in Python to print Sum of Digit.
num = int(input("Enter an integer number: "))
total = 0

while num > 0:
        digit = num % 10  
        total += digit       
        num //= 10

print("sum of the digits: ", total)

"""output:
Enter an integer number: 638401
sum of the digits: 22
"""