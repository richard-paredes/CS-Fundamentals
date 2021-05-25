from unittest import TestCase, mock
from requests import head
from spell_check_service import get_response, is_spelling_correct, parse_text

class SpellCheckServiceTests(TestCase):

  def test_get_response_from_service_URL_and_confirm_text_was_received(self):
    word = "apple"

    response_text = get_response(word)

    self.assertTrue(response_text != "")
  
  def test_parse_text_true_and_return_boolean_true(self):
    text = "true"

    self.assertTrue(parse_text(text))

  def test_parse_text_false_and_return_boolean_false(self):
    text = "false"

    self.assertFalse(parse_text(text))

  def test_parse_text_something_else_and_return_value_error(self):
    text = "something else"

    self.assertRaisesRegex(ValueError, "Input could not be parsed", parse_text, text)

  def test_is_spelling_correct_should_take_a_word_and_returns_true_for_word_right(self):
    word = "right"

    with mock.patch("spell_check_service.get_response") as mock_get_response:
      mock_get_response.return_value = "true"
      
      self.assertTrue(is_spelling_correct(word))

  def test_is_spelling_correct_should_take_a_word_and_returns_false_for_word_rigth(self):
    word = "rigth"

    with mock.patch("spell_check_service.get_response") as mock_get_response:
      mock_get_response.return_value = "false"
      
      self.assertFalse(is_spelling_correct(word))

  def test_is_spelling_correct_should_take_a_word_and_returns_false_for_word_haha(self):
    word = "haha"

    with mock.patch("spell_check_service.get_response") as mock_get_response:
      mock_get_response.return_value = "false"

      self.assertFalse(is_spelling_correct(word))

  def test_is_spelling_correct_handles_exeption_from_get_response_properly(self):
    word = "get_response exception"

    with mock.patch("spell_check_service.get_response") as mock_get_response:
      mock_get_response.side_effect = Exception("Network error")
      
      self.assertRaisesRegex(Exception, "Network error", is_spelling_correct, word)

  def test_is_spelling_correct_integration_takes_word_correct_and_returns_boolean_true(self):
    word = "correct"

    self.assertTrue(is_spelling_correct(word))
  
  def test_is_spelling_correct_integration_takes_word_corect_and_returns_boolean_false(self):
    word = "corect"

    self.assertFalse(is_spelling_correct(word))
