import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
nltk.download('punkt')

print("**** Use NLTK to See Result of word tokenize abd sent tokenize on given file ****")
print("")
file_address = input("Enter File Address: ")
file1 = open(file_address, 'r')
print("Main File Text:")
text = str(file1.read())
print(text)
print(" ")
words = word_tokenize(text)
print("***** Tokenized words with word_tokenize *****")
for word in words:
    print(word)
print("")
print("****** Sentences with sent_tokenize ******")
sents = sent_tokenize(text)
for sent in sents:
    print(sent)
    print("///")