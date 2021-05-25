from unittest import TestCase
from test_operations.uppercase_write_operation_test import UpperCaseWriteOperationTests
from string_writer import StringWriter

class UpperCaseStringWriterTests(UpperCaseWriteOperationTests, TestCase):
  def create_writer(self, *operations):
    return StringWriter(*operations)