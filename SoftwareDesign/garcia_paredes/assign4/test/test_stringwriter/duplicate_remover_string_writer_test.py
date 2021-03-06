from unittest import TestCase
from test_operations.duplicate_remover_write_operation_tests import DuplicateRemoverWriteOperationTests
from string_writer import StringWriter
from os import remove

class DuplicateRemoverStringWriterTests(DuplicateRemoverWriteOperationTests, TestCase):
  def create_writer(self, *operations):
    return StringWriter(*operations)
