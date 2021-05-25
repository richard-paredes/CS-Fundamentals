from operators import lowercase, uppercase, stupid_remover, duplicate_remover

class CombinedOperationTests:
  
  def test_write_to_writer_with_uppercase_then_lowercase_operation_returns_lowercase(self):
    self.writer = self.create_writer(uppercase, lowercase) 
    
    self.writer.write("hello THERE")

    self.assertEquals("hello there", self.writer.get_contents())

  def test_write_to_writer_with_lowercase_then_uppercase_operation_returns_lowercase(self):
    self.writer = self.create_writer(lowercase, uppercase) 
    
    self.writer.write("hello THERE")

    self.assertEquals("HELLO THERE", self.writer.get_contents())
  
  def test_write_to_writer_with_lowercase_then_stupid_remover_returns_lowercase_and_stupid_removed(self):
    self.writer = self.create_writer(lowercase, stupid_remover)

    self.writer.write("hELLo stupid")

    self.assertEquals("hello s*****", self.writer.get_contents())

  def test_write_to_writer_wth_stupid_remover_then_lowercase_returns_stupid_removed_and_lowercase(self):
    self.writer = self.create_writer(stupid_remover, lowercase)

    self.writer.write("hELLo stupid")

    self.assertEquals("hello s*****", self.writer.get_contents())

  def test_write_to_writer_with_uppercase_then_stupid_remover_returns_uppercase_without_stupid_removed(self):
    self.writer = self.create_writer(uppercase, stupid_remover)

    self.writer.write("hELLo stupid")

    self.assertEquals("HELLO STUPID", self.writer.get_contents())
  
  def test_write_to_writer_with_stupid_remover_then_uppercase_returns_stupid_removed_and_uppercase(self):
    self.writer = self.create_writer(stupid_remover, uppercase)

    self.writer.write("hELLo stupid")

    self.assertEquals("HELLO S*****", self.writer.get_contents())
  
  def test_write_to_writer_with_duplicate_then_stupid_returns_with_duplicates_and_stupid_removed(self):
    self.writer = self.create_writer(duplicate_remover, stupid_remover)

    self.writer.write("This is really really stupid!!!")

    self.assertEquals("This is really s*****!!!", self.writer.get_contents())
  
  def test_write_to_writer_with_duplicate_then_stupid_remover_then_lowercase_returns_lowercase_with_duplicates_and_stupid_removed(self):
    self.writer = self.create_writer(duplicate_remover, stupid_remover, lowercase)

    self.writer.write("This is really really stupid!!!")

    self.assertEquals("this is really s*****!!!", self.writer.get_contents())

  def test_write_to_writer_with_duplicate_then_stupid_remover_then_uppercase_returns_uppercase_with_duplicates_and_stupid_removed(self):
    self.writer = self.create_writer(duplicate_remover, stupid_remover, uppercase)

    self.writer.write("This is really really stupid!!!")

    self.assertEquals("THIS IS REALLY S*****!!!", self.writer.get_contents())
  