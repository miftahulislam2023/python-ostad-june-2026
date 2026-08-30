import json

# Define all functions and variables needed
notes = [
    {
        "id": 1,
        "note": "Your notes goes here.."
    }
]

filename = "notes.txt"
choice = None

# load notes from a file
def load_notes(filename):
    with open(f"/Users/miftahulislam/Programming/python/python-ostad-june-2026/module-11/class-3/file-note-app/{filename}", "r") as f:
        pass

# write notes to a file
def save_notes(filename):
    pass

# add note to the end of the notes list
def add_note(note):
    temporary_note = {
        "id": len(notes) + 1,
        "note": note
    }
    notes.append(temporary_note)

# view note of the note_id
def view_note(note_id):
    for note in notes:
        if note["id"] == note_id:
            print(note["note"])

# update note of the note_id with updated_note
def update_note(note_id, updated_note):
    for note in notes:
        if note["id"] == note_id:
            note["note"] = updated_note

# delete note of the note_id
def delete_note(note_id):
    for note in notes:
        if note["id"] == note_id:
            ## think
            notes.remove(note)

# show menu to the user
def show_menu():
    print("Enter your choice: ")
    print("1. Add Note")
    print("2. View Note")
    print("3. Update Note")
    print("4. Delete Note")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    return choice

while choice != 5:
    choice = show_menu()
    if choice == 1:
        note = input("Enter your note:\n")
        add_note(note)
    elif choice == 2:
        note_id = int(input("Enter note_id: "))
        view_note(note_id)
    elif choice == 3:
        note_id = int(input("Enter note_id: "))
        updated_note = input("Enter your note:\n")
        update_note(note_id, updated_note)
    elif choice == 4:
        note_id = int(input("Enter note_id: "))
        delete_note(note_id)
    elif choice == 5:
        print("Exiting")
        break
    else:
        print("Invalid choice")

for i, note in enumerate(notes):
    print(f'{i+1}. {note["note"]}')