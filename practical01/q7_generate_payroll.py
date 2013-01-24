# Filename: q7_generate_payroll.py
# Author: Jason Hong
# Created: 20130122
# Modified: 20120122
# Description: Program to generate payroll

# main

# promt and get name
Name = (input("Enter Name: "))

# promt and get number of hours worked weekly
Hours = float(input("Enter number of hours worked weekly: "))

# promt and get hourly pay rate
Hourly = float(input("Enter hourly pay rate: "))

# promt and get CPF contribution rate
CPF = int(input("Enter CPF contribution rate(%): "))

# calculate gross pay
Gross = (Hours) * (Hourly)

# calculate CPF contribution
Contribution = (Gross) * (CPF) / 100

# calculate net pay
Net = Gross - Contribution

# Display payroll
print("Payroll statement for " + Name)
print("Number of hours worked in a week: " + "{0:.1f}".format(Hours))
print("Hourly pay rate: $" + "{0:.2f}".format(Hourly))
print("Gross pay = $" + "{0:.2f}".format(Gross))
print("CPF contribution at " + "{0:}".format(CPF) + "% = $" + "{0:.2f}".format(Contribution))
print("Net pay = $" + "{0:.2f}".format(Net))
