import os, sys
sys.path.append(os.path.dirname(__file__).replace("app", ""))

from click import Abort, echo, style, prompt
from perfect_number import generate_perfect_numbers_upto

def print_perfect_numbers_upto(number):
  perfect_numbers = generate_perfect_numbers_upto(number)
  echo(f"The perfect numbers between 1 and {number} are: {style(', '.join(map(str, perfect_numbers)), fg='bright_cyan', bold=True)}")

def main():
  should_prompt_user = True

  while should_prompt_user:
    user_number = int(prompt("Please enter a number greater than 0"))

    print_perfect_numbers_upto(user_number)

    should_prompt_user = prompt("Want to continue? [y/n]").lower() == "y"
    echo()
  
  echo("Exiting.")

if __name__ == "__main__":
  try:
    main()
  except Abort:
    pass
  except Exception as exception:
    echo(style(f"\nError! {str(exception)}", fg="bright_red", bold=True))