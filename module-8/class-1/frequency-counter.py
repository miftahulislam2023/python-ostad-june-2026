numbers = [0, 1, 2, 3, 1, 4, 5, 1, 3, 2, 6, 7, 8, 9, 2, 3, 4, 5, 5, 6]

frequencies = { }

for n in numbers:
    key_found = False

    for key in frequencies.keys():
        if int(key) == n:
            frequencies[f"{n}"] += 1
            key_found = True
            break
    
    if not key_found:
        frequencies[f"{n}"] = 1

print(frequencies)

