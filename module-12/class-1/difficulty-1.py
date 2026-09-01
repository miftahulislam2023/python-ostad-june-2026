list = [{'id': 1, 'note': 'Your notes goes here..'}, {'id': 2, 'note': 'Pythonnnnn'}]

string = str(list)
# print(string)
# print(type(string))

evaluated_list = eval(string)
# print(type(evaluated_list))

for item in evaluated_list:
    # print(item)
    # print(type(item))
    print(item['note'])