string = "I love my father."
# all letters become items in set
# print(dict(string))
string = "{'name': 'Miftahul Islam', 'age': 26, 'isStudent': True, 'courses': ['Python', 'Data Science', 'Machine Learning']}"
# print(dict(string))
print(eval(string)["courses"][1])
print(type(string))
data = (('a', 1), ('b', 2), ('c', 3))
print(type(dict(data)))
data = [('a', 1), ('b', True), ('c', 3)]
print(dict(data))