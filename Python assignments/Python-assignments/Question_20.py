#Write a program in Python to print Factors of a Number.
num = int(input("Enter a +ve integer: "))

for i in range(1, num + 1):
        if num % i == 0:
            print(i)

"""output:
Enter a +ve integer: 14
1
2
7
14"""