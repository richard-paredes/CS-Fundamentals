from unittest import TestCase
from test_operations.writer_test import WriterTests
from string_writer import StringWriter

class TestStringWriter(WriterTests, TestCase):
  def create_writer(self):
    return StringWriter()
