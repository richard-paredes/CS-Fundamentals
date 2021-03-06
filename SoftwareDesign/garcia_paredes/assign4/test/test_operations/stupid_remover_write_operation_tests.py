from operators import stupid_remover

class StupidRemoverWriteOperationTests:
  def setUp(self):
    self.writer = self.create_writer(stupid_remover)

  def test_write_nothing_to_writer_with_stupid_remover_operations_returns_empty_string(self):
    self.assertEquals("", self.writer.get_contents())

  def test_write_stupid_lowercase_to_writer_with_stupid_remover_operation_returns_replaced_stupid(self):
    self.writer.write("This is really really stupid!!!")

    self.assertEquals("This is really really s*****!!!", self.writer.get_contents())

  def test_write_stupid_uppercase_to_writer_with_stupid_remover_operation_returns_uppercase_stupid(self):
    self.writer.write("STUPID")

    self.assertEquals("STUPID", self.writer.get_contents())

  def test_write_stupid_mixedcase_to_writer_with_stupid_remover_operation_returns_mixed_case_stupid(self):
    self.writer.write("stUPId")

    self.assertEquals("stUPId", self.writer.get_contents())

  def test_write_twice_to_writer_with_stupid_remover_operation_returns_replaced_stupid(self):
    self.writer.write("stupid")
    self.writer.write(" stupid")

    self.assertEquals("s***** s*****", self.writer.get_contents())

  def test_write_close_write_to_writer_with_stupid_remover_operation_returns_first_asterisks(self):
    self.writer.write("stupid")
    self.writer.close()
    self.writer.write(" stupid")

    self.assertEquals("s*****", self.writer.get_contents())

  def test_close_write_to_writer_with_uppercase_operations_returns_empty_string(self):
    self.writer.close()
    self.writer.write("stupid")

    self.assertEquals("", self.writer.get_contents())
