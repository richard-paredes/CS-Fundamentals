# -*- coding: utf-8 -*-
"""
Richard Paredes
PSID: 1492535
COSC 1306
Assignment #10
"""

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

def getTriangles(allPerimeters, baseTriangle, limit, isScaled=False):
    perimeter = sum(baseTriangle)

    if (perimeter > limit):
        return
    if (perimeter not in allPerimeters):
        allPerimeters[perimeter] = []
    if (baseTriangle not in allPerimeters[perimeter]):
        allPerimeters[perimeter].append(baseTriangle)    

    multiple = 1
    nextTriangle = baseTriangle

    while (not isScaled and sum(nextTriangle) < limit):
        getTriangles(allPerimeters, nextTriangle, limit, True)

        tri_1 = generateTriangle1(nextTriangle)
        getTriangles(allPerimeters, tri_1, limit)

        tri_2 = generateTriangle2(nextTriangle)
        getTriangles(allPerimeters, tri_2, limit)

        tri_3 = generateTriangle3(nextTriangle)
        getTriangles(allPerimeters, tri_3, limit)

        multiple += 1  
        nextTriangle = tuple([multiple* side for side in baseTriangle])        

def determineMostTriangles(allPerimeters):
    # start with smallest pythagorean triple
    correspondingPerimeter = 12
    maxNumTriangles = len(allPerimeters[correspondingPerimeter])

    for perimeter in sorted(allPerimeters.keys()):
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
    allPerimeters = {}
    # start with smallest pythagorean triple
    baseTriangle = (3, 4, 5)
    getTriangles(allPerimeters, baseTriangle, 2019)
    perimeter, numTriangles = determineMostTriangles(allPerimeters)
    printTriangles(allPerimeters, perimeter, numTriangles)
main()