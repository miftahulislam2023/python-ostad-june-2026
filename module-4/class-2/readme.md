# Class - 11

## Today's Topic
- Beginner problems (sum, even/odd, max of 3)

## Relevant Notes with code examples in English

### Practical Examples

#### 1. Check Even or Odd
```python
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
```

#### 2. Find Maximum of Three Numbers
```python
a, b, c = map(int, input("Enter three space-separated numbers: ").split())

if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

print(f"The largest number is: {largest}")
```
