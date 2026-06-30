x0 = 0
x1 = 1
print(x0)
print(x1)

i = 1
while i <= 11:
    x2 = x0 + x1
    print(x2)
    x0 = x1
    x1 = x2
    i += 1