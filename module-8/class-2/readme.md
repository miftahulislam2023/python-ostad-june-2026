# Class - 21

## Today's Topic
- Nested loop logic
- conditions with dictionaries

### Nested Loops in Lists
Using nested loops to iterate over 2D structures (matrices).

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for val in row:
        print(val, end=" ")
    print()
```
