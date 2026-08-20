def max_of_two_numbers (x, y):
    if x > y:
        return x
    elif y > x:
        return y
    else:
        return x

lambda_max_of_two_numbers = lambda x, y: x if x > y else y

print(max_of_two_numbers(132, 64))
print(max_of_two_numbers(23, 64))
print(max_of_two_numbers(23, 23))

print(lambda_max_of_two_numbers(12, 12))