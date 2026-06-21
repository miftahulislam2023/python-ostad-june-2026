# Class - 18

## Today's Topic
- Sets – Unique values, operations, use cases

## Relevant Notes with code examples in English

### Python Sets
Sets are unordered, unindexed, and contain unique elements only.

```python
# Creating sets
numbers_set = {1, 2, 3, 3, 4}
print(numbers_set) # {1, 2, 3, 4} (Duplicates removed)
```

### Set Operations
- **Union (`|`):** Combines elements from both sets.
- **Intersection (`&`):** Elements present in both sets.
- **Difference (`-`):** Elements in set A but not in set B.
- **Symmetric Difference (`^`):** Elements in either set, but not both.

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b) # {1, 2, 3, 4, 5}
print(a & b) # {3}
print(a - b) # {1, 2}
```
