import math
def root_of_quadratic_equation(a, b, c):
    return (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)

lambda_root_of_quadratic_equation = lambda a, b, c: (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)

print(root_of_quadratic_equation(2, 5, 3))

print(lambda_root_of_quadratic_equation(2, 5, 3))