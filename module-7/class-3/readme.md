# Class - 19

## Today's Topic
- Mini Project – Contact book or Inventory

## Notes

### Mini Project: Contact Book
A contact book utilizing Python Dictionaries to execute CRUD operations dynamically.

```python
contacts = {}

while True:
    print("\n--- Contact Book ---")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. View All")
    print("6. Exit")
    
    choice = input("Enter choice (1-6): ")
    if choice == '1':
        name = input("Enter contact name: ").strip()
        phone = input("Enter phone number: ").strip()
        contacts[name] = phone
        print(f"Contact for {name} added!")
    elif choice == '2':
        name = input("Enter name to search: ").strip()
        if name in contacts:
            print(f"{name}: {contacts[name]}")
        else:
            print("Contact not found.")
    elif choice == '3':
        name = input("Enter contact name to update: ").strip()
        if name in contacts:
            new_phone = input("Enter new phone: ")
            contacts[name] = new_phone
            print("Contact updated.")
        else:
            print("Contact not found.")
    elif choice == '4':
        name = input("Enter contact name to delete: ").strip()
        if name in contacts:
            contacts.pop(name)
            print("Contact deleted.")
        else:
            print("Contact not found.")
    elif choice == '5':
        for name, phone in contacts.items():
            print(f"- {name}: {phone}")
    elif choice == '6':
        break
```
