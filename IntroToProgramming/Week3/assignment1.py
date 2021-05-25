# -*- coding: utf-8 -*-
"""
Richard Paredes
Assignment #1: Variables and Basic I/O
COSC 1306
"""
# libraries
import math

# user input
radius = float(input("Enter radius for a circle: "))

# calculations
circleArea = math.pi*(radius**2)
hexagonArea = ((3*math.sqrt(3))/2)*(radius**2)
shadedArea = circleArea - hexagonArea

# output
print()
print("="*40)
print("Circle area  =", circleArea)
print("Hexagon area =", hexagonArea)
print("Shaded area  =", shadedArea)
print("="*40)

# bonus:
# value: 1.839871
