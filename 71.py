#!/usr/bin/env python
# -*- coding: utf-8 -*-
from nltk.corpus import stopwords

stopwords_list = list(set(stopwords.words('english')))


def checkstopwords(word):
    return word in stopwords_list


if __name__ == '__main__':
    test = 'he'
    print [checkstopwords(word) for word in test.split(' ')]
