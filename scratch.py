# import the existing word and sentence tokenizing
# libraries
import nltk
from nltk.tokenize import sent_tokenize,word_tokenize


text = "Natural language processing (NLP) is a field " + \
	"of computer science, artificial intelligence " + \
	"and computational linguistics concerned with " + \
	"the interactions between computers and human " + \
	"(natural) languages, and, in particular, " + \
	"concerned with programming computers to " + \
	"fruitfully process large natural language " + \
	"corpora. Challenges in natural language " + \
	"processing frequently involve natural " + \
	"language understanding, natural language" + \
	"generation frequently from formal, machine" + \
	"-readable logical forms), connecting language " + \
	"and machine perception, managing human-" + \
	"computer dialog systems, or some combination " + \
	"thereof."

print(sent_tokenize(text))
print(word_tokenize(text))

from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
porter = PorterStemmer()
lancaster=LancasterStemmer()
#proide a word to be stemmed
print("Porter Stemmer")
print(porter.stem("patient"))
print(porter.stem("date of service"))
print(porter.stem("place of service"))
print(porter.stem("accident"))
print("Lancaster Stemmer")
print(lancaster.stem("patient"))
print(lancaster.stem("date of service"))
print(lancaster.stem("place of service"))
print(lancaster.stem("accident"))

# define punctuation
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

my_str = text

# To take input from the user
# my_str = input("Enter a string: ")

# remove punctuation from the string
no_punct = ""
for char in my_str:
   if char not in punctuations:
       no_punct = no_punct + char

# display the unpunctuated string
print(no_punct)

import nltk
import re
import numpy as np
import random2
import stringformat
import Corpus
import bs4 as bs
import urllib.request

# execute the text here as :
# text = """ # place text here  ""
dataset = sent_tokenize(no_punct)
for i in range(len(dataset)):
    dataset[i] = dataset[i].lower()
    dataset[i] = re.sub(r'\W', ' ', dataset[i])
    dataset[i] = re.sub(r'\s+', ' ', dataset[i])
print(dataset)

# Creating the Bag of Words model
word2count =[]
for data in dataset:
	words = nltk.word_tokenize(no_punct)
	print(word2count)

def freq_words():
	X = []
	for text in dataset:
		vector = []
		for words in freq_words:
			if words in nltk.word_tokenize(no_punct):
				vector.append(1)
			else:
				vector.append(0)
		X.append(vector)
	X = np.asarray(X)
print(freq_words)

def w2v_tokenize_text(data):
	tokens = []
	for sent in nltk.sent_tokenize(text, language='english'):
		for words in nltk.word_tokenize(sent, language='english'):
			if len(data) < 2:
				continue
			tokens.append(data)
	return tokens
print(w2v_tokenize_text)

tf_idf = {}
def N():
    for i in range(N):
     tokens = text[i]
     counter = Counter(dataset + processed_title[i])
    for token in np.unique(dataset):
        tf = counter[dataset]/words_count
        df = doc_freq(dataset)
        idf = np.log(N/(df+1))
        tf_idf[doc, token] = tf*idf
print(N)

def matching_score(query):
    query_weights = {}
    for key in tf_idf:
        if key[1] in dataset:
            query_weights[key[0]] += tf_idf[key]

# Document Vectorization
def counter():
    counter = counter(dataset)
    words_count = len(dataset)
    query_weights = {}
    for token in np.unique(dataset):
       tf = counter[token]/words_count
       df = doc_freq(dataset)
       idf = math.log((N+1)/(df+1))
print(matching_score)
print(counter)
