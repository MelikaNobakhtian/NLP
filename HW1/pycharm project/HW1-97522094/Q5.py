from nltk.tokenize import TreebankWordTokenizer
from nltk.stem import *

english_example_Address = "AlbertEinstein.txt"
file1 = open(english_example_Address, 'r')
english_example = str(file1.read())

persian_example_Address = "Shahnameh.txt"
file1 = open(persian_example_Address, 'r')
persian_example = str(file1.read())

english_short_text_Address = "ShortSampleEnglish.txt"
file1 = open(english_short_text_Address, 'r')
english_short = str(file1.read())

persian_short_text_Address = "ShortSamplePersian.txt"
file1 = open(persian_short_text_Address, 'r')
persian_short = str(file1.read())

tokens = TreebankWordTokenizer().tokenize(english_example)
idx = [2, 10, 18, 19, 21, 22, 42]

porter = PorterStemmer()
choosen_tokens = [tokens[id]for id in idx]
print("*** Original Words ***:")
print(', '.join(choosen_tokens))
print('')

## Porter
porter_result = [porter.stem(tk) for tk in choosen_tokens]
print("** Stemmed with PorterStemmer **:")
print(', '.join(porter_result))
print("")

## Lancaster
lancaster = LancasterStemmer()
lancaster_result = [lancaster.stem(tk) for tk in choosen_tokens]
print("** Stemmed with LancasterStemmer **:")
print(', '.join(lancaster_result))
print("")

## Lemmatize
words = ['waves', 'fishing', 'rocks', 'was', 'corpora', 'better', 'ate', 'broken']
lemmatizer = WordNetLemmatizer()
lemm_result = [lemmatizer.lemmatize(w) for w in words]
print("*** Lemmatize given Words ***:")
print(', '.join(lemm_result))
print("")
print("*** Lemmatize with Type ***:")
print(f'word : fishing, lemm : {lemmatizer.lemmatize("fishing", pos="v")}')
print(f'word : was, lemm : {lemmatizer.lemmatize("was", pos="v")}')
print(f'word : better, lemm : {lemmatizer.lemmatize("better", pos="a")}')
print(f'word : ate, lemm : {lemmatizer.lemmatize("ate", pos="v")}')
print(f'word : broken, lemm : {lemmatizer.lemmatize("broken", pos="v")}')
