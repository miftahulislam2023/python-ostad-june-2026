# Class - 6

## Today's Topic
- Mini Project – Grade evaluator or age checker

## Notes

### Mini Project: Grade Evaluator
This project takes a score as input, checks its validity, and calculates grades dynamically. It demonstrates nested conditions, truthy/falsy inputs, and type conversion.

```python
score_input = input("Enter your exam score (0-100): ")

if not score_input.strip(): # Truthy check for empty input
    print("Error: Input cannot be empty.")
else:
    score = float(score_input)
    if score < 0 or score > 100:
        print("Invalid score! Please enter a value between 0 and 100.")
    else:
        if score >= 90:
            grade = "A+"
        elif score >= 80:
            grade = "A"
        elif score >= 70:
            grade = "B"
        elif score >= 60:
            grade = "C"
        elif score >= 50:
            grade = "D"
        else:
            grade = "F"
        print(f"Your grade is: {grade}")
```
