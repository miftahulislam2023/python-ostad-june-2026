import csv
with open("/Users/miftahulislam/Programming/python/python-ostad-june-2026/module-11/class-1/students.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Miftahul Islam", "23", "Rajshahi"])
    writer.writerow(["Samiul Islam", "22", "Dhaka"])
    writer.writerow(["Mizanur Rahman", "24", "Chittagong"])
    writer.writerow(["Milon Rahman", "25", "Sylhet"])
    writer.writerow(["Milon Rahman", "25", "Sylhet"])