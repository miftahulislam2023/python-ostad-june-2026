import random

first_names = ["Abir", "Adnan", "Ahsan", "Alim", "Anik", "Anis", "Arif", "Arman", "Asif", "Atif", "Fahim", "Farhan", "Habib", "Hasan", "Imtiaz", "Iqbal", "Jamil", "Khalid", "Mahbub", "Mahmud", "Masud", "Mizan", "Nabil", "Nafis", "Naim", "Nasir", "Rashed", "Riaz", "Rubel", "Sajjad", "Sakib", "Salam", "Salman", "Shahin", "Sohel", "Tamim", "Tanvir", "Tariq", "Touhid", "Yasir", "Zahid", "Zaman", "Kamal", "Jamal", "Rafiq", "Shafiq", "Tareq", "Javed", "Saif", "Nayan"]
last_names = ["Ahmed", "Ali", "Amin", "Chowdhury", "Hasan", "Islam", "Khan", "Miah", "Mollah", "Rahman", "Sarker", "Sheikh", "Talukder", "Uddin"]
cities = ["Dhaka", "Chittagong", "Rajshahi", "Sylhet", "Khulna", "Barisal", "Rangpur", "Mymensingh", "Comilla", "Cox\''s Bazar", "Gazipur", "Narayanganj", "Jessore", "Bogra", "Feni"]

generated = []
used_names = set()

while len(generated) < 50:
    name = f"{random.choice(first_names)} {random.choice(last_names)}"
    if name not in used_names:
        used_names.add(name)
        phone = f"01{random.choice([3, 4, 5, 6, 7, 8, 9])}{random.randint(10000000, 99999999)}"
        city = random.choice(cities)
        generated.append(f"{name},{phone},{city}")

with open("/Users/miftahulislam/Programming/python/python-ostad-june-2026/module-11/class-1/contacts.csv", "a") as f:
    for line in generated:
        f.write("\n" + line)