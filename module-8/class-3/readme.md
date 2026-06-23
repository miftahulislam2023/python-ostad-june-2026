# Class - 22

## Today's Topic
- Mini Project – Voting system or student management

## Notes

### Mini Project: Student Management System
Manages students grades, showing records and calculating averages using nested dictionaries.

```python
students = {}

while True:
    print("\n--- Student Management System ---")
    print("1. Add Student & Grades")
    print("2. View Students")
    print("3. Exit")
    
    choice = input("Enter choice: ")
    if choice == '1':
        name = input("Enter student name: ")
        math = float(input("Math Grade: "))
        science = float(input("Science Grade: "))
        students[name] = {"Math": math, "Science": science}
    elif choice == '2':
        for name, subjects in students.items():
            avg = sum(subjects.values()) / len(subjects)
            print(f"Student: {name} | Math: {subjects['Math']} | Science: {subjects['Science']} | Avg: {avg:.2f}")
    elif choice == '3':
        break
```
