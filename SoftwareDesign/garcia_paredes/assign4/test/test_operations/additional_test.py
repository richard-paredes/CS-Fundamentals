from unittest import TestCase
from string_writer import StringWriter
from operators import lowercase, uppercase, stupid_remover, duplicate_remover

class AdditionalTests(TestCase):
  def test_replace_multiple_stupid_words(self):
    string_writer = StringWriter(stupid_remover)
    string_writer.write("This is stupid really stupid")

    self.assertEquals("This is s***** really s*****", string_writer.get_contents())

  def test_donot_replace_capitalized_stupid_word(self):
    string_writer = StringWriter(stupid_remover)
    string_writer.write("This is Stupid")

    self.assertEquals("This is Stupid", string_writer.get_contents())

#  def test_donot_replace_embedded_stupid_word(self):
#    string_writer = StringWriter(stupid_remover)
#    string_writer.write("This is stupidest")
#
#    self.assertEquals("This is stupidest", string_writer.get_contents())

  def test_replace_three_consequetive_duplicated_words(self):
    string_writer = StringWriter(duplicate_remover)
    string_writer.write("This is duplicate duplicate duplicate")

    self.assertEquals("This is duplicate", string_writer.get_contents())

  def test_donot_replace_non_consequetive_repeated_words(self):
    string_writer = StringWriter(duplicate_remover)
    string_writer.write("Is this a duplicate no not a duplicate")

    self.assertEquals("Is this a duplicate no not a duplicate", string_writer.get_contents())

  def test_lower_stupid_duplicate_combination(self):
    string_writer = StringWriter(lowercase, stupid_remover, duplicate_remover)
    string_writer.write("This is a stupid stupid test")

    self.assertEquals("this is a s***** test", string_writer.get_contents())
