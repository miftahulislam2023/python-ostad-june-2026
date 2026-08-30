import json
filename = "notes.txt"
with open(f"/Users/miftahulislam/Programming/python/python-ostad-june-2026/module-11/class-3/file-note-app/{filename}", "r") as f:
    # print(type(f.read()))
    file_content = f.read()
    print(json.load(file_content))
