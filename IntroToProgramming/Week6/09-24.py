# -*- coding: utf-8 -*-
"""

Richard Paredes
COSC 1306
Week 6:
    Looping
"""

# while loops:
''' 
    will loop until condition is met 
    features:
        start
        step
        end
'''
condition = True
while condition:
    print("Hello World")
    condition = False

# useful for:
'''
    Generating sequence of numbers
    repeat tasks
'''

# 0, 1, 2, 3, 4, finished
x = 0
while (x < 5):
    print(x)
    x += 1
print('Finished')

# 0, 3, 6, 9, 12, finished
x = 0
while (x < 15):
    print(x)
    x += 3
print('Finished')

# 10, 8, 6, 4, 2, 0, finished
x = 10
while (x >= 0):
    print(x)
    x -= 2
print('Finished')

# FizzBuzz problem
'''
Count by 1,
if # divisible by 3, say Fizz
if # divisible by 5, say Buzz
otherwise, say #
'''
def fizzBuzz(num):
    
    while (num < 100):
        if (num % 3 == 0 and num % 5 == 0):
            print('FizzBuzz')
        elif (num % 3 == 0):
            print('Fizz')
        elif (num % 5 == 0):
            print('Buzz')
        else: 
            print(num)
        num += 1

# Loop Practice
''' 
    Print Rectangles
    Print Triangles
    Determine Prime
    Do Euclid's Algorithm
'''

def printRectangle(height, width):
    count = 0
    while (count < height):
        print('='*width)
        count += 1

def printTriangle(base):
    count = 1
    while (count <= base):
        print('*'*count)
        count += 1
    
def isPrime(num):
    if (num == 2 or num == 1):
        return True
    elif (num % 2 == 0):
        return False
    elif (num > 1):
        count = 3
        sqroot = int(num ** (1/2))
        
        while(count <= sqroot):
            if (num % count == 0):
                return False
            count += 2
        return True
    else:
        return False


def main():
    height = int(input("Please enter a length: "))
    width = int(input("Please enter a width: "))
    printRectangle(height, width)
    printTriangle(width)
    num = int(input("Enter a number: "))
    print(isPrime(num))
main()