# Filename: q1_farenheit_to_celcius.py
# Author: Jason
# Created: 20130222
# Modified: 20130222
# Description: Program to convert farenheit to celcius

# main

# promt and get temperature in farenheit
Farenheit = float(input("Enter temperature in farenheit: "))

# convert to temperature in celcius

Temperature = (Farenheit - 32) * (5/9)

# display result
print("Celcius ={0:.1f}".format(Temperature) + ("°C"))
