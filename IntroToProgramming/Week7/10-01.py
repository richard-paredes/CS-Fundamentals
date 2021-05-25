''' 
utf-8
Richard Paredes
More Loops:
    - For loops
'''

# Range()
'''
@params:
    3 overloads:
        1) range(stop-value)
        2) range(start-value, stop-value)
        3) range(start-value, stop-value, step-size)
    * stop-value is non-inclusive
    * start-value is inclusive
    * range starts at 0 if not specified
'''
for x in range(2,10):
    print(x)

x=0
while x < 0:
    print(x)
    x += 1

# print a square checkerboard
def draw_square(size):
    for i in range(size):
        if (i % 2 == 0):
            print('XO'*size)
        else:
            print('OX'*size)

# print a rectangular checkerboard
def draw_rectangle(height, width):
    for i in range(height):
        for j in range(width):
            if ((i+j) % 2 == 0):
                print('X', end='')
            else:
                print('O',end='')

            '''
            if (i % 2 == 0):
                if (j % 2 == 0):
                    print('X', end='')
                else:
                    print('O', end='')
            else: 
                if (j % 2 == 0):
                    print('O',end='')
                else:
                    print('X',end='')
            '''
        print()

def main():
    draw_square(3)
    draw_rectangle(3,4)
main()