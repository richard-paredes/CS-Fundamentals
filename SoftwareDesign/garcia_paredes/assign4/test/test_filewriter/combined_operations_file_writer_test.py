from unittest import TestCase
from test_operations.combined_operations_test import CombinedOperationTests
from file_writer import FileWriter
from os import remove

class CombinedOperationsFileWriterTests(CombinedOperationTests, TestCase):
  TEST_FILE_NAME = "contents.txt"

  def create_writer(self, *operations):
    return FileWriter(self.TEST_FILE_NAME, *operations)
  
  def tearDown(self):
    self.writer.close()
    self.addCleanup(remove, self.TEST_FILE_NAME)