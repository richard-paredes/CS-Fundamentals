class FibonacciTest():
  def setUp(self):
    self.fibonacci = self.create_fibonacci()
 
  def test_canary(self):
    assert True == True
 
  def test_for_positions(self):
    for(position, expected) in [(0, 1), (1, 1), (2, 2), (3, 3), (5, 8), (10, 89)]:
      yield self.check_fibonacci, position, expected
  
  def test_for_invalid_position(self):
    try:
      self.fibonacci(-1)
    except ValueError as exception:
      assert str(exception) == "Invalid Fibonacci sequence position"
    else:
      assert False, "Expected error raised for invalid Fibonacci position"
    
  def check_fibonacci(self, position, expected):
    assert self.fibonacci(position) == expected