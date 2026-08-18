def divide(a, b=12):
    if b != 0:
        print(a / b)
    else:
        print("Can't divide by zero")

divide(12, 4)
divide(4, 12)

divide(a=12, b=4)
divide(b=4, a=12)

divide(a=4, b=12)
divide(b=12, a=4)