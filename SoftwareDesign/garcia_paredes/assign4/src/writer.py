from functools import reduce, partial

class Writer:
  def __init__(self, *operations):
    self.operation = partial(reduce, lambda text, operator: operator(text), operations)
  
  def write(self, message):
    self.write_to_target(self.operation(message))