# Class - 25

## Today's Topic
- Scope
- lambda

## Notes
- [Greek Alphabet](https://web.mit.edu/jmorzins/www/greek-alphabet.html)

### Scope
Scope determines the visibility/accessibility of variables:
- **Local Scope:** Variables created inside a function.
- **Global Scope:** Variables created in the main body of the script.

```python
x = 10 # Global

def func():
    x = 5 # Local
    print("Inside:", x)

func() # Inside: 5
print("Outside:", x) # Outside: 10
```

## Lambda
1. Lambda is a function
2. It is not a complete function as it lacks some functionalities
3. There are some special cases where it is used

### Lambda Functions
Anonymous, single-line functions.
```python
square = lambda x: x * x
print(square(5)) # 25
```