# Take marks of a student of four different subject find average depending on average findGrade(if marks >=75 i.e,’A’ or >=60 but <=75 i.e,’B’ or >=40 but <=60 i.e,’C’ or <=40 i.e,’D’)

sub1 = float(input("Enter marks for physics: "))
sub2 = float(input("Enter marks for maths: "))
sub3 = float(input("Enter marks for biology: "))
sub4 = float(input("Enter marks for chemistry: "))
avg = (sub1 + sub2 + sub3 + sub4) / 4

if avg >= 75:
    print("Grade: A")
elif avg >= 60 and avg <= 75:
    print("Grade: B")
elif avg >= 40 and avg <= 60:
    print("Grade: C")
else:
    print("Grade: D")

"""output:
Enter marks for physics: 64
Enter marks for maths: 72
Enter marks for biology: 65
Enter marks for chemistry: 60
Grade: B
"""