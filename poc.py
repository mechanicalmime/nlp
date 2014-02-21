# coding: utf-8
from __future__ import division
import nltk, re, pprint

f = open('document.txt')
raw = f.read()

tokens = nltk.word_tokenize(raw)

words = [w.lower() for w in tokens]

vocab = sorted(set(words))

for word in words:
	print word

print len(vocab)
print len(tokens)