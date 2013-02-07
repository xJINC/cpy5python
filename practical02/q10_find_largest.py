# Filename: q10_find_largest.py
# Author: Jason Hong
# Created: 20130131
# Modified: 20120131
# Description: Program to find the largest integer n such that n^3 < 12000

n = 10000
running = True

while running:
    if n**3 > 12000:
        n = n - 1
    elif n**3 <= 12000:
        print("largest integer is: " "{0:.0f}".format(n))
        running = False
   
