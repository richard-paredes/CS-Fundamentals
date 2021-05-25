
'''
    Fascinating properties of right triangles:
    a*b = 12 * k, where k is a scalar
    a % 3 = 0
    b % 5 = 0
    c % 12 = 0
    
'''
def getPossibleTrianglesForPerimeter(perimeter, triangles): 

    # all triangle perimeters are even
    if perimeter % 2 == 0 : 
        count = 0
        for sideB in range(1, perimeter // 3): 
            sideA = (perimeter / 2) * (perimeter - 2*sideB) / (perimeter - sideB)
            
            if (sideA.is_integer()): 
                triangle = tuple(sorted((int(sideA), sideB, perimeter-int(sideA)-sideB))) 

                if (perimeter not in triangles): 
                    triangles[perimeter] = [triangle]
                else:
                    triangles[perimeter].append(triangle)         
    return

def main():
    triangles={}
    for i in range(12, 2019):
        getPossibleTrianglesForPerimeter(i, triangles)
    for perimeter in triangles:
        print(perimeter, ':', triangles[perimeter])
        

main()

