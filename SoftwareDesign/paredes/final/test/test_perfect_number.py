from unittest import TestCase
from perfect_number import is_perfect_number, generate_perfect_numbers_upto

class TestPerfectNumber(TestCase):
  def test_canary(self):
    self.assertTrue(True)

  def test_is_perfect_number_for_negative_1_returns_false(self):
    self.assertFalse(is_perfect_number(-1))

  def test_is_perfect_number_for_1_returns_false(self):
    self.assertFalse(is_perfect_number(1))

  def test_is_perfect_number_for_6_returns_true(self):
    self.assertTrue(is_perfect_number(6))

  def test_is_perfect_number_for_14_returns_false(self):
    self.assertFalse(is_perfect_number(14))

  def test_is_perfect_number_for_28_returns_true(self):
    self.assertTrue(is_perfect_number(28))

  def test_generate_perfect_numbers_upto_negative_1_returns_empty_list(self):
    self.assertEquals([], generate_perfect_numbers_upto(-1))

  def test_generate_perfect_numbers_upto_1_returns_empty_list(self):
    self.assertEquals([], generate_perfect_numbers_upto(1))

  def test_generate_perfect_numbers_upto_6_returns_list_with_6(self):
    self.assertEquals([6], generate_perfect_numbers_upto(6))

  def test_generate_perfect_numbers_upto_14_returns_list_with_6(self):
    self.assertEquals([6], generate_perfect_numbers_upto(14))

  def test_generate_perfect_numbers_upto_28_returns_list_with_6_and_28(self):
    self.assertEquals([6, 28], generate_perfect_numbers_upto(28))
