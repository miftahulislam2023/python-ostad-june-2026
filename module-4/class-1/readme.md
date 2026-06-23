# Class - 10

## Today's Topic
- Problem-solving techniques, input/output patterns

## Notes

### Problem Solving Strategy
1. **Understand the Goal:** Write down inputs, expected outputs, and constraints.
2. **Plan with Pseudocode:** Outline the logical steps in plain English before writing code.
3. **Handle Edge Cases:** Think about empty inputs, zero, negatives, and large numbers.

### Common Input/Output Patterns
Many coding platforms require taking single or multiple values in a single line.
- Reading multiple space-separated inputs:
```python
# Example: reading two space-separated integers
x, y = map(int, input("Enter two numbers: ").split())
print(f"Sum: {x + y}")
```
