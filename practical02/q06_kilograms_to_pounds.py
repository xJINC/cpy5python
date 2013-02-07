# Filename: q06_kilograms_to_pounds.py
# Author: Jason
# Created: 20130129
# Modified: 20130129
# Description: Program displaying a table to convert kilograms to pounds

# Print results
print("{0} {1}".format("kilograms", "pounds"))
      
for x in range(1,11):
    if x < 5 or x == 10:
        print("{0} {1:12.1f}".format(x, x * 2.2))
    else:
        print("{0} {1:13.1f}".format(x, x * 2.2))

    
