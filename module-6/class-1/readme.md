# Class - 14

## Today's Topic
- Lists – index, slice, methods (append, insert)

## Relevant Notes with code examples in English

### Python Lists
Lists are ordered, mutable, and allow duplicate elements.

```python
# Initializing lists
numbers = [10, 20, 30, 40, 50]
```

### Indexing and Slicing
- **Index:** Elements can be accessed using positive indices (starting at 0) or negative indices (starting at -1 from end).
- **Slicing:** Get a sublist using `list[start:stop:step]`.

```python
print(numbers[0])   # 10
print(numbers[-1])  # 50 (Last element)
print(numbers[1:4]) # [20, 30, 40]
```

### List Mutation Methods
- `.append(x)`: Adds item `x` to the end.
- `.insert(index, x)`: Inserts item `x` at given `index`.
- `.remove(x)`: Removes first occurrence of `x`.
- `.pop()`: Removes and returns the last element.

```python
numbers.append(60)
numbers.insert(1, 15) # Inserts 15 at index 1
print(numbers) # [10, 15, 20, 30, 40, 50, 60]
```
