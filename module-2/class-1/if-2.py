# Age Grouping
# 16+ > Adult
#  < 16- Teenager
# 30+ > Youth
# 60+ > Senior Citizen

age = int(input("Enter your age: "))

if age <= 16 and age > 0:
    print("Teenager")
elif age > 16 and age <= 30:
    print("Adult")
elif age > 30 and age <= 60:
    print("Youth")
else:
    print("Senior Citizen")