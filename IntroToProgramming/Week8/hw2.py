
# if a point, given X and Y is inside a circle.
# check if center is inside the circle
def getCoordinate(width, height):
    for row in range(height):
        for col in range(width):
            x = -1 + (2 / (width - 1))*col
            y = -1 + (2 / (height - 1))*row

            if (x==0 and y==0):
                print('+', end='')
            elif (y == 0):
                print('-', end='')
            elif (x == 0):
                print('|', end='')
            elif (isInCircle(x, y)):
                print('0', end='')
            else:
                print(' ', end='')
        print()

def isInCircle(x, y):
    circle = x**2 + y**2
    return ( circle <= 1)

if __name__ == "__main__":
    width = 90
    height = 40
    getCoordinate(width, height)