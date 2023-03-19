import re
import nltk
from nltk.corpus import words

word = input("Word should be normalized:")
char_repeated = re.compile(r'(\w*)(\w)\2(\w*)')

while not word in words.words():
    normal_word = char_repeated.sub(r'\1\2\3', word)
    if normal_word == word:
      break
    word = normal_word

print(f'normal word: {word}')