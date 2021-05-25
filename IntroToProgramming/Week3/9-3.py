# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 14:31:07 2019

@author: richa
"""

# =============================================================================
# Variables and Types
# =============================================================================

# =============================================================================
# type() - returns the data type of the value entered
# =============================================================================
type("hello") # <class 'str'>
type("5 + 3") # <class 'str'>
type(9) # <class 'int'>

# =============================================================================
# Longs in python3 : denoted by a large number followed with an L
# =============================================================================

# =============================================================================
# Floats have limited precision
# Ints have precise precision
# =============================================================================

# =============================================================================
# Type casting:
# str() -> converts input into strings
# int() -> converts int-like strings into integers
#       -> cannot parse float-like strings
#       -> can parse floats into integers (truncates: removes decimal completely)
# float() -> converts float-like strings into floats
# =============================================================================
str(9) # '9'
int('5') # 5
int(1412.324) # 1412
float('1412.324') # 1412.324
print(float(8.24))

var = type('9')
print(var, type(var))

# =============================================================================
# Python uses snake case:
# bigBrother --- big_brother
# =============================================================================

# =============================================================================
# OPERATORS:
# / -> division, always returns a float
# // -> floor division, returns a float if a float is used in the expression
# =============================================================================
