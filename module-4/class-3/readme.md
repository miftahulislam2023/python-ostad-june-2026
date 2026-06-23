# Class - 12

## Today's Topic
- Practice session – live problem walkthrough, assignments

## Notes

### Advanced Beginner Challenges

#### Problem 1: Leap Year Checker
A year is leap if it is divisible by 4, but not by 100, unless it is also divisible by 400.

```python
year = int(input("Enter year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a Leap Year")
else:
    print(f"{year} is not a Leap Year")
```

#### Problem 2: Fibonacci Sequence Generator
Generate first `N` terms of the Fibonacci sequence.

```python
n = int(input("How many terms? "))
a, b = 0, 1
count = 0

if n <= 0:
    print("Please enter a positive integer")
else:
    while count < n:
        print(a, end=" ")
        a, b = b, a + b
        count += 1
    print()
```
