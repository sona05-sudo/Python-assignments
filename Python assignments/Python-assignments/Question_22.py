#Write a Python program to find Factorial of a given number
n = int(input("Enter a number: "))
fact = 1
for i in range(2, n + 1):
        fact *= i
print("The factorial of the number is:", fact)  

"""Output:
Enter a number: 5
The factorial of the number is: 120"""