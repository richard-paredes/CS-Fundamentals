from itertools import groupby

def lowercase(text):
  return text.lower()

def uppercase(text):
  return text.upper()

def stupid_remover(text):
  return text.replace("stupid", "s*****")

def duplicate_remover(text):
  return ' '.join([duplicates[0] for duplicates in groupby(text.split(' '))])