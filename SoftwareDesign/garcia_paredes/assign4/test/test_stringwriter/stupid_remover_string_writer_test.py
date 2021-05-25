from unittest import TestCase
from test_operations.stupid_remover_write_operation_tests import StupidRemoverWriteOperationTests
from string_writer import StringWriter

class StupidRemoverStringWriterTests(StupidRemoverWriteOperationTests, TestCase):
  def create_writer(self, *operations):
    return StringWriter(*operations)