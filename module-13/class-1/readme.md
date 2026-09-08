# Class - 33

## Today's Topic
- Introduction to OOP

## A PIE
1. Abstraction -> বিমূর্ততা
2. Polymorphism -> বহুরূপিতা
3. Inheritance -> উত্তরাধিকার
4. Encapsulation -> তথ্য লুকানো/আবদ্ধতা

## Programming Paradigms
1. Functional Programming -> React
2. Structural Programming -> C, Go
3. Object Oriented Programming -> **Java**, **C++**, C#, Kotlin, **Dart**, Swift, PHP, Python, Ruby

### Object Oriented Programming (OOP)
OOP is a programming paradigm based on the concept of "objects" which primarily consists of attributes (or properties).

### Basic Concepts

#### 1. **Class**
A blueprint for creating objects.
```python
class Dog:
    species = "Canis familiaris"
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        return f"{self.name} says Woof!"
```

#### 2. **Object**
An instance of a class.
```python
# Creating objects (instances)
dog1 = Dog("Buddy", 3)
dog2 = Dog("Lucy", 2)
```

#### 3. **Attributes**
Variables that store data within a class.
```python
print(dog1.name)  # Output: Buddy
print(dog2.age)   # Output: 2
```

#### 4. **Methods**
Functions defined inside a class that perform operations.
```python
print(dog1.bark())  # Output: Buddy says Woof!
```

### Why Use OOP?
1. **Modularity**: Code is organized into objects, making it easier to manage.
2. **Reusability**: Classes can be reused in different parts of the program or in other programs.
3. **Maintainability**: Easier to debug and modify code.
4. **Scalability**: Better for building large and complex applications.