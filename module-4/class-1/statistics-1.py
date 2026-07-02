# Input n numbers and show their mean/mathematical average and mode
"""
3 6 12 67 34 3 6 20 -9 -23 90 3 2 1 1
total number -> n
summation -> sum
mean/mathematical average = sum / n
"""
n = int(input("How many numbers do you want to input? "))
input_string = input('Enter the numbers separated by an space:\n')
number_list = input_string.split(" ")

# print(n)
# print(input_string)
# print(number_list)

for number in number_list:
    print(number)

# 12 45 43 90 23