# -*- coding: utf-8 -*-
"""

Richard Paredes
Homework #1

COSC1306

"""
import math

# finds the gallons of paint needed to cover the 4 walls and ceiling
def calculatePaint(length, width, height):
    GALLONS_PER_SQFT = 400
    # cover 4 walls + ceiling
    areaOfWalls = 2*(length*height) + 2*(width*height) + (width*height)
    gallonsNeeded = (areaOfWalls / GALLONS_PER_SQFT)
    return int(math.ceil(gallonsNeeded))

# finds the number of tiles needed to cover the floor   
def calculateTiles(length, width):
    TILES_PER_SQFT = 16
    # tiles must cover floor
    areaOfFloor = (length*width)
    tilesNeeded = areaOfFloor * TILES_PER_SQFT
    return int(math.ceil(tilesNeeded))
    
    
def main():
    length = float(input("Enter the length of the room in feet: "))
    width = float(input("Enter the width of the room in feet: "))
    height = float(input("Enter the height of the room in feet: "))
    print()
    print("The total paint needed to cover the walls and ceiling is", calculatePaint(length, width, height), "gallons.")
    print()
    print("A total of", calculateTiles(length, width), "tiles are needed to cover the floor.")

main()