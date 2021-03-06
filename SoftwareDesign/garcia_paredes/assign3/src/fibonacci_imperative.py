def fibonacci(position):
  if position < 0:
    raise ValueError("Invalid Fibonacci sequence position")

  previous, current = 0, 1

  for _ in range(position): 
    previous, current = current, current + previous

  return current
