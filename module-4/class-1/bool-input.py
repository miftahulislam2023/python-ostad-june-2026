input = input('Are you married? ')

if input.lower() == "false" or input.lower() == "f":
    is_married = False
    print(is_married)
elif input.lower() == "true" or input.lower() == "t":
    is_married = True
    print(is_married)
else:
    print('Invalid input')