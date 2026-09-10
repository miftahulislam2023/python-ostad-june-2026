class Animal:
    has_life = True
    number_of_ears = 2
    number_of_legs = 4

animal1 = Animal()

print(f'has_life: {animal1.has_life}')
print(f'number_of_ears: {animal1.number_of_ears}')
print(f'number_of_legs: {animal1.number_of_legs}')

animal2 = Animal()
animal2.number_of_ears = 4
animal2.number_of_legs = 2

print(f'has_life: {animal2.has_life}')
print(f'number_of_ears: {animal2.number_of_ears}')
print(f'number_of_legs: {animal2.number_of_legs}')