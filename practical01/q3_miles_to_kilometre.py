# Filename: q3_miles_to_kilometre.py
# Author: Jason
# Created: 20130221
# Modified: 20130221
# Description: Program to convert length from miles to kilometre

# main

# prompt and get length in miles
Miles = int(input("Enter distance in miles: "))

# convert length to kilometre
Km = Miles * 1.60934

# display result
print("Distance in Km ={0:.3f}".format(Km))
