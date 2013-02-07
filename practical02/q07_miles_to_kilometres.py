# Filename: q07_miles_to_kilometres.py
# Author: Jason
# Created: 20130130
# Modified: 20130130
# Description: Program to display two tables side by side to convert miles to kilo

# Print results
print("{0} {1} {2} {3}".format("miles", "kilometres", "miles", "kilometres"))

i = 20
for x in range(1,11):
    if x == 10:
        print("{0} {1:11.3f} {2:>5} {3:10.3f}".format(x, x * 1.609, i, i * 1.609))
        i= i+5
    elif x < 7:
        print("{0} {1:11.3f} {2:>6} {3:9.3f}".format(x, x * 1.609, i, i * 1.609))
        i= i+5
    else:
        print("{0} {1:12.3f} {2:>5} {3:9.3f}".format(x, x * 1.609, i, i * 1.609))
        i= i+5
