from operators import duplicate_remover

class DuplicateRemoverWriteOperationTests:
  def setUp(self):
    self.writer = self.create_writer(duplicate_remover)

  def test_write_nothing_to_writer_with_duplicate_remover_operations_returns_empty_string(self):
    self.assertEquals("", self.writer.get_contents())

  def test_write_duplicate_lowercase_to_writer_with_duplicate_remover_operation_returns_without_duplicate(self):
    self.writer.write("hello hello")

    self.assertEquals("hello", self.writer.get_contents())

  def test_write_duplicate_uppercase_to_writer_with_duplicate_remover_operation_returns_without_duplicate(self):
    self.writer.write("HELLO HELLO")

    self.assertEquals("HELLO", self.writer.get_contents())

  def test_write_nonconsecutive_duplicate_to_writer_with_duplicate_remover_operation_returns_duplicates(self):
    self.writer.write("hello world hello")

    self.assertEquals("hello world hello", self.writer.get_contents())

  def test_write_mixedcase_to_writer_with_duplicate_remover_operation_returns_mixed_case_with_duplicate(self):
    self.writer.write("hello HELLO")

    self.assertEquals("hello HELLO", self.writer.get_contents())

  def test_write_twice_to_writer_with_duplicate_remover_operation_returns_with_duplicate(self):
    self.writer.write("hello")
    self.writer.write(" hello")

    self.assertEquals("hello hello", self.writer.get_contents())

  def test_write_close_write_to_writer_with_duplicate_remover_operation_returns_first_without_duplicate(self):
    self.writer.write("hello hello")
    self.writer.close()
    self.writer.write(" world world")

    self.assertEquals("hello", self.writer.get_contents())

  def test_close_write_to_writer_with_uppercase_operations_returns_empty_string(self):
    self.writer.close()
    self.writer.write("hello hello")

    self.assertEquals("", self.writer.get_contents())
