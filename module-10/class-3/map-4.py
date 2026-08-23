mark_lists = [
    [89, 78, 81, 90, 95],
    [67, 85, 90, 94, 87],
    [72, 88, 91, 79, 85],
    [95, 92, 89, 88, 96],
    [60, 75, 80, 85, 90],
    [82, 84, 88, 90, 92],
    [77, 81, 85, 89, 93],
    [91, 93, 95, 97, 99],
    [65, 70, 75, 80, 85],
    [88, 89, 90, 91, 92]
]

def count_total_marks(marks):
    sum = 0
    for n in marks:
        sum += n
    return sum

total_marks = list(
    map(
        lambda mark_list: count_total_marks(mark_list),
        mark_lists
    )
)

print(total_marks)