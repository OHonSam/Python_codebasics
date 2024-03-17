import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

print(nltk.data.path)
nltk.download('punkt')

# Example text
text = "NLTK is a Python package for natural language processing."

# Tokenize by word
words = word_tokenize(text)
print("Words:", words)

# Tokenize by sentence
sentences = sent_tokenize(text)
print("Sentences:", sentences)
