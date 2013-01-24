# Filename: compute_bmi.py
# Author: Jason
# Created: 20130221
# Modified: 20130221
# Description: Program to get user weight and height and
# calculate body mass index (split up sentences so they are easier to read)

# main

# prompt and get weight
weight = int(input("Enter weight in kg: "))

# prompt and get height
height = float(input("Enter height in m: "))

# calculate bmi
bmi = weight / (height * height)

# display result
print("BMI ={0:.2f}".format(bmi))

# determine health risk
if bmi >= 27.5:
    print("High risk")
#elif bmi >= 23.5 and bmi <27.5
elif 23.5 <= bmi < 27.5:
    print("Moderate risk")
elif 18.5 <= bmi < 23:
    print("Healthy")
else:
    print("Malnutrition")
    
