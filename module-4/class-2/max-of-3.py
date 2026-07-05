# Maxium of three numbers
"""
a, b, c

Step 1: Input three numbers
Step 2: Compare numbers
Step 3: Print the maximum number

a > b and a > c: print(a)
b > a and b > c: print(b)
c > a and c > b: print(c)
"""

a = int(input("Enter 1st number:"))
b = int(input("Enter 2nd number:"))
c = int(input("Enter 3rd number:"))

if a >= b and a >= c:
    print(f'Maximum number is {a}')
elif b >= a and b >= c:
    print(f'Maximum number is {b}')
else:
    print(f'Maximum number is {c}')