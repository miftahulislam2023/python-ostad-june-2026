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

### Abstraction
Hiding complex details and showing only essential features using abstract base classes (`abc` module).

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        return "Vroom! Car engine started."
```
