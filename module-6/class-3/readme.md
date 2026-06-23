# Class - 16

## Today's Topic
- Mini Project – Score Tracker

## Notes

### Mini Project: Score Tracker
This program allows dynamic tracking of student scores. It allows adding scores, calculating stats (min, max, average), and filtering passing marks.

```python
scores = []

while True:
    print("\n--- Score Tracker ---")
    print("1. Add Score")
    print("2. Display Stats")
    print("3. Exit")
    
    choice = input("Enter choice (1-3): ")
    if choice == '1':
        score_val = float(input("Enter exam score: "))
        scores.append(score_val)
        print("Score added successfully!")
    elif choice == '2':
        if not scores:
            print("No scores recorded yet.")
        else:
            avg_score = sum(scores) / len(scores)
            print(f"Total Scores: {len(scores)}")
            print(f"Highest Score: {max(scores)}")
            print(f"Lowest Score: {min(scores)}")
            print(f"Average Score: {avg_score:.2f}")
    elif choice == '3':
        print("Exiting Tracker. Goodbye!")
        break
    else:
        print("Invalid Choice!")
```
