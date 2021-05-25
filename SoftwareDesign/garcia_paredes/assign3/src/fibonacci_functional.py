from functools import reduce

def fibonacci(position):
  if position < 0:
    raise ValueError("Invalid Fibonacci sequence position")

  return reduce(lambda series, _:[series[1], sum(series)], range(position), [0, 1])[1]    
