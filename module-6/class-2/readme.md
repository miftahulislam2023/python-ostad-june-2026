# Class - 15

## Today's Topic
- Tuples – immutable, unpacking, usage

## Notes

### Tuples
Tuples are ordered and immutable collections. Once created, they cannot be altered (no append, insert, or remove).

```python
# Creating tuples
coordinates = (10.0, 20.0)
single_tuple = (5,) # Notice the trailing comma for single-item tuple
```

### Tuple Unpacking
Unpacking extracts tuple elements into individual variables.

```python
point = (3, 4, 5)
x, y, z = point
print(f"x: {x}, y: {y}, z: {z}")
```

### Why use Tuples instead of Lists?
1. **Safety:** Protects data against accidental changes.
2. **Speed:** Tuples are slightly faster than lists in terms of memory overhead and processing.
3. **Dictionary Keys:** Tuples can be used as keys in a dictionary (lists cannot because they are mutable).
