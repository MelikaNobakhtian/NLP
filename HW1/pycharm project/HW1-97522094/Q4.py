from nltk.tokenize import TreebankWordTokenizer, RegexpTokenizer, WhitespaceTokenizer, WordPunctTokenizer
import re

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

## Treebank Word Tokenizer

tt = TreebankWordTokenizer().tokenize(english_example)
print(f'** Token count in AlbertEinstein.txt with Treebankwordtokenizer : {len(tt)}')
print(f'** Token types in AlbertEinstein.txt with Treebankwordtokenizer : {", ".join(list(set(tt)))}')
print("")

tt = TreebankWordTokenizer().tokenize(persian_example)
print(f'** Token count in Shahnameh.txt with Treebankwordtokenizer : {len(tt)}')
print(f'** Token types in Shahnameh.txt with Treebankwordtokenizer : {", ".join(list(set(tt)))}')
print("")

tt = TreebankWordTokenizer().tokenize(english_short)
print(f'** Token count in ShortSampleEnglish.txt with Treebankwordtokenizer : {len(tt)}')
print(f'** Token types in ShortSampleEnglish.txt with Treebankwordtokenizer : {", ".join(list(set(tt)))}')
print("")

tt = TreebankWordTokenizer().tokenize(persian_short)
print(f'** Token count in ShortSamplePersian.txt with Treebankwordtokenizer : {len(tt)}')
print(f'** Token types in ShortSamplePersian.txt with Treebankwordtokenizer : {", ".join(list(set(tt)))}')
print("")

## RegexpTokenizer
regexp = RegexpTokenizer('[0-9]+').tokenize(english_example)
print(f'AlbertEinstein.txt numbers with Regexp : {", ".join(regexp)}')
print("")

regexp = RegexpTokenizer('\w+').tokenize(english_short)
print(f'ShortSampleEnglish.txt tokens with Regexp : {", ".join(regexp)}')
print("")

regexp = RegexpTokenizer('[a-zA-Z]+').tokenize(english_short)
print(f'ShortSampleEnglish.txt words with Regexp : {", ".join(regexp)}')
print("")

regexp = RegexpTokenizer('\w+').tokenize(persian_short)
print(f'ShortSamplePersian.txt tokens with Regexp : {", ".join(regexp)}')
print("")


## WhiteSpace Tokenizer
ws = WhitespaceTokenizer().tokenize(english_short)
print(f'ShortSampleEnglish.txt words with WhiteSpaceTokenizer : {", ".join(ws)}')
print("")

tokenizer = RegexpTokenizer('\s+', gaps=True).tokenize(english_short)
print(f'ShortSampleEnglish.txt words with RegexpTokenizer like WhiteSpaceTokenizer : {", ".join(tokenizer)}')
print("")

## WordPunctTokenizer
wpunct = WordPunctTokenizer().tokenize(english_short)
print(f'ShortSampleEnglish.txt words with WordPunctTokenizer : {", ".join(wpunct)}')
print("")










