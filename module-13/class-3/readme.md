# Class - 35

## Today's Topic
- Polymorphism

## Notes

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

### Encapsulation
Encapsulation wraps data and methods into a single unit (class) and restricts access using access modifiers.
- **Public:** Default behavior.
- **Private:** Prefixed with double underscores `__`.

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            
    def get_balance(self): # Getter method
        return self.__balance

account = BankAccount("Abed", 1000)
account.deposit(500)
print(account.get_balance()) # 1500
# print(account.__balance) # Raises AttributeError
```


### Polymorphism
Polymorphism means "many forms". It allows methods in different classes to have the same name but behave differently.

```python
class Cat:
    def sound(self):
        return "Meow"

class Duck:
    def sound(self):
        return "Quack"

def make_sound(animal_obj):
    print(animal_obj.sound()) # Dynamically calls sound() based on object type

make_sound(Cat())  # Meow
make_sound(Duck()) # Quack
```
