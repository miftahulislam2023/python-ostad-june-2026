# Piecewise function
"""
100 Unit

75 x 5.26 = 394.50
25 x 7.20 = 180.00
Demand charge 42 x 2 = 84
VAT -> 33.00
Total -> 692.00
"""

"""
Unit -> charge
VAT -> 5%

"""

unit = int(input("Enter your total electricity units: "))
total_charge = 0

if unit <= 50 and unit >= 0:
    total_charge = unit * 4.63
elif unit >= 0 and unit <= 75:
    total_charge = unit * 5.26
elif unit >= 76 and unit <= 200:
    unit1 = 75
    unit2 = unit - unit1
    total_charge = unit1 * 5.26 + unit2 * 7.20
elif unit >= 201 and unit <= 300:
    unit1 = 75
    unit2 = 200 - 75
    unit3 = unit - 200
    total_charge = unit1 * 5.26 + unit2 * 7.20 + unit3 * 7.59
elif unit >= 301 and unit <= 400:
    unit1 = 75
    unit2 = 200 - 75
    unit3 = 300 - 200
    unit4 = unit - 300
    total_charge = unit1 * 5.26 + unit2 * 7.20 + unit3 * 7.59 + unit4 * 8.02
elif unit >= 401 and unit <= 600:
    unit1 = 75
    unit2 = 200 - 75
    unit3 = 300 - 200
    unit4 = 400 - 300
    unit5 = unit - 400
    total_charge = unit1 * 5.26 + unit2 * 7.20 + unit3 * 7.59 + unit4 * 8.02 + unit5 * 12.67
elif unit > 600:
    unit1 = 75
    unit2 = 200 - 75
    unit3 = 300 - 200
    unit4 = 400 - 300
    unit5 = 600 - 400
    unit6 = unit - 600
    total_charge = unit1 * 5.26 + unit2 * 7.20 + unit3 * 7.59 + unit4 * 8.02 + unit5 * 12.67 + unit6 * 14.61

vat = total_charge * 5 / 100

final_charge = total_charge + vat

print("Vat: ", vat)
print("Total charge:", total_charge)
print("Final charge:", final_charge)