# Class - 3

## Today's Topic
- Practice session: First 10-line program\n- Debugging syntax errors\n- Hands-on input/output\n- Homework walkthrough

## Relevant Notes with code examples in English

### Debugging Syntax and Runtime Errors
- **SyntaxError:** Code violates the grammar rules of Python (e.g., missing closing parenthesis or quote).
- **TypeError:** Operation performed on incompatible types (e.g., adding string and integer directly).
- **ValueError:** Passing an argument with the right type but inappropriate value.

### Basic Expressions and Operators
Python supports standard arithmetic operations:
- Addition: `+`
- Subtraction: `-`
- Multiplication: `*`
- Division: `/` (returns float)
- Floor Division: `//` (discards decimal part)
- Modulus: `%` (returns remainder)
- Exponentiation: `**` (power of)

### Example: Interactive Calculator (First 10-Line Program)
```python
# A simple program to calculate percentage
total_marks = float(input("Enter total marks: "))
obtained_marks = float(input("Enter obtained marks: "))

# Calculate percentage
percentage = (obtained_marks / total_marks) * 100

print(f"Obtained: {obtained_marks}/{total_marks}")
print(f"Percentage: {percentage:.2f}%")
```
