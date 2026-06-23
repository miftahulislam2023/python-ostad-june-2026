# Class - 21

## Today's Topic
- Nested loop logic, conditions with dictionaries

## Notes

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

### Filtering Dictionaries with Conditions
```python
grades = {
    "Alice": 85,
    "Bob": 42,
    "Charlie": 90,
    "Diana": 55
}

# Finding students who passed (marks >= 50)
passed_students = {name: score for name, score in grades.items() if score >= 50}
print(passed_students) # {'Alice': 85, 'Charlie': 90, 'Diana': 55}
```
