# Filename: q5_upper_to_lower.py
# Author: Jason Hong
# Created: 20130122
# Modified: 20120122
# Description: Program to convert uppercase letter to lowercase letter using ASCII

# main

# promt and get uppercase letter
Letter = (input("Enter a uppercase letter: "))

# Convert it to lowercase letter
Lowercase = chr(ord(Letter) + 32)

# display results
print("lowercase = {0:}".format(Lowercase))

