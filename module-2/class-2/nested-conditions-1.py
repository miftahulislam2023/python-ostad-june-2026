# Grade Calculator -> single line comment
"""
Multiple Line Comment
"""

'''
A+ -> 80 to 100
A  -> 70 to < 80
A- -> 60 to < 70
B  -> 50 to < 60
C  -> 40 to < 50
D  -> 33 to < 40
F  -> 00 to < 33
'''

mark = int(input("Enter your mark: "))
if mark < 0 or mark > 100:
    print("Invalid mark")
else:
    if mark >= 80 and mark <= 100:
        print("Your grade is: A+")

    elif mark >= 70 and mark < 80:
        print("Your grade is: A")

    elif mark >= 60 and mark < 70:
        print("Your grade is: A-")

    elif mark >= 50 and mark < 60:
        print("Your grade is: B")

    elif mark >= 40 and mark < 50:
        print("Your grade is: C")

    elif mark >= 33 and mark < 40:
        print("Your grade is: D")

    else:
        print("Your grade is: F")

