nums = [1, 2, 3, 4]

# def is_even(x):
#     return x % 2 == 0

def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False

evens = list (
    filter (
        is_even,
        nums
    )
)

print(evens)