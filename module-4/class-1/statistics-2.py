n = int(input("How many numbers do you want to input? "))
input_string = input('Enter the numbers separated by an space:\n')
number_list = input_string.split(" ")
sum = 0
# 12 45 43 90 23 12 88
for number in number_list:
    sum += int(number)

print(sum)
print(f"The mean is {sum / n}")