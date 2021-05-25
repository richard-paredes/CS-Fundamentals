from fibonacci_test import FibonacciTest
from fibonacci_recursive import fibonacci

class TestFibonacciRecursive(FibonacciTest):
  
  def create_fibonacci(self):
    return fibonacci