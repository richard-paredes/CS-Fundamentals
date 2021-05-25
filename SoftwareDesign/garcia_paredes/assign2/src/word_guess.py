from collections import Counter
from random import sample, choice

def scramble_word(word):
  scrambled_word = ''.join(sample(word.strip().lower(), len(word.strip())))
  return scrambled_word if scrambled_word != word else scramble_word(word)

def calculate_points_from_guess(word, guess, is_spelling_correct):
  return {
    True: 0, 
    False: sum(map(lambda letter: 1 if letter in "aeiou" else 2, guess))
  } [len(Counter(guess) - Counter(word)) > 0 or not all(is_spelling_correct(s) for s in guess.split())]

def pick_a_random_word(words):
  rand_word = choice(words)
  while len(cache()) < len(words):
    return rand_word if rand_word not in cache() else pick_a_random_word(words)
  clear_cache()
  return rand_word

def cache(word=None,lst=[]): 
  if word is not None: lst.append(word)
  return lst

def clear_cache():
  cache().clear()
  