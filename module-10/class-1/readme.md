# Class - 24

## Today's Topic
- Functions, parameters, return values

## Notes

### Introduction to Functions
Functions are **reusable** **blocks of code** that **perform a specific task**. They are defined using the `def` keyword.

```python
def greet(name): # name is a parameter
    return f"Hello, {name}!" # Return value

message = greet("Md. Abedur Rahman") # "Md. Abedur Rahman" is an argument
print(message)
```

### Argument Types
- **Positional Arguments:** Matched by position.
- **Keyword Arguments:** Specified by name.
- **Default Parameters:** Default values if none are passed.

```python
def power(base, exponent=2): # exponent has default value of 2
    return base ** exponent

print(power(4))    # 16 (uses default)
print(power(2, 3)) # 8 (overrides default)
```

## HW
1. Create a function that multiplies two numbers and print their values
2. Create a function that multiplies two numbers and return their values
3. Create a function that multiplies two numbers and can print or return (by using a parameter) their values
4. Create a function that calculates factorial of a number
5. Creat a function that calculates fibonacci number of term n