# Filename: q7_display_matrix.py
# Author: Jason Hong
# Created: 20130222
# Modified: 20120222
# Description: Program to display an n by n matrix

from random import *

def print_matrix(n):
    for i in range(0, n):
        for x in range (0, n):
            print(randint(0,1), end=" ")
        print(" ")

n = int(input("Enter a positive integer: "))
print_matrix(n)
