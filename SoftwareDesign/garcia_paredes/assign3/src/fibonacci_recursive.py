def fibonacci(position, recursive = None):
  if position < 0:
    raise ValueError("Invalid Fibonacci sequence position")
  
  recursive = recursive or fibonacci
  
  return 1 if position < 2 else recursive(position - 2) + recursive(position - 1)
