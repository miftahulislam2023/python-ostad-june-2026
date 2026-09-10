class Animal:
    def __init__(self, name, age, color, gender):
        self.name = name
        self.age = age
        self.color = color
        self.gender = gender

    def speak(self):
        print(f'{self.name} says Animal Sound!')

class Dog(Animal):
    def __init__(self, name, age, color, gender):
        super().__init__(name, age, color, gender)

class Cat(Animal):
    def __init__(self, name, age, color, gender):
        super().__init__(name, age, color, gender)

dog1 = Dog("Tommy", 2, "Black", "Male")
cat1 = Cat("Pussy", 2, "White", "Female")

dog1.speak()
cat1.speak()

# dog
print(f'Name: {dog1.name}')
print(f'Age: {dog1.age}')
print(f'Color: {dog1.color}')
print(f'Gender: {dog1.gender}')

# cat
print(f'Name: {cat1.name}')
print(f'Age: {cat1.age}')
print(f'Color: {cat1.color}')
print(f'Gender: {cat1.gender}')
