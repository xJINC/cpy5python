# Filename: q05_find_month_days.py
# Author: Jason
# Created: 20130129
# Modified: 20130129
# Description: Program to display number of days in a month

# Promt user to enter year and month
year = int(input("Enter year: "))
month_no = int(input("Enter month (e.g. January = 1, March = 3): "))
month_list = ["January", "February", "March", "April", "May", "June",\
              "July", "August", "September", "October", "November", "December"]
month = month_list[month_no - 1]
#Determine if year is a leap year and display results
if month_no == 1 or month == 3 or month == 5 or month == 7 or month == 8 \
or month_no == 10 or month == 12:
    print(format(month) + format(year) + " has 31 days")
elif month_no == 4 or month == 6 or month == 9 or month == 11:
    print(format(month) + format(year) + "has 30 days")
else:
    if year % 4 == 0 and year % 100 != 0 and month_no == 2:
        print(format(month) + " " + format(year) + " has 29 days")
    elif year % 400 == 0 and month == 2:
        print(format(month) + " " + format(year) + " has 29 days")
    else:
        print(format(month) + " " + format(year) + " has 28 days")
