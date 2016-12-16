#!/usr/bin/env python
# -*- coding: utf-8 -*-
import fileinput
from nltk.stem.snowball import SnowballStemmer
from nltk.stem.porter import *
from nltk.corpus import stopwords


stopwords_list = list(set(stopwords.words('english')))
stemmer = SnowballStemmer("english", ignore_stopwords=True)
stemmer2 = PorterStemmer()


def checkstopwords(word):
    return word in stopwords_list


def getFeature(sentence):
    result = set()
    label, sent = sentence[:2], sentence[3:].split(' ')
    for word in sent:
        if not checkstopwords(word) and word not in ['.', ',']:
            try:
                result.add(stemmer.stem(word))
            except:
                continue
    return (label, list(result))


if __name__ == '__main__':
    for line in fileinput.input():
        print getFeature(line.strip())
