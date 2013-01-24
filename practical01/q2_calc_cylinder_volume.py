# Filename: q2_calc_cylinder_volume.py
# Author: Jason
# Created: 2130222
# Modified: 20130222
# Description: Program to get the radius and height of cylinder and
# calculate volume of cylinder

# main

# Promt and get radius of base
Radius = float(input("Enter radius in cm: "))

# Promt and get height of cylinder
Height = float(input("Enter radius in cm: "))

# Calculate volume of Cylinder
from math import pi
Volume = (pi) * (Radius) * (Radius) * (Height)

# Display result
print("Volume ={0:.2f}".format(Volume))
