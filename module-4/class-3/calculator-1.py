# Calculator (+, -, *, /)
#    - Input 2 numbers
#    - Input operator (+, -, *, /)
#    - Calculate
#    - Print result with proper message
#    - Handle division by zero

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
operator = input("Enter the operator: ")

if operator == "+":
    print(a + b)
elif operator == "-":
    print(a - b)
elif operator == "*":
    print(a * b)
elif operator == "/":
    if b != 0:
        print(a / b)
    else:
        print("Can't divide by zero!")
else:
    print("Invalid operator")