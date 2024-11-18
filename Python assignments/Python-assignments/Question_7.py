#Write a program in Python to convert a given number of days into days, month, year and week

num = int(input("Enter total no of days: "))

yrs = num // 365
days = num % 365
months = days // 30
days = days % 30
weeks = days // 7
days = days % 7

print("No of years: ",yrs)
print("No of months: ",months)
print("No of weeks: ",weeks)
print("No of days: ",days)

"""output:
Enter total no of days: 685
No of years:  1
No of months:  10
No of weeks:  2
No of days:  6"""