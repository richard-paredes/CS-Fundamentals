from fibonacci_test import FibonacciTest
from fibonacci_functional import fibonacci

class TestFibonacciFunctional(FibonacciTest):
  
  def create_fibonacci(self):
    return fibonacci