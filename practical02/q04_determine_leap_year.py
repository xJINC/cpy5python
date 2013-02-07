# Filename: q04_determine_leap_year.py
# Author: Jason
# Created: 20130129
# Modified: 20130129
# Description: Program to determine if year entered by user is a leap year

# Prompt for year
year = int(input("Enter year: "))

# Determine whether year is a leap year
if year % 4 == 0 and year % 100 != 0:
    print("Leap Year!")
elif year % 400 == 0:
    print("Leap Year!")
else:
    print("Non-leap Year")

