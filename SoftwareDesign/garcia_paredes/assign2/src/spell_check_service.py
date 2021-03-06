from requests import get
from urllib.parse import quote

def parse_text(text):
  if text in ["true", "false"]:
    return text == "true"
  raise ValueError("Input could not be parsed")

def get_response(word):
  return get(f"http://agilec.cs.uh.edu/spell?check={quote(word)}").text

def is_spelling_correct(word):
  return parse_text(get_response(word))
  