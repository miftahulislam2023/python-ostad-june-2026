# Class - 33

## Today's Topic
- Encapsulation

## Relevant Notes with code examples in English

### Object Oriented Programming (OOP)
OOP is a paradigm based on "objects", which contain data (attributes) and code (methods).

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
