# file1 = open("module-1-class-1.md", "r")
# absolute path -> full path
# file1 = open("/Users/miftahulislam/Programming/python/python-ostad-june-2026/module-11/class-1/module-1-class-1.md", "r")

# relative path -> path relative to the current working directory
file1 = open("module-1-class-1.md", "r")

file_content = file1.read()
print(file_content)

file1.close()