# -*- coding: utf-8 -*-
"""
Richard Paredes
PSID: 1492535
COSC 1306
Assignment #9
"""
def openFile(fileName):
    threeLetterWords = []
    fourLetterWords = []
    with open(fileName) as file:
        for line in file:
            word = line.strip()
            if (len(word) == 3):
                threeLetterWords.append(word)
            if (len(word) == 4):
                fourLetterWords.append(word)
    words = { "ThreeLetterWords":threeLetterWords, "FourLetterWords":fourLetterWords }
    return words

def getTable():
    phoneLetters = {
        0: 'O',
        1: 'LI',
        2: 'ABC',
        3: 'DEF',
        4: 'GHI',
        5: 'JKL',
        6: 'MNO',
        7: 'PQRS',
        8: 'TUV',
        9: 'WXYZ'
    }
    return phoneLetters

def getNumber():
    return input("Please enter a phone number (###-####): ")

def askToContinue():
    answer = input("Try another (Y/N)? ")
    print()
    shouldContinue = (answer[0].upper() == 'Y')
    return shouldContinue

def getWordsFromPhoneNumber(phoneNumber, words):
    possibleThreeLetterWords = getWords(phoneNumber[:3])
    possibleFourLetterWords = getWords(phoneNumber[4:])

    for firstWord in possibleThreeLetterWords:
        if (firstWord in words["ThreeLetterWords"]):
            for secondWord in possibleFourLetterWords:
                if (secondWord in words["FourLetterWords"]):
                    print(firstWord + '-' + secondWord)
    print()
    
    
def getWords(phoneNumber):
    phoneLetters = getTable()
    possibleWords = [""]

    for digitChar in phoneNumber:
        phoneDigit = int(digitChar)
        possibleWords = wordBuilder(possibleWords, phoneLetters[phoneDigit])
    return possibleWords

def wordBuilder(first, second):
    result = []
    for a in first:
        for b in second:
            result.append(a+b)
    return result      

def main():
    fileName="words.txt"
    words = openFile(fileName)
    shouldContinue = True
    while (shouldContinue):
        phoneNumber = getNumber()
        getWordsFromPhoneNumber(phoneNumber, words)
        shouldContinue = askToContinue()
    print("Good-Bye!")
main()
