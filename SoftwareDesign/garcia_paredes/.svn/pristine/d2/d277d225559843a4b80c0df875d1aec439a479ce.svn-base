from operators import uppercase

class UpperCaseWriteOperationTests:
  def setUp(self):
    self.writer = self.create_writer(uppercase)

  def test_write_nothing_to_writer_with_uppercase_operations_returns_empty_string(self):
    self.assertEquals("", self.writer.get_contents())

  def test_write_mixed_case_to_writer_with_uppercase_operation_returns_uppercase(self):
    self.writer.write("hello THERE")

    self.assertEquals("HELLO THERE", self.writer.get_contents())

  def test_write_twice_to_writer_with_uppercase_operation_returns_uppercase(self):
    self.writer.write("hELLo")
    self.writer.write(" wORLD")

    self.assertEquals("HELLO WORLD", self.writer.get_contents())

  def test_write_close_write_to_writer_with_uppercase_operation_returns_first_write_uppercase(self):
    self.writer.write("heLLo")
    self.writer.close()
    self.writer.write(" thERe")

    self.assertEquals("HELLO", self.writer.get_contents())

  def test_close_write_to_writer_with_uppercase_operations_returns_empty_string(self):
    self.writer.close()
    self.writer.write("hELLo")

    self.assertEquals("", self.writer.get_contents())
