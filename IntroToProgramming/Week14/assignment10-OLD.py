# -*- coding: utf-8 -*-
"""
Richard Paredes
PSID: 1492535
COSC 1306
Assignment #10
"""

'''
1. Include a multi-line comments at the top of the file with your name, course number, and the
assignment number.
2. Your program should use functions and good programming style to solve the problem. No
user input is required.
3. Your program should determine the perimeter, less than 2019, with the most possible integersided right triangles and output this perimeter.
4. Your program should keep track of the possible triangles and output the triangles associated
with the maximal perimeter in sorted order.
Hint: Test your program with a smaller limit (200) to confirm that your program works with the
results that you are given.

'''
def isTwelveMultiple(a,b):
    return (a*b % 12 == 0)

def isRightTriangle(a,b,c):
    return (a*a + b*b == c*c)
        
def findSides(allPerimeters, perimeter):

    for a in range(1, (perimeter//3)):
        for b in range(a+1, (perimeter//2)):
            if (isTwelveMultiple(a,b) and isRightTriangle(a,b,perimeter-a-b)):
                
                if (perimeter not in allPerimeters):
                    allPerimeters[perimeter] = []
                
                allPerimeters[perimeter].append((a,b,perimeter-a-b))
    
    return

'''
    Fascinating properties of right triangles:
    a*b = 12 * k, where k is a scalar
    a % 3 = 0
    b % 5 = 0
    c % 12 = 0
    --> side 
'''
def generateTriangle1(triangle):
    a,b,c = triangle
    '''
        [
            1 -2 2
            2 -1 2
            2 -2 3
        ]
    '''
    _a = a - 2*b + 2*c
    _b = 2*a - b + 2*c
    _c = 2*a - 2*b + 3*c
    return tuple(sorted([_a,_b,_c]))

def generateTriangle2(triangle):
    a,b,c = triangle
    '''
        [
            1 2 2
            2 1 2
            2 2 3
        ]
    '''
    _a = a + 2*b + 2*c
    _b = 2*a + b + 2*c
    _c = 2*a + 2*b + 3*c
    return tuple(sorted([_a,_b,_c]))

def generateTriangle3(triangle):
    a,b,c = triangle
    '''
        [
            -1 2 2
            -2 1 2
            -2 2 3
        ]
    '''
    _a= -a + 2*b + 2*c
    _b= -2*a + b + 2*c
    _c= -2*a + 2*b + 3*c
    return tuple(sorted([_a,_b,_c]))

def determineMostTriangles(allPerimeters):
    # start with smallest pythagorean triple
    correspondingPerimeter = 12
    maxNumTriangles = len(allPerimeters[correspondingPerimeter])

    for perimeter in allPerimeters:
        numTriangles = len(allPerimeters[perimeter])
        if (numTriangles > maxNumTriangles):
            correspondingPerimeter = perimeter
            maxNumTriangles = numTriangles
        
    return (correspondingPerimeter, maxNumTriangles)

def printTriangles(allPerimeters, perimeter, numTriangles):
    print('The perimeter of {} gives a maximum number of {} triangles.'.format(perimeter, numTriangles))
    for triangle in allPerimeters[perimeter]:
        print(triangle)
    print()

def main():
    #perimeterLimit = 200
    perimeterLimit = 2019
    allPerimeters = {}
    for perimeter in range(12, perimeterLimit, 2):
        findSides(allPerimeters, perimeter)
    
    perimeter, numTriangles = determineMostTriangles(allPerimeters)
    printTriangles(allPerimeters, perimeter, numTriangles)
    
main()