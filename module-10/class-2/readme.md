# Class - 25

## Today's Topic
- Scope, lambda, map() and filter() (intro)

## Notes

### Scope
Scope determines the visibility/accessibility of variables:
- **Local Scope:** Variables created inside a function.
- **Global Scope:** Variables created in the main body of the script.

```python
x = 10 # Global

def func():
    x = 5 # Local
    print("Inside:", x)

func() # Inside: 5
print("Outside:", x) # Outside: 10
```

### Lambda Functions
Anonymous, single-line functions.
```python
square = lambda x: x * x
print(square(5)) # 25
```

### map() and filter()
- `map(func, iterable)`: Applies a function to all items in an input list.
- `filter(func, iterable)`: Filters items based on a boolean-returning function.

```python
nums = [1, 2, 3, 4]
squared = list(map(lambda x: x*x, nums)) # [1, 4, 9, 16]
evens = list(filter(lambda x: x % 2 == 0, nums)) # [2, 4]
```
