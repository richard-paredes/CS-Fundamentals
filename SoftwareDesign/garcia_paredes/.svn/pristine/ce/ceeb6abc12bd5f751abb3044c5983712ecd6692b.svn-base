import os
import requests
import sys
sys.path.append(os.path.dirname(__file__).replace("app", ""))

from click import command, option, Path, echo, style, prompt
from click.exceptions import Abort
from spell_check_service import is_spelling_correct
from word_guess import pick_a_random_word, scramble_word, calculate_points_from_guess, cache


def prompt_guess_until_correct(chosen_word, scrambled_word):
  user_guess = ""
  while user_guess != chosen_word:
    echo(style(f"\"{scrambled_word}\"", fg="magenta", bold=True))
    user_guess = prompt("Enter your guess")
    try:
      score = calculate_points_from_guess(chosen_word, user_guess, is_spelling_correct)
    except requests.exceptions.ConnectionError as error:
      raise error
    echo(style(f"Score: {score}\n", fg="blue"))

def play_game_loop(words):
  should_play_game = True

  while should_play_game:
    chosen_word = pick_a_random_word(words)
    cache(chosen_word)
    scrambled_word = scramble_word(chosen_word)
    prompt_guess_until_correct(chosen_word, scrambled_word)
    echo(style("Congratulations! You guessed the word.", fg="green", bold=True))
    should_play_game = prompt("Want to play again? [y/n]").lower() == "y"
    echo()
  
  echo("Exiting. Let's play again later!")

@command()
@option('--input_file',
        type=Path(exists=True),
        required=True,
        help="Path to sample input file.")
def main(input_file):
  try:
    with open(input_file, "r") as file:
      words = list(filter(None, file.read().splitlines()))
    play_game_loop(words)
  except Abort:
    pass
  except Exception as exception:
    echo(style(f"\nError! {str(exception)}", fg="red"))


if __name__ == '__main__':
  main()
