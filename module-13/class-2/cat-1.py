# name, meow(), age, color, gender
class Cat:
    def __init__(self, name, age, color, gender):
        self.name = name
        self.age = age
        self.color = color
        self.gender = gender

    def meow(self):
        print(f'{self.name} says Meow!')


cat1 = Cat("Pussy", 2, "White", "Female")

print(f'Name: {cat1.name}')
print(f'Age: {cat1.age}')
print(f'Color: {cat1.color}')
print(f'Gender: {cat1.gender}')
cat1.meow()