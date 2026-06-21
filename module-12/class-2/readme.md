# Class - 31

## Today's Topic
- Sorting logic, basic algorithm thinking

## Relevant Notes with code examples in English

### Sorting in Python
- `.sort()`: Sorts list in-place.
- `sorted()`: Returns a new sorted list.

```python
nums = [4, 2, 8, 1]
print(sorted(nums)) # [1, 2, 4, 8]
```

### Implementing Bubble Sort
```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

print(bubble_sort([64, 34, 25, 12, 22])) # [12, 22, 25, 34, 64]
```
