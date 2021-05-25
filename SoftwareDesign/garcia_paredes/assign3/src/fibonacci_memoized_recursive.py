from functools import partial
from fibonacci_recursive import fibonacci as recursive_fibonacci

def fibonacci(position, cache = [{}]):
  if position < 0:
    raise ValueError("Invalid Fibonacci sequence position")

  cache = cache[0] if cache else {0:1, 1:1}

  if position not in cache:
    cache[position] = recursive_fibonacci(position, partial(fibonacci, cache = [cache]))

  return cache[position]
