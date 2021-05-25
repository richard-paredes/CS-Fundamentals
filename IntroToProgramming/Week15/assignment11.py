# -*- coding: utf-8 -*-
"""
Richard Paredes
PSID: 1492535
COSC 1306
Assignment #11
"""
def getWords(fileName):
    alphabet = [chr(letter) for letter in range(65,91)]
    letterFrequencies = { letter : 0 for letter in alphabet }
    totalLetters = 0
    with open(fileName) as file:
        for line in file:
            word = line.strip()
            for letter in word:
                letterFrequencies[letter] += 1
                totalLetters += 1
    
    return (letterFrequencies, totalLetters)

def main():
    fileName = 'zingarelli2005.txt'
    letterFrequencies, totalLetters = getWords(fileName)

    for letter in letterFrequencies:
        letterFrequency = (letterFrequencies[letter] / totalLetters) * 100
        print('{} - {:>6.3f}%'.format(letter, letterFrequency))

main()
