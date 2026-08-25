import csv
with open("/Users/miftahulislam/Programming/python/python-ostad-june-2026/module-11/class-1/contacts.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        # print(type(row))
        print(row[0], row[1], row[2])