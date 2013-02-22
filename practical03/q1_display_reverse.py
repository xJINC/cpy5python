# Filename: q1_display_reverse.py
# Author: Jason Hong
# Created: 20130219
# Modified: 20120219
# Description: Program to display an integer in reverse

def reverse_int(n):
    return int(str(n)[::-1])
   
# main
x = int(input("Input an integer: "))
print("Reversed integer is: " + str(reverse_int(x)))


## 532 // 10 = 53  532 % 10 = 2
## 53 // 10 = 5    53  % 10 = 3
## 5 // 10   = 0   5   % 10 = 5
