# Filename: q4_sum_series.py
# Author: Jason Hong
# Created: 20130222
# Modified: 20120222
# Description: Program to sum a series

def m_series(i):
    add = 0.000 #define sum variable
    print ("i","    ","m(i)") #header
    for n in range(2, i+2): #numerator range
        for d in range (1, n+1): #denominator range
            add = add + float((d-1)/d) #result
        print (n-1, " "*(5-len(str(n-1))), "{0:>.4f}".format(add))
        add = 0.0000

m_series(20)
