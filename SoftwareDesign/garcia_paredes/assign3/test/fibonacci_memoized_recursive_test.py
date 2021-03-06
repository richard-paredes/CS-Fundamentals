from time import perf_counter
from fibonacci_test import FibonacciTest
from fibonacci_recursive import fibonacci as recursive_fibonacci
from fibonacci_memoized_recursive import fibonacci as memoized_fibonacci

class TestFibonacciMemoizedRecursive(FibonacciTest):
  
  def create_fibonacci(self):
    return memoized_fibonacci

  def fibonacci_timer(self, fibonacci):
    start_time = perf_counter()
    fibonacci(30)
    end_time = perf_counter()
    
    return end_time - start_time
  
  def test_memoized_fibonacci_faster_than_recursive_fibonacci(self):
    recursive_time = self.fibonacci_timer(recursive_fibonacci)
    memoized_time = self.fibonacci_timer(memoized_fibonacci)

    assert memoized_time * 10 < recursive_time, f"Memoized function is not faster than non-memoized version.\nRecursive: {recursive_time} s\nMemoized: {memoized_time} s"