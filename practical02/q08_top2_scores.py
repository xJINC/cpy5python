# Filename: q08_top2_scores.py
# Author: Jason Hong
# Created: 20130201
# Modified: 20130201
# Description: Program to display the names and scores of the top 2 pupil

# Promt user to input number of students
people = int(input("Enter number of students: "))

# Declare misc variables
i = 0
top_score = 0
second_score = 0
top_name = str("name")
second_name = str("name2")
running = True

# prompt user to enter names and scores using a while loop
while (people > i):
    name = str(input("Enter name of student: "))
    score = int(input("Enter score of " + str(name) + ": "))
    i = i + 1
    
    if people == i:
        running = False
        print((top_name) + " has the highest score of " + str(top_score))
        print((second_name) + " has the second highest score of " + str(second_score))

    elif top_score <= score:
        second_score = int(top_score)
        second_name = str(top_name)
        top_score = int(score)
        top_name = str(name)
        
    elif top_score >= score and second_score <= score:
        top_score = int(top_score)
        top_name = str(top_name)
        second_score = int(score)
        second_name = str(name)

    elif top_score >= score and second_score >= score:
        top_score = int(top_score)
        top_name = str(top_name)
        second_score = int(second_score)
        second_name = str(second_name)

    
