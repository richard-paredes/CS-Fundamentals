# -*- coding: utf-8 -*-
"""
Richard Paredes
PSID: 1492535
COSC 1306
Homework #5
"""
def evenFormula(num):
    return int(num/2)

def oddFormula(num):
    return int(3*num + 1)

def performSequence(number):
    
    output = number
    sequence = [number]
    while (output > 1):
        if (output % 2 == 0):
            output = evenFormula(output)
        else:
            output = oddFormula(output)
        
        sequence.append(output)
    return sequence

def determineLargestSequence():
    limit = 2000000 # two million
    largestSequence = [1]
    correspondingNumber = 0
    for num in range(0, limit): # only positive numbers
        sequence = performSequence(num)
        if (len(sequence) > len(largestSequence)):
            correspondingNumber = num
            largestSequence = sequence
    printResult(correspondingNumber, largestSequence)

def printResult(number, sequence):
    print('The longest sequence is {} with a length of {}'.format(number, len(sequence)))
    print(sequence)

def main():
    determineLargestSequence()
main()
    
