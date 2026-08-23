marks = [89, 78, 81, 90, 95]

def count_total_marks(marks):
    sum = 0
    for n in marks:
        sum += n
    return sum

lambda_count_total_marks = lambda marks: count_total_marks(marks)

print(count_total_marks(marks))
print(lambda_count_total_marks(marks))