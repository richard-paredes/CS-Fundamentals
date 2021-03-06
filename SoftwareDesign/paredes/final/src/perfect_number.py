from math import ceil, sqrt
from functools import reduce

def is_perfect_number(number):
  return number > 1 and number == reduce(lambda total, current: total + current + number // current if number % current == 0 else total, range(2, ceil(sqrt(number))), 1)

def generate_perfect_numbers_upto(number):
  return list(filter(is_perfect_number, range(1, number + 1)))