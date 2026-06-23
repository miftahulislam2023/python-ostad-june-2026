# Class - 29

## Today's Topic
- Mini Project – Expense Tracker or File Note App

## Notes

### Mini Project: File-Based Note App
A script that saves user notes directly to a text file persistently.

```python
def add_note():
    note = input("Enter your note: ")
    with open("notes.txt", "a") as file:
        file.write(note + "\n")
    print("Note saved!")

def view_notes():
    try:
        with open("notes.txt", "r") as file:
            print("\n--- Saved Notes ---")
            for idx, line in enumerate(file, 1):
                print(f"{idx}. {line.strip()}")
    except FileNotFoundError:
        print("No notes found yet.")

while True:
    print("\n1. Add Note\n2. View Notes\n3. Exit")
    choice = input("Enter choice: ")
    if choice == '1': add_note()
    elif choice == '2': view_notes()
    elif choice == '3': break
```
