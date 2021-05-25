from unittest import TestCase
from test_operations.writer_test import WriterTests
from file_writer import FileWriter
from os import remove

class TestFileWriter(WriterTests, TestCase):
  TEST_FILE_NAME = "contents.txt"

  def create_writer(self):
    return FileWriter(self.TEST_FILE_NAME)
  
  def tearDown(self):
    self.writer.close()
    self.addCleanup(remove, self.TEST_FILE_NAME)
