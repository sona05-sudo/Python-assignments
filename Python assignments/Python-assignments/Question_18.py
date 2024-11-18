# Write a program in Python to print sum of natural number
n = int(input("Enter n: "))
sum = 0
for i in range(1, n+1):
    sum += i

print("Total sum: ",sum) 

"""output:
Enter n: 7
Total sum: 28
"""