# Filename: q02_triangle.py
# Author: Jason
# Created: 20130129
# Modified: 20130129
# Description: Program to check determine if a triangle is valid
# and display perimeter if triangle is valid

# Promt user to enter sides
a = float(input("Enter side 1: "))
b = float(input("Enter side 2: "))
c = float(input("Enter side 3: "))

# Determine if triange is valid
if a+b <= c or b+c <= a or a+c <= b:
    print("triangle is invalid")
else:
    print("Perimeter = {0:.2f}".format(a+b+c))
