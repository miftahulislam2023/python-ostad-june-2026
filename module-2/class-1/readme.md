# Class - 4

## Today's Topic
- if, else, elif
- logical operators (and, or, not)

## Relevant Notes with code examples in English

### Comparison Operators
Comparison operators compare two values and return a boolean:
- `>` : Greater than
- `<` : Less than
- `==` : Equal to
- `>=` : Greater than or equal to
- `<=` : Less than or equal to
- `!=` : Not equal to

### Conditional Statements
Use `if`, `elif`, and `else` to control the flow of execution based on conditions.
```python
score = 85

if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
else:
    print("Grade F")
```

### Logical Operators
- `and`: Returns `True` if both conditions are True.
- `or`: Returns `True` if at least one condition is True.
- `not`: Reverses the boolean result.

```python
age = 20
has_license = True

if age >= 18 and has_license:
    print("You can drive.")
else:
    print("You cannot drive.")
```
