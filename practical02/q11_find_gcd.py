# Filename: q11_find_gcd.py
# Author: Jason Hong
# Created: 20130131
# Modified: 20120131
# Description: Program to find the greatest common divisor of two integers

#prompt and get integers
n1 = int(input("Enter first integer: "))
n2 = int(input("Enter second integer: "))

#find smaller integer
if n1 == n2:
    print("Greatest common divisor is: " "{0}".format(n1))
elif n1 < n2:
    d = n1
elif n2 < n1:
    d = n2

#while loop to find greatest GCD
    running = True
    while running:
          if n1 % d != 0 or n2 % d != 0:
              d = d - 1
          elif n1 % d == 0 and n2 % d == 0:
              print("Greatest common divisor is: " "{0}".format(d))
              running = False
          
