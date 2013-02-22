# Filename: q8_convert_milliseconds.py
# Author: Jason Hong
# Created: 20130222
# Modified: 20120222
# Description: Program to display an n by n matrix


def convert_ms(n):
    seconds = n // 100
    minutes = seconds // 60
    hours = minutes // 60

    seconds = seconds - minutes * 60
    minutes = minutes - hours * 60

    return(str(hours)+"h " + str(minutes)+ "min " + str(seconds) + "s ")

n = int(input("Enter an integer: "))
print (convert_ms(n))
