# -*- coding: utf-8 -*-
"""
Richard Paredes
PSID: 1492535
COSC 1306
Assignment #8
"""
def printSearchResults(found, steps, searchType):
    message = "{} Search: Password {}found after {} step{}."
    if (found):
        if (steps < 2):
            print(message.format(searchType,"",steps,""))
        else:
            print(message.format(searchType,"",steps,"s"))
        print("Password found! You should change your password!")
    else:
        print(message.format(searchType,"NOT ",steps,"s"))

def linear_search(password, passwords):
    step = 0
    found = False
    while (step < len(passwords) and not found):
        if (passwords[step] == password):
            found = True
        step += 1
    printSearchResults(found, step, "Linear")

def binary_search(password, passwords):
    leftHalf = 0
    rightHalf = len(passwords)
    found = False
    step = 0
    while ((leftHalf <= rightHalf) and not found):
        midPoint = (leftHalf+rightHalf)//2
        if (passwords[midPoint] == password):
            found = True
        elif (passwords[midPoint] > password):
            rightHalf = midPoint-1
        else:
            leftHalf = midPoint+1
        step += 1
    printSearchResults(found, step, "Binary")


def main():
    shortFile = "passwords_short.txt"
    # longFile = "passwords_long.txt"
    with open(shortFile) as file:
        passwords = []
        print("Reading password data ... ", end='')
        for line in file:
            passwords.append(line.strip())
        print("Complete!")
    
    password = input("Please enther the password to search for: ")
    while (password != ''):
        linear_search(password, passwords)
        binary_search(password, passwords)
        print()
        password = input("Please enther the password to search for: ")
    print()
    print("Thank you and good bye!")
    
main()