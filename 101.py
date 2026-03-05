# Example: Basic NLTK usage for text preprocessing

import os
import ssl
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Ensure required NLTK data is available; if missing, download to local folder.
NLTK_DATA_DIR = os.path.join(os.path.dirname(__file__), 'nltk_data')
if NLTK_DATA_DIR not in nltk.data.path:
    nltk.data.path.append(NLTK_DATA_DIR)


def ensure_nltk_data():
    missing = False
    try:
        nltk.data.find('tokenizers/punkt')
    except LookupError:
        missing = True
    try:
        nltk.data.find('tokenizers/punkt_tab/english')
    except LookupError:
        missing = True
    try:
        nltk.data.find('corpora/stopwords')
    except LookupError:
        missing = True

    if not missing:
        return

    try:
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        pass
    else:
        ssl._create_default_https_context = _create_unverified_https_context

    os.makedirs(NLTK_DATA_DIR, exist_ok=True)
    nltk.download('punkt', download_dir=NLTK_DATA_DIR)
    nltk.download('punkt_tab', download_dir=NLTK_DATA_DIR)
    nltk.download('stopwords', download_dir=NLTK_DATA_DIR)


ensure_nltk_data()

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
