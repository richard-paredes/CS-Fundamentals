from fibonacci_test import FibonacciTest
from fibonacci_imperative import fibonacci

class TestFibonacciImperative(FibonacciTest):
  
  def create_fibonacci(self):
    return fibonacci
