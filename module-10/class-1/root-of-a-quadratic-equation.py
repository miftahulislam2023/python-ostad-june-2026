# Equation 1: 2x^2 + 5x + 3 = 0
"""
x1 = (-b + sqrt(b^2 - 4ac)) / 2a
x2 = (-b - sqrt(b^2 - 4ac)) / 2a
"""

import math

# print(math.sqrt(9))
# print(math.sqrt(30))
a = 2
b = 5
c = 3

x1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
x2 = (-b - math.sqrt(b**2 - 4*a*c)) / (2*a)
print(x1, x2)

# Equation 2: x^2 - 5x + 6 = 0
a = 1
b = -5
c = 6

x1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
x2 = (-b - math.sqrt(b**2 - 4*a*c)) / (2*a)
print(x1, x2)