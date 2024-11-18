#Write a Python program to check a number is palindrome or not

num = int(input("Enter the number to check: "))
num_str = str(num)
rev_num_str = num_str[::-1]
if num_str == rev_num_str:
    print("The no is a palindrome.")
else:
    print("The no is not palindrome.")

"""output:
Enter the number to check: 9009.
The no is a palindrome."""