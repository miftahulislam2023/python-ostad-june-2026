events = [
    "Rajakar",
    "Abu Sayeed killing",
    "Mir Mugdho killing",
    "Massacre",
    "Attack"
]

found_events = []

is_found = False

for event in events:
    if event.lower().find("mir".lower()) >= 0:
        is_found = True
        found_events.append(event)

if is_found:
    print("Event found")
else:
    print("Event not found")