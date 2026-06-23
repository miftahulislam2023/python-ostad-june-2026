# Class - 17

## Today's Topic
- Dictionaries – CRUD, .items(), nested dicts

## Notes

### Python Dictionaries
Dictionaries store data in key-value pairs. They are ordered (since 3.7), mutable, and do not allow duplicate keys.

```python
# Initializing Dictionary
student = {
    "name": "Abedur",
    "age": 22,
    "course": "Python"
}
```

### CRUD Operations
- **Create/Update:** `dict[key] = value`
- **Read:** `dict[key]` or `dict.get(key)`
- **Delete:** `del dict[key]` or `dict.pop(key)`

```python
# Read
print(student.get("name"))

# Update
student["age"] = 23

# Create
student["grade"] = "A+"
```

### Iteration
- `.keys()`: Iterate keys.
- `.values()`: Iterate values.
- `.items()`: Iterate both keys and values.

```python
for key, val in student.items():
    print(f"{key}: {val}")
```
