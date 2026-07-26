person2 = {
    "name": "Mahbubur Rahman",
    "age": 32,
    "gender": "Male",
    "monthly_income": 65
}

for value in person2.values():
    print(value)

print('\n')

for key in person2.keys():
    print(key)

print('\n')

for key, val in person2.items():
    print(f'{key}: {val}')