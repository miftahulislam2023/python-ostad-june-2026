class Dog:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def bark(self):
        print(f'{self.name} says Woof Woof!')

    def sit(self):
        print(f'{self.name} is sitting')

    def sleep(self):
        print(f'{self.name} is sleeping')


dog1 = Dog("Tommy", 2, "Brown")
dog2 = Dog("Buddy", 3, "Black")

dog1.bark()
dog2.sit()

print(f'Name: {dog1.name}')
print(f'Age: {dog1.age}')
print(f'Color: {dog1.color}')

print(f'Name: {dog2.name}')
print(f'Age: {dog2.age}')
print(f'Color: {dog2.color}')