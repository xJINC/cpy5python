# Filename: q5_compute_series.py
# Author: Jason Hong
# Created: 20130222
# Modified: 20120222
# Description: Program to compute a series

def c_series(i):
    sum = 0.0000 #define variable
    print ("i", "    ", "m(i)") #header
    j = 1
    while j <= i: #using while loop
        sum = sum + (1 /(2*j - 1)) #do all the addition
        sum = sum - (1 /(2*j + 1)) #do all the subtraction
        print (j, " "*(5-len(str(j))), "{0:>.11f}".format(sum * 4.0))
        j = j + 2

c_series(19)
