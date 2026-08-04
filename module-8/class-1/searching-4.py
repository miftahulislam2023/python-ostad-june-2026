events = [
    "Rajakar",
    "Abu Sayeed killing",
    "Mir Mugdho killing",
    "Massacre",
    "Attack"
]

found_events = []
is_found = False

search_term = input("Enter what you want to search: ")

for event in events:
    if event.lower().find(search_term.lower()) >= 0:
        is_found = True
        found_events.append(event)

if is_found:
    print(f"Found events for the term '{search_term}' are listed below: ")
    i = 1
    for event in found_events:
        print(f"{i}. {event}")
        i += 1
else:
    print(f"Event not found for the term '{search_term}'")