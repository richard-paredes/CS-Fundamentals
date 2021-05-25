# -*- coding: utf-8 -*-
'''

Richard Paredes
COSC 1306
Assignment # 5
'''

def printShapeOptions():
    print('1- Square')
    print('2- Rectangle')
    print('3- Right Triangle (left)')
    print('4- Right Triangle (right)')
    print('5- Diamond')
    print('0- Exit')

def getShape():
    print('Please select from the following shapes:')
    printShapeOptions()
    shape = int(input('Please enter your selection: '))
    while (shape < 0 or shape > 5):
        print('Invalid selection (',shape,')')
        shape = int(input('Please enter your selection: '))
    return shape

def getDimension(shape, dimension):
    measurement = int(input('Please enter the '+dimension+' of the '+shape+': '))
    while (measurement < 1):
        print('Invalid '+dimension+' (',measurement,'). Please enter a positive value.')
        measurement = int(input('Please enter the '+dimension+' of the '+shape+': '))
    return measurement

def drawSquare(size):
    print()
    for i in range(size):
        print('#'*size)

def drawRectangle(length, width):
    print()
    for i in range(width):
        print('!'*length)
        
def drawRightTriangle_L(size):
    print()
    for i in range(1,size+1):
        print('\\'*i)

def drawRightTriangle_R(size):
    print()
    for i in range(1,size+1):
        print(' '*(size-i), '/'*i)

def drawDiamond(size):
    print()
    for i in range(size):
        spaces = abs(i-size//2)
        characters = size - 2*spaces
        print(' '*spaces + '%'*characters)


def main():
    userChoice = getShape()
    
    while userChoice != 0:  
        
        if (userChoice == 1):
            shape = 'square'
            size = getDimension(shape, 'size')
            drawSquare(size)
        elif (userChoice == 2):
            shape = 'rectangle'
            length = getDimension(shape, 'length')
            width = getDimension(shape, 'width')
            drawRectangle(length, width)
        elif (userChoice == 3):
            shape = 'right triangle (left)'
            size = getDimension(shape, 'size')
            drawRightTriangle_L(size)
        elif (userChoice == 4):
            shape = 'right triangle (right)'
            size = getDimension(shape, 'size')
            drawRightTriangle_R(size)
        else:
            shape = 'diamond'
            size = getDimension(shape, 'size')
            # additional condition
            while (size % 2 == 0):
                print('Invalid size (',size,'). Please enter an odd value.')
                size = getDimension(shape, 'size')
            drawDiamond(size)
        print()
        userChoice = getShape()
    
    print('Good-Bye!')

main()