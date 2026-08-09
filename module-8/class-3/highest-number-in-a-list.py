numbers = [1200, 56, 123, 45, 23, 5600, 36, 74, 61, 234, 56, 234, 12, 89, 1020]

highest_number = numbers[0]

for n in numbers:
    if n > highest_number:
        highest_number = n

print(highest_number)