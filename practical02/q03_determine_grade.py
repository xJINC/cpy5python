# Filename: q03_determine_grade.py
# Author: Jason
# Created: 20130129
# Modified: 20130129
# Description: Program to determine grade of score that user enter

# Promt user to enter score
score = int(input("Enter score: "))

# Determine grade
if score<0 or score>100:
    print("Invalid score!")
if 0<= score <= 34:
    print("Grade is U")
if 35<= score <= 44:
    print("Grade is S")
if 45<= score <= 49:
    print("Grade is E")
if 50<= score <= 54:
    print("Grade is D")
if 55<= score <= 59:
    print("Grade is C")
if 60<= score <= 69:
    print("Grade is B")
if 70<= score <= 100:
    print("Grade is A")
