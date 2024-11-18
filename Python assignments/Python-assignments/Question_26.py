#Write a Python program to print Fibonacci series of n term
n = int(input("Enter n terms:"))
fib = []
a, b = 0, 1
for i in range(n):
   fib.append(a)
   a, b = b, a + b
print(fib)

"""output;
Enter n terms:5
[0, 1, 1, 2, 3]"""