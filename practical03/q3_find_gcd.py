# Filename: q3_find_gcd.py
# Author: Jason Hong
# Created: 20130221
# Modified: 20120221
# Description: Program to display the greatest common divisor

#main
def gcd(m, n):
    #find smaller integer
    d = 1
    if m < n:
        d = m
    elif n < m:
        d = n

#while loop to find greatest GCD
    while m % d != 0 or n % d != 0:
        d = d-1
        if m%d == 0 and n%d == 0:
              print(d)

(gcd(24,16))
(gcd(255,25))
