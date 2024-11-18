#Take input from user if it is greater than 15 print two times of difference if it’s less than 15 print four times of difference.
num = int(input("Enter the number: "))

condition1 = 2 * (num - 15)
condition2 = 4 * (15 - num)

if(num > 15):
    print("Condition 1:", condition1)
else:
    print("Condition 2: ", condition2)

    """output:
    Enter the number: 3
    Condition 2: 48
    """
