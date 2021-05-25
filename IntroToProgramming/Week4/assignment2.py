# -*- coding: utf-8 -*-
"""

Richard Paredes
Assignment #2
COSC1306

"""
# instead of using math.ceil()
def roundUp(number):
    return int(number+0.999999999999)

# determines area of the floor
def  getRoomArea(length, width):
    area = length*width
    return roundUp(area)

# determines number of liters needed to cover area
def getLitersNeeded(area):
    SQM_PER_LITER = 6
    liters = area / SQM_PER_LITER
    return roundUp(liters)

# determines number of bottles needed for given liters
def getBottlesNeeded(liters):
    LITERS_PER_BOTTLE = 2
    bottles = liters / LITERS_PER_BOTTLE
    return roundUp(bottles)

# determines total cost of bottles needed
def getCost(bottles, costPerBottle):
    totalCost = bottles * costPerBottle
    return roundUp(totalCost)

def main():
    # get input from user
    length = float(input("Enter the length of the room (m): "))
    width = float(input("Enter the width of the room (m): "))
    cost = float(input("Enter the cost per bottle ($): "))
    
    # get calculated values
    area = getRoomArea(length, width)
    liters = getLitersNeeded(area)
    bottles = getBottlesNeeded(liters)
    totalCost = getCost(bottles, cost)
    
    # prints the output
    print()
    print('='*40)
    print('Room area     (m2) =', area)
    print('Sealant needed (L) =', liters)
    print('Bottles needed     =', bottles)
    print('Total Cost     ($) =', totalCost)
    print('='*40)
    
main()
    