# Class - 26

## Today's Topic
- Mini Project – Function-based calculator

## Notes

### Mini Project: Function-Based Calculator
Uses pure modular functions to handle core arithmetic operations.

```python
def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): 
    return "Error! Division by zero." if b == 0 else a / b

def calculator():
    print("1. Add\n2. Subtract\n3. Multiply\n4. Divide")
    choice = input("Select operation (1-4): ")
    x = float(input("First number: "))
    y = float(input("Second number: "))
    
    if choice == '1': print("Result:", add(x, y))
    elif choice == '2': print("Result:", subtract(x, y))
    elif choice == '3': print("Result:", multiply(x, y))
    elif choice == '4': print("Result:", divide(x, y))
    else: print("Invalid choice.")

if __name__ == "__main__":
    calculator()
```
