# Class - 2

## Today's Topic
- print(), input()\n- Variables, Data Types (int, float, str, bool)\n- Type conversion, type(), id()\n- Writing basic expressions

## Relevant Notes with code examples in English

### Variables and Naming Rules
Variables are containers for storing data values. In Python, variables are dynamically typed.
Rules:
- Must start with a letter or underscore `_`.
- Cannot start with a number.
- Can only contain alphanumeric characters and underscores (`a-z`, `A-Z`, `0-9`, `_`).
- Case-sensitive (`age` and `Age` are different).

### Fundamental Data Types
- `int`: Integers (e.g., `10`, `-5`)
- `float`: Floating point/decimal numbers (e.g., `10.5`, `-0.99`)
- `str`: Strings/Text (e.g., `"Hello"`, `'Python'`)
- `bool`: Boolean values (`True` or `False`)

### Input and Output
- `print()`: Used to display output.
- `input()`: Used to take input from the user (always returns a string).

```python
# Taking input and printing
name = input("Enter your name: ")
age = int(input("Enter your age: ")) # Type conversion from str to int

print(f"Hello {name}, you are {age} years old.")
```

### Type Conversion and Utility Functions
- `type()`: Returns the data type of an object.
- `id()`: Returns the unique memory address identifier of an object.

```python
x = 10
y = "10"
print(type(x)) # <class 'int'>
print(id(x))   # Memory address representation

# Explicit Type Conversion (Casting)
converted_y = int(y)
print(type(converted_y)) # <class 'int'>
```
