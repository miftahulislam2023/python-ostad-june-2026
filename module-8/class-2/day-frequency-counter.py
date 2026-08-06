oct_2026 = [
    [0, 0, 0, 0, 1, 2, 3],
    [4, 5, 6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15, 16, 17],
    [18, 19, 20, 21, 22, 23, 24],
    [25, 26, 27, 28, 29, 30, 31]
]

day_frequency = {
    "Sunday": 0,
    "Monday": 0,
    "Tuesday": 0,
    "Wednesday": 0,
    "Thursday": 0,
    "Friday": 0,
    "Saturday": 0
}

for i in range(0, 5):
    for j in range(0, 7):
        if oct_2026[i][j] != 0:
            if j == 0:
                day_frequency["Sunday"] += 1
            elif j == 1:
                day_frequency["Monday"] += 1
            elif j == 2:
                day_frequency["Tuesday"] += 1
            elif j == 3:
                day_frequency["Wednesday"] += 1
            elif j == 4:
                day_frequency["Thursday"] += 1
            elif j == 5:
                day_frequency["Friday"] += 1
            elif j == 6:
                day_frequency["Saturday"] += 1
        
print(day_frequency)