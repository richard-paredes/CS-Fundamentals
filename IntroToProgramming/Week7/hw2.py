# -*- coding: utf-8 -*-
"""
Richard Paredes
PSID: 1492535
COSC 1306
Homework 2
"""

def in_mandelbrot(c):
    # Complex iterations
    ITERATIONS = 5000
    z = c

    for iteration in range(ITERATIONS):
        z = z*z + c
        temp = abs(z)
        # print(iteration, temp)
        if temp > 2:
            return False
    return True

def plot_mandelbrot(width, height, minimumX, maximumX, minimumY, maximumY):
    
    IN_CHAR = '*'
    OUT_CHAR = '-'
    for row in range(height):
        for col in range(width):
            x = (minimumX + (col*(maximumX-minimumX)/width))
            y = (minimumY + (row*(maximumY-minimumY)/height))
            z = complex(x,y)
            if (in_mandelbrot(z)):
                print(IN_CHAR, end='')
            else:
                print(OUT_CHAR,end='')
        print()

def main():
    width = int(input("Enter a width: "))
    height = int(input("Enter a height: "))
    minimumX = -2.0
    maximumX = 1.0
    minimumY = -1.0
    maximumY = 1.0
    
    # OPTIONAL: ADJUST DOMAIN AND RANGE OF PLOT
    '''
    minimumX = float(input("Enter the minimum X value of the display: "))
    maximumX = float(input("Enter the maximum X value of the display: "))
    minimumY = float(input("Enter the minimum Y value of the display: "))
    maximumY = float(input("Enter hte maximum Y value of the display: "))
    '''
    
    plot_mandelbrot(width, height, minimumX, maximumX, minimumY, maximumY)

main()