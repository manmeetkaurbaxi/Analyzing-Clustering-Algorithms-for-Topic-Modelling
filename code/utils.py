# This file contains all the functions required to run all the tests on the datasets

# Necessary imports
import nltk
from nltk.stem import WordNetLemmatizer #Used to lemmatize words
from nltk.tokenize import word_tokenize #Used to extract words from documents
import numpy as np
import pandas as pd
import re
from sklearn import datasets 
import gensim
from gensim.utils import simple_preprocess

# ======================================= Pre-processing functions ===================================================
def clean_text(sentence):
    # remove non alphabetic sequences
    pattern = re.compile(r'[^a-z]+')
    sentence = sentence.lower()
    sentence = pattern.sub(' ', sentence).strip()
    sentence = sentence.replace('\n','')
    
    # Tokenize
    word_list = word_tokenize(sentence)
    
    # stop words
    stopwords_list = set(nltk.corpus.stopwords.words('english'))
    
    # remove stop words
    word_list = [word for word in word_list if word not in stopwords_list]
    # remove very small words, length < 3, they don't contribute any useful information
    word_list = [word for word in word_list if len(word) > 3]
        
    # lemmatize
    # lemma = WordNetLemmatizer()
    # word_list = [lemma.lemmatize(word) for word in word_list]
    # list to sentence
    sentence = ' '.join(word_list)
    
    return sentence


def strip_newline(series):
    return [review.replace('\n','') for review in series]

def sent_to_words(sentences):
    for sentence in sentences:
        yield(gensim.utils.simple_preprocess(str(sentence), deacc=True))
        
def remove_stopwords(texts):
    return [[word for word in simple_preprocess(str(doc)) if word not in nltk.corpus.stopwords.words('english')] for doc in texts]