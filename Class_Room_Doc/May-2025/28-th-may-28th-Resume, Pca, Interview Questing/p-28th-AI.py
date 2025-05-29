import os
import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')

text = "Hello, I am using NLTK on Mac!"
print(word_tokenize(text))
