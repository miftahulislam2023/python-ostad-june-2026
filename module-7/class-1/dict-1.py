"""
key - reference / pointer / label / name of data
value - data
"""

person1 = {
    "name": "Samiul Islam",
    "age": 30,
    "gender": "Male",
    "monthly_income": 40.5,
    'age': 50
}

person2 = {
    "name": "Mahbubur Rahman",
    "age": 32,
    "gender": "Male",
    "monthly_income": 65
}

person3 = {
    "name": "Zannatul Maowa",
    "age": 29,
    "gender": "Female",
    "monthly_income": 75
}

print(person1["name"])
print(person2['age'])
print(person3['gender'])

print(person1['age'])
person1['age'] = 57
print(person1['age'])

del person3['name']
print(person3)

person3.pop('age')
print(person3)