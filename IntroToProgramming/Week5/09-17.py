# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 14:18:43 2019

@author: richa
"""
# Conditional Execution:

'''
    Boolean Logic
    Logical operations
    The 'if' statement
    Practice with 'if', 'else', 'elif'
    ==, <, >, <=, >=
    AND, OR, NOT
    truth tables!!
'''

# Determines if a number is negative
def isNegative():
    num = eval(input('Please enter a number: '))
    if (num == 0):
        print('You entered zero!')
    elif (num > 0):
        print('You entered a negative number!')
        print('I fixed it for you:', num*-1)
    else:
        print('You entered a positive number!')
    
    return

def isEven():
    num = eval(input('Please enter a number: '))
    if (num % 2 == 0):
        print('You entered an even number!')
    else:
        print('You entered an odd number!')

def isLeapYear():
    year = int(input('Please enter a year: '))
    if (year % 4 == 0):
        if (year % 100 == 0 and not year % 400 == 0):
            print(year, 'is not a leap year!')
            return False
        print(year, 'is a leap year!')
        return True
    print(year, 'is not a leap year!')
    return False
Def get_input():
    return input("enter:")

def main():
    # isNegative()
    # isEven()
    isLeapYear()
    
main()


