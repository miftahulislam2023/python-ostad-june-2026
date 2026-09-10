# Class - 34

## Today's Topic
- Abstraction & Inheritance

## Notes

### Inheritance
Inheritance allows a new class (child/subclass) to inherit attributes and methods of an existing class (parent/superclass).

```python
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return "Animal Sound"

class Dog(Animal): # Dog inherits from Animal
    def speak(self): # Overriding method
        return "Bark!"

d = Dog("Rex")
print(d.name)  # Rex
print(d.speak()) # Bark!
```

## Homework
1. Create 5 classes and create 2 objects of each
2. Write a Python script and show inheritance with examples