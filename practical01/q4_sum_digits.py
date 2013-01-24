# Filename: q4_sum_digits.py
# Author: Jason Hong
# Created: 20130122
# Modified: 20120122
# Description: Program to sum up digits in an integer between 0 and 1000

# main

# promt and get integer
Integer = int(input("Enter integer between 0 to 1000: "))

#reject invalid integer
if Integer <= 0:
    print("invalid integer")
elif Integer >= 1000:
    print("invalid integer")
else:

# Extract digits from the integer
    a= Integer // 100
    b= Integer % 100 // 10
    c= Integer %10

#Sum up the digits
    Sum = a + b + c

# display results
    print("Sum of digits= {0:.0f}".format(Sum))
