filename = "notes.txt"
with open(f"/Users/miftahulislam/Programming/python/python-ostad-june-2026/module-11/class-3/file-note-app/{filename}", "r") as f:
    file_content = f.read()
    print(type(file_content))
    print(file_content)

    evaluated_list = eval(file_content)
    print(evaluated_list)
    print(type(evaluated_list))
