# Filename: q09_find_smallest.py
# Author: Jason Hong
# Created: 20130131
# Modified: 20120131
# Description: Program to find the smallest integer n such that n^2 > 12000

n = 1
running = True

while running:
    if n**2 < 12000:
        n = n + 1
    elif n**2 >= 12000:
        print("smallest integer is: " "{0}".format(n))
        running = False
   
