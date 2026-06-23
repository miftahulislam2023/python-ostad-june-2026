# Class - 8

## Today's Topic
- for loop, range(), loop nesting

## Notes

### For Loops and Iteration
A `for` loop is used for iterating over a sequence (such as a list, tuple, dictionary, set, or string).

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

### The range() Function
The `range(start, stop, step)` function generates a sequence of numbers:
- `start` (optional): Starting integer (default is 0)
- `stop` (required): End integer (exclusive)
- `step` (optional): Increment value (default is 1)

```python
# Generates numbers from 2 to 9, stepping by 2
for i in range(2, 10, 2):
    print(i) # Outputs: 2, 4, 6, 8
```

### Nested Loops
A nested loop is a loop inside a loop.

```python
for i in range(1, 4):
    for j in range(1, 4):
        print(f"i={i}, j={j}")
```
