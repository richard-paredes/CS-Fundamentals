# -*- coding: utf-8 -*-
"""

Richard Paredes
COSC 1306
Assignment #3

"""

# will find the letter grade corresponding
# to the final grade (using syllabus as guide)
def getLetterGrade(grade):
    if (grade >= 90):
        return 'A'
    elif (grade >= 86):
        return 'A-'
    elif (grade >= 82):
        return 'B+'
    elif (grade >= 78):
        return 'B'
    elif (grade >= 74):
        return 'B-'
    elif (grade >= 70):
        return 'C+'
    elif (grade >= 66):
        return 'C'
    elif (grade >= 62):
        return 'C-'
    elif (grade >= 58):
        return 'D+'
    elif (grade >= 54):
        return 'D'
    elif (grade >= 50):
        return 'D-'
    else:
        return 'F'

# will find the closest grade from the 
# current grade and print it out
def getGradeDifference(grade):
    grade_difference = 0
    next_letter_grade = ''
    if (grade < 50):
        grade_difference = (50 - grade)
        next_letter_grade = 'D-'
    elif (grade < 54):
        grade_difference = (54 - grade)
        next_letter_grade = 'D'
    elif (grade < 58):
        grade_difference = (58 - grade)
        next_letter_grade = 'D+'
    elif (grade < 62):
        grade_difference = (62 - grade)
        next_letter_grade = 'C-'
    elif (grade < 66):
        grade_difference = (66 - grade)
        next_letter_grade = 'C'
    elif (grade < 70):
        grade_difference = (70 - grade)
        next_letter_grade = 'C+'
    elif (grade < 74):
        grade_difference = (74 - grade)
        next_letter_grade = 'B-'
    elif (grade < 78):
        grade_difference = (78 - grade)
        next_letter_grade = 'B'
    elif (grade < 82):
        grade_difference = (82 - grade)
        next_letter_grade = 'B+'
    elif (grade < 86):
        grade_difference = (86 - grade)
        next_letter_grade = 'A-'
    elif (grade < 90):
        grade_difference = (90 - grade)
        next_letter_grade = 'A'
    
    # check whether or not there is a higher grade
    if (grade_difference > 0):
        print('You are only', round(grade_difference, 3), 'points away from the cutoff for a/an', next_letter_grade + '!')
    else:
        print('You already have an A. There is no higher grade!')

# calls all the necessary functions  
def main():
    final_average = float(input("Please enter a final average: "))
    letter_grade = getLetterGrade(final_average)
    print()
    print("Congratulations, you earned a/an", letter_grade + ".")
    print()
    getGradeDifference(final_average)

main()

