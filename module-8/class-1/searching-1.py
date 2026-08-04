events = [
    "Rajakar",
    "Abu Sayeed killing",
    "Mir Mugdho killing",
    "Massacre",
    "Attack"
]

is_found = False

for event in events:
    if event == "Mir Mugdho killing":
        is_found = True
        break


if is_found:
    print("Event found")
else:
    print("Event not found")