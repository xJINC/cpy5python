# Filename: q6_find_ascii_char.py
# Author: Jason Hong
# Created: 20130122
# Modified: 20120122
# Description: Program to find the character of an ASCII code

# main

# promt and get ASCII code
ASCII = int(input("Enter ASCII code: "))

# set limit for integer
if 0 < ASCII < 127:

# Convert it to a character
    Character = chr(ASCII)

# display results
    print("Character = {0:}".format(Character))

# reject undefined ASCII value
else:
    print("invalid ASCII value")
