# Class - 27

## Today's Topic
- File handling (open, read, write, .csv)

## Relevant Notes with code examples in English

### File Handling in Python
Always use the `with` statement when opening files to ensure they are automatically closed.

#### Writing and Reading Text Files
```python
# Writing to file
with open("note.txt", "w") as file:
    file.write("Hello, files in Python!")

# Reading from file
with open("note.txt", "r") as file:
    content = file.read()
    print(content)
```

#### Parsing CSV files
```python
import csv

# Writing to CSV
with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age"])
    writer.writerow(["Abedur", "24"])

# Reading CSV
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```
