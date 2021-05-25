from operators import lowercase

class LowerCaseWriteOperationTests:
  def setUp(self):
    self.writer = self.create_writer(lowercase)

  def test_write_nothing_to_writer_with_lowercase_operations_returns_empty_string(self):
    self.assertEquals("", self.writer.get_contents())
  
  def test_write_mixed_case_to_writer_with_lowercase_operation_returns_lowercase(self):
    self.writer.write("hello THERE")

    self.assertEquals("hello there", self.writer.get_contents())

  def test_write_twice_to_writer_with_lowercase_operation_returns_lowercase(self):
    self.writer.write("hELLo")
    self.writer.write(" wORLD")

    self.assertEquals("hello world", self.writer.get_contents())

  def test_write_close_write_to_writer_with_lowercase_operation_returns_first_write_lowercase(self):
    self.writer.write("hELLo")
    self.writer.close()
    self.writer.write(" wORLD")

    self.assertEquals("hello", self.writer.get_contents())

  def test_close_write_to_writer_with_lowercase_operations_returns_empty_string(self):
    self.writer.close()
    self.writer.write("hELLo")

    self.assertEquals("", self.writer.get_contents())
