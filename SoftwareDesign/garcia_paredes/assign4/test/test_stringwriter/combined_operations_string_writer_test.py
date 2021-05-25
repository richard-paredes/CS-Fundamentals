from unittest import TestCase
from test_operations.combined_operations_test import CombinedOperationTests
from string_writer import StringWriter

class CombinedOperationsStringWriterTests(CombinedOperationTests, TestCase):
  def create_writer(self, *operations):
    return StringWriter(*operations)