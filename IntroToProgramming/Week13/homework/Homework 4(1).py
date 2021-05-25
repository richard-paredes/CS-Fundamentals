#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dan Biediger
Homework #4 - First Look
"""

def get_sig(word): # Get the signature for a given word
    temp = list(word)
    temp.sort()
    return tuple(temp)


# Read in all the words for processing
words = []
with open("words.txt") as file:
    for word in file.readlines():
        word = word.strip()
        if len(word) == 3:
            words.append(word)


# Begin the main body of the program here
for word in words:
    print(word, get_sig(word))