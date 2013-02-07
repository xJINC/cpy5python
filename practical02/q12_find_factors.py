# Filename: q12_find_factors.py
# Author: Jason Hong
# Created: 20130201
# Modified: 20120201
# Description: Program to find the factors of an integer

# promt to get integer
x = int(input("Enter Integer: "))
i = 2
# get factors
while (x / i >= 1):
    if (x % i == 0):
        print(i)
        x = x / i
    else:
        i = i + 1
