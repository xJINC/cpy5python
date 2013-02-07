# Filename: q01_check_even.py
# Author: Jason
# Created: 20130129
# Modified: 20130129
# Description: Program to check whether a number is even

# prompt user to enter integer
x = int(input("Enter integer: "))

# Check if it is even
if x % 2 == 1:
    print(format(x) + " is odd")
else:
    print("{0:}".format(x) + " is even")
