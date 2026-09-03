numbers = [10, 2, 9, 4, 5, 1]
final_result = [10, 9, 5, 4, 2, 1]

# we need two loops
"""
Iteration-1:
Start: 10, 2, 9, 4, 5, 1
Step-1: 2, 10, 9, 4, 5, 1
Step-2: 2, 9, 10, 4, 5, 1
Step-3: 2, 9, 4, 10, 5, 1
Step-4: 2, 9, 4, 5, 10, 1
Step-5: 2, 9, 4, 5, 1, 10

Iteration-2:
Start: 2, 9, 4, 5, 1, 10
Step-1: 2, 9, 4, 5, 1, 10
Step-2: 2, 4, 9, 5, 1, 10
Step-3: 2, 4, 5, 9, 1, 10
Step-4: 2, 4, 5, 1, 9, 10

Iteration-3:
Start: 2, 4, 5, 1, 9, 10
Step-1: 2, 4, 5, 1, 9, 10
Step-2: 2, 4, 5, 1, 9, 10
Step-3: 2, 4, 1, 5, 9, 10

Iteration-4:
Start: 2, 4, 1, 5, 9, 10
Step-1: 2, 4, 1, 5, 9, 10
Step-2: 2, 1, 4, 5, 9, 10

Iteration-5:
Start: 2, 1, 4, 5, 9, 10
Step-1: 1, 2, 4, 5, 9, 10

Iteration-1:
Start: 10, 2, 9, 4, 5, 1
Step-1: 10, 2, 9, 4, 5, 1
Step-2: 10, 2, 9, 5, 4, 1
Step-3: 10, 2, 9, 5, 4, 1
Step-4: 10, 9, 2, 5, 4, 1
Step-5: 10, 9, 2, 5, 4, 1

Iteration-2:
Start: 10, 9, 2, 5, 4, 1
Step-1: 10, 9, 2, 5, 4, 1
Step-2: 10, 9, 2, 5, 4, 1
Step-3: 10, 9, 5, 2, 4, 1
Step-4: 10, 9, 5, 4, 2, 1

Ascending thinkng the other way:
Iteration-1:
Start: 10, 2, 9, 4, 5, 1
Step-1: 10, 2, 9, 4, 1, 5
Step-2: 10, 2, 9, 1, 4, 5
Step-3: 10, 2, 1, 9, 4, 5
Step-4: 10, 1, 2, 9, 4, 5
Step-5: 1, 10, 2, 9, 4, 5

Iteration-2:
Start: 1, 10, 2, 9, 4, 5
Step-1: 1, 10, 2, 9, 4, 5
Step-2: 1, 10, 2, 4, 9, 5
Step-3: 1, 10, 2, 4, 9, 5
Step-4: 1, 2, 10, 4, 9, 5
"""

"""
outer loop -> iteration
inner loop -> step i.e. comparing and swapping the numbers
"""
numbers = [100, -2, 9, 40, 5, 1, -232]
i = 0
while i < 6:
    j = 0
    while j < len(numbers) - (i + 1):
        if numbers[j] > numbers[j+1]:
            temp = numbers[j+1]
            numbers[j+1] = numbers[j]
            numbers[j] = temp
        j += 1
    i += 1
        
print(numbers)

"""
Swapping two numbers without using a 3rd variable
a = 2, b = 7
a = a + b # a = 9
b = a - b # b = 2
a = a - b # a = 7

a = 3, b = -5
a = a + b # a = -2
b = a - b # b = 3
a = a - b # a = -5
"""