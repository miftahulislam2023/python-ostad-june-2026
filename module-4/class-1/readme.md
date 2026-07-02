# Class - 10

## Today's Topic
- Problem-solving techniques
    - Flow chart
- input/output patterns

## Notes

## Problem Solving Strategy
1. **Understand the Goal:** Write down inputs, expected outputs, and constraints.
2. **Plan with Pseudocode:** Outline the logical steps in plain English before writing code.
3. **Handle Edge Cases:** Think about empty inputs, zero, negatives, and large numbers.

## Common Input/Output Patterns
1. Reading multiple space-separated integers
2. Input string
3. Input bool
4. Input float
5. Output integers
6. Output float
7. Output string
8. Output bool

## Number input -> mean, median, mode
```bash
>>> type(12 + 12.5)
<class 'float'>
>>> type(12 + "12.5")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> "12" + "12.5"
'1212.5'
>>> clear
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'clear' is not defined
>>> "12" * 4
'12121212'
>>> "34" * "2"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can't multiply sequence by non-int of type 'str'
>>> False * 2
0
```