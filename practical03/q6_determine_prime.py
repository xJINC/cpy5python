# Filename: q6_determine_prime.py
# Author: Jason Hong
# Created: 20130222
# Modified: 20120222
# Description: Program to determine whether an intger is a prime number

from math import *

def is_prime(n):
    for d in range (2, int(sqrt(n)+1)):
        if n % d == 0:
            return False
    return True

a = 0
b = 0
r = 0 #number of rows
while a >= 0:
    if is_prime(a) == True:
        print(int(a), end = " ")
        b = b + 1
        if b == 10:
            print(end = "\n")
            b = 0
            r = r + 1
            if r > 100:
                break
    a = a + 1
    
