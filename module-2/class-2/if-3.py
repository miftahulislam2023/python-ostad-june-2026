age = int(input("Enter your age: "))

if age <= 0 or age >= 200:
    print("Invalid age")
elif age <= 16 and age > 0:
    print("Teenager")
elif age > 16 and age <= 30:
    print("Adult")
elif age > 30 and age <= 60:
    print("Youth")
else:
    print("Senior Citizen")