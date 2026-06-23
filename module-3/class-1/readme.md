# Class - 7

## Today's Topic
- while loop, infinite loops, counters

## Notes

### Introduction to While Loops
A `while` loop repeatedly executes a block of code as long as a specified condition is `True`.

```python
count = 1
while count <= 5:
    print(f"Counter is: {count}")
    count += 1 # Incrementation to avoid infinite loop
```

### Infinite Loops
An infinite loop runs forever because the loop condition never evaluates to `False`. You can interrupt an infinite loop with `Ctrl + C`.

```python
# To avoid this, make sure the condition is updated inside the loop.
# while True:
#     print("This will run forever!")
```

### Controlling Loops: break and continue
- `break`: Terminates the loop statement and transfers execution to the statement immediately following the loop.
- `continue`: Skips the rest of the current iteration and jumps back to the condition check.

```python
n = 0
while n < 10:
    n += 1
    if n == 5:
        continue # Skip printing 5
    if n == 8:
        break    # Terminate loop at 8
    print(n)
```
