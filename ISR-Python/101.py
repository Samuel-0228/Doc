# Example: Basic NLTK usage for text preprocessing

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Download required NLTK data files (only needed once)
nltk.download('punkt')
nltk.download('stopwords')

# Sample text
text = "Natural Language Processing with NLTK is powerful and fun!"

# 1. Tokenization
tokens = word_tokenize(text)
print("Tokens:", tokens)

# 2. Remove stopwords
stop_words = set(stopwords.words('english'))
filtered_tokens = [word for word in tokens if word.lower() not in stop_words]
print("Filtered Tokens:", filtered_tokens)

# 3. Stemming
stemmer = PorterStemmer()
stemmed_tokens = [stemmer.stem(word) for word in filtered_tokens]
print("Stemmed Tokens:", stemmed_tokens)
