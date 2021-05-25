# -*- coding: utf-8 -*-
"""
Richard Paredes
COSC 1306

Assignment #4
"""

import math

def get_number():
  number = float(input("Please enter a number: "))
  while number < 0:
    print("The number you entered was negative.")
    print("Please enter a positive number.")
    number = float(input("Please enter a number: "))
    
  return number

def newton(num, steps):
  guess = 2
  count = 0
  while count < steps:
    guess = (guess + num/guess)/2
    count += 1

  return guess

def work(value):
  print("Steps = Value")
  i = 1
  while i <= 16:
    print(i,"=", newton(value,i))
    i *= 2

  print("sqrt =", math.sqrt(value))
  print("="*40)

def main():
  value = 1
  while value != 0:
    value = get_number()
    if (value != 0):
      work(value)
  print("Thank you, Good Bye!")

main()