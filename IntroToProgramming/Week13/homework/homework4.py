# -*- coding: utf-8 -*-
"""
Richard Paredes
PSID: 1492535
COSC 1306
Homework #4
"""
def openFile(fileName):
    with open(fileName) as file:
        filteredWords = []
        for line in file:
            word = line.strip()
            filteredWords.append(word)  
    return filteredWords

def getWordDictionary(words):
    # dictionary groups words based on length
    wordsDictionary = {}
    for word in words:
        key = ('').join(sorted(word)) # could use a tuple here. . 
        if (key in wordsDictionary):
            wordsDictionary[key].append(word)
        else:
            wordsDictionary[key] = [ word ] 
    return wordsDictionary
    
def sortAnagramsBySize(wordsDictionary):
    anagrams = {}
    for key in wordsDictionary:
        size = len(wordsDictionary[key])
        if (size in anagrams):
            anagrams[size].append(key)
        else:
            anagrams[size] = [ key ]
    return anagrams

def getAnagramSize(minSize, maxSize):
    anagramSize = int(input("Please enter the anagram group size ({}-{}) or 0 to quit: ".format(minSize,maxSize)))
    while (anagramSize < minSize and anagramSize != 0) or (anagramSize > maxSize):
        print('There are no anagrams of that size.')
        print()
        anagramSize = int(input("Please enter the anagram group size ({}-{}) or 0 to quit: ".format(minSize,maxSize)))
    return anagramSize


def printAnagrams(wordDictionary, anagrams, size):
    print()
    for anagramSignature in anagrams[size]:
        print(wordDictionary[anagramSignature])

def main():
    fileName="words.txt"
    words = openFile(fileName)
    
    wordDictionary = getWordDictionary(words)
    anagrams = sortAnagramsBySize(wordDictionary)
    minSize = min(anagrams.keys())
    maxSize = max(anagrams.keys())
    anagramSize = getAnagramSize(minSize,maxSize)
    while (anagramSize != 0):
        printAnagrams(wordDictionary, anagrams, anagramSize)
        print()
        anagramSize=getAnagramSize(minSize,maxSize)
    print()
    print("Thank you. Good bye!")
    
main()