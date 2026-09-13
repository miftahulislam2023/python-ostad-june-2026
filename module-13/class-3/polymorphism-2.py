# Parent Class
class Animal:
    def speak(self):
        print("Animal is speaking")

# Child Class 1
class Dog(Animal):
    pass

# Child Class 2
class Cat(Animal):
    def speak(self):  # মেথড ওভাররাইডিং
        print("Cat is meowing")

# ব্যবহার
animals = [Dog(), Cat(), Animal()]

for animal in animals:
    animal.speak()
