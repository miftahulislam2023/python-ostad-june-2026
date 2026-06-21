# Class - 30

## Today's Topic
- String problems, real-world logic

## Relevant Notes with code examples in English

### Basic String Operations
Strings are immutable sequences of characters.

#### Methods:
- `.split()`: Splits string into a list.
- `.join()`: Joins list elements into a string.
- `.replace()`: Replaces substring.
- String slicing: `string[::-1]` reverses a string.

```python
text = "python programming"
print(text.upper()) # PYTHON PROGRAMMING
print(text.replace("python", "Java")) # Java programming
```

#### Palindrome Check Example
```python
word = input("Enter a word: ").lower()
if word == word[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")
```
