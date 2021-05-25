import unittest
from unittest import mock, TestCase
from functools import partial
import requests
from word_guess import scramble_word, calculate_points_from_guess as calculate_points, pick_a_random_word, cache, clear_cache

calculate_points_from_guess =\
  partial(calculate_points, is_spelling_correct = lambda word: True)

def throw(exception):
  raise exception

class WordGuessTests(TestCase):

  def test_canary(self):
    self.assertTrue(True)
  
  def setUp(self):
    clear_cache()

  def test_scramble_word_apple(self):
    word = "apple"

    scrambled_word = scramble_word(word)

    self.assertNotEquals(word, scrambled_word)

  def test_scramble_word_matter(self):
    word = "matter"

    scrambled_word = scramble_word(word)

    self.assertNotEquals(word, scrambled_word)

  def test_scramble_word_apple_twice_and_expect_different_results(self):
    word = "apple"

    first_scrambled_word = scramble_word(word)
    second_scrambled_word = scramble_word(first_scrambled_word)

    self.assertNotEquals(second_scrambled_word, first_scrambled_word)

  def test_scramble_an_empty_string_and_returns_scramble_without_space(self):
    word = "    "

    scrambled_word = scramble_word(word)

    self.assertFalse(scrambled_word.isspace())

  def test_scramble_word_with_space_in_the_beginning_and_returns_scramble_without_space(self):
    word = " scramble"

    scrambled_word = scramble_word(word)

    self.assertFalse(scrambled_word.isspace())

  def test_scramble_word_with_space_at_end_returns_scramble_without_space(self):
    word = "scramble "

    scrambled_word = scramble_word(word)

    self.assertFalse(scrambled_word.isspace())

  def test_scramble_word_with_space_in_middle_returns_scramble_with_space(self):
    word = "ice cream"

    scrambled_word = scramble_word(word)

    self.assertEquals(1, scrambled_word.count(" "))

  def test_scramble_word_with_mixed_casing_returns_scramble_with_lowercase(self):
    word = "PoLyMoRpHiSm"

    scrambled_word = scramble_word(word)

    self.assertTrue(scrambled_word.islower())

  def test_scramble_word_returns_scramble_with_same_characters(self):
    word = "scramble"

    scrambled_word = scramble_word(word)

    self.assertTrue(sorted(word) == sorted(scrambled_word))

  def test_calculate_points_from_guess_for_monk_with_original_word_monkey_and_returns_7(self):
    word = "monkey"
    guess = "monk"
    
    self.assertEquals(7, calculate_points_from_guess(word, guess))

  def test_calculate_points_from_guess_for_pine_with_original_word_pineapple_and_returns_6(self):
    word = "pineapple"
    guess = "pine"

    self.assertEquals(6, calculate_points_from_guess(word, guess))

  def test_calculate_points_from_guess_for_mop_with_original_word_monkey_returns_0(self):
    word = "monkey"
    guess = "mop"

    self.assertEquals(0, calculate_points_from_guess(word, guess))

  def test_calculate_points_from_guess_for_pink_with_original_word_pineapple_returns_0(self):
    word = "pineapple"
    guess = "pink"

    self.assertEquals(0, calculate_points_from_guess(word, guess))

  def test_calculate_points_for_guess_with_right_letters_but_not_in_order_with_original_word_hyena_returns_5(self):
    word = "hyena"
    guess = "nay"

    self.assertEquals(5, calculate_points_from_guess(word, guess))

  def test_calculate_points_for_guess_with_right_letters_but_not_in_order_with_original_word_pineapple_returns_6(self):
    word = "pineapple"
    guess = "peel"

    self.assertEquals(6, calculate_points_from_guess(word, guess))

  def test_calculate_points_from_guess_for_a_with_original_word_apple_returns_1(self):
    word = "apple"
    guess = "a"

    self.assertEquals(1, calculate_points_from_guess(word, guess))

  def test_calculate_points_from_non_continuous_guess_ape_with_original_word_apple_returns_4(self):
    word = "apple"
    guess = "ape"
    
    self.assertEquals(4, calculate_points_from_guess(word, guess))

  def test_calculate_points_from_no_vowel_guess_by_with_original_word_bayou_returns_4(self):
    word = "bayou"
    guess = "by"

    self.assertEquals(4, calculate_points_from_guess(word, guess))

  def test_calculate_points_for_guess_with_letters_not_in_original_word_returns_0(self):
    word = "bayou"
    guess = "bye"

    self.assertEquals(0, calculate_points_from_guess(word, guess))

  def test_calculate_points_for_guess_with_repeated_letters_in_original_word_returns_0(self):
    word = "relate"
    guess = "rear"

    self.assertEquals(0, calculate_points_from_guess(word, guess))

  def test_calculate_points_for_guess_with_incorrect_spelling_and_correct_order(self):
    word = "apple"
    guess = "app"

    is_spelling_correct = lambda word: False
    
    self.assertEquals(0, calculate_points(word, guess, is_spelling_correct))    

  def test_calculate_points_for_guess_with_incorrect_spelling_and_incorrect_order(self):
    word = "apple"
    guess = "ael"

    is_spelling_correct = lambda word: False

    self.assertEquals(0, calculate_points(word, guess, is_spelling_correct))

  def test_calculate_points_for_guess_with_correct_spelling_but_spell_checker_throws_runtime_exception(self):
    word = "monkey"

    guess = "monk"

    is_spelling_correct = lambda word: throw(Exception("Runtime exception while spell checking"))

    self.assertRaisesRegex(Exception, "Runtime exception while spell checking", calculate_points, word, guess, is_spelling_correct)

  def test_pick_a_random_word_returns_random_word_from_list_of_words(self):
    words = ['monkey', 'pineapple']

    self.assertIn(pick_a_random_word(words), words)
  
  def test_pick_a_random_word_returns_different_word_when_called_again(self):
    words = ['monkey', 'pineapple']

    first_word = pick_a_random_word(words)
    cache(first_word)
    
    second_word = pick_a_random_word(words)
    cache(second_word)
    
    self.assertNotEquals(first_word, second_word)
  
  def test_pick_a_random_word_from_empty_list_raises_error(self):
    words = []

    self.assertRaises(IndexError, pick_a_random_word, words)

  def test_pick_a_random_word_clears_cache_when_all_words_picked(self):
    words = ["banana", "apple"]
    cache("banana")
    cache("apple")

    pick_a_random_word(words)

    self.assertListEqual([], cache())

