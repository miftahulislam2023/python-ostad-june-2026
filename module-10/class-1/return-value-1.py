import math

def root_of_quadratic_equation(a, b, c):
    x1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
    x2 = (-b - math.sqrt(b**2 - 4*a*c)) / (2*a)
    return (x1, x2)

print(root_of_quadratic_equation(2, 5, 3))