class WriterTests:
  def setUp(self):
    self.writer = self.create_writer()

  def test_canary(self):
    self.assertTrue(True)
  
  def test_write_nothing_to_writer_is_ignored(self):
    self.assertEquals("", self.writer.get_contents())

  def test_write_string_to_writer_writes_to_target(self):
    self.writer.write("Hello")

    self.assertEquals("Hello", self.writer.get_contents())
  
  def test_write_string_twice_to_writer_writes_both_to_target(self):
    self.writer.write("Hello")
    self.writer.write(" World!")

    self.assertEquals("Hello World!", self.writer.get_contents())
  
  def test_write_close_write_to_writer_ignores_second_write(self):
    self.writer.write("Hello")
    self.writer.close()
    self.writer.write(" World!")

    self.assertEquals("Hello", self.writer.get_contents())
  
  def test_close_write_to_writer_ignores_write(self):
    self.writer.close()
    self.writer.write("Hello")

    self.assertEquals("", self.writer.get_contents())
