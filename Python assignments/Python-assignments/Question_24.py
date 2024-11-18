#Write a Python program to check a number is prime or not
n = int(input("Enter the number:"))

for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            print("Not prime")
            break
else:
        print("Prime number.")
        
"""output:
Enter the number:67
Prime number."""