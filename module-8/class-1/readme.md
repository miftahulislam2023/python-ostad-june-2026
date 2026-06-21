# Class - 20

## Today's Topic
- Searching in lists, frequency counters

## Relevant Notes with code examples in English

### Searching Algorithms
- **Linear Search:** Checks each element sequentially until a match is found. Time complexity is $O(N)$.
```python
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
```

### Frequency Counter Pattern
Use dictionaries to count frequencies of elements in list.
```python
items = ["apple", "banana", "apple", "cherry", "banana", "apple"]
frequency = {}

for item in items:
    frequency[item] = frequency.get(item, 0) + 1

print(frequency) # {'apple': 3, 'banana': 2, 'cherry': 1}
```
