# Write a program in Python to check a given year is leap year or not.
year = int(input("Enter the year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Given year is a leap year.")
else:
    print("Given year is not a leap year.")

    """
    output:
    Enter the year: 2049
    Given year is not a leap year.
    """
