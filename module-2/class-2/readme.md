# Class - 5

## Today's Topic
- Nested conditions
- truthy/falsy values
- debugging

## Relevant Notes with code examples in English

### Nested Conditions
You can write conditional statements inside other conditional statements to handle complex decision making.

```python
age = 20
citizen = True

if age >= 18:
    if citizen:
        print("You are eligible to vote.")
    else:
        print("Must be a citizen to vote.")
else:
    print("Too young to vote.")
```

### Truthy and Falsy Values
In Python, objects evaluate to either `True` or `False` in conditional contexts.
- **Falsy Values:**
  - `None`
  - `False`
  - Zero numbers: `0`, `0.0`
  - Empty sequences/collections: `""`, `[]`, `()`, `{}`, `set()`
- **Truthy Values:**
  - Almost everything else (non-empty strings, non-zero numbers, etc.)

```python
items = [] # Empty list is Falsy

if not items:
    print("No items in the list.")
```


## Cheatsheet
- [VS Code Windows Cheatsheet](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-windows.pdf)
- [VS Code MacOS Cheatsheet](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-macos.pdf)