# Class - 35

## Today's Topic
- Polymorphism

## Notes

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
