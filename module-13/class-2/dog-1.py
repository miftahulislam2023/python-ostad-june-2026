class Dog:
    name = ""
    age = ""
    color = ""
    gender = ""
    
    def bark(self):
        print("Woof Woof!")

    def sit(self):
        print("Dog is sitting")

    def sleep(self):
        print("Dog is sleeping")


dog1 = Dog()
dog1.name = "Tommy"
dog1.age = 2
dog1.color = "Brown"
dog1.gender = "Male"
dog1.bark()
dog1.sit()
dog1.sleep()

print(f'Name: {dog1.name}')
print(f'Age: {dog1.age}')
print(f'Color: {dog1.color}')
print(f'Gender: {dog1.gender}')
