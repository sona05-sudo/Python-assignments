#Write a Python program to check a number is Armstrong or not.
num = int(input("Enter a number:"))
str_num = str(num)
num_dig = len(str_num)
sum = sum(int(digit) ** num_dig for digit in str_num)

if sum == num:
    print("No is an armstrong number.")
else:
    print("Not an armstrong number.")

"""output:
Enter a number:3453
Not an armstrong number"""