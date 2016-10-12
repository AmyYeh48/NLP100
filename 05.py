#!/usr/bin/env python
# -*- coding: utf-8 -*-
query = "I am an NLPer"


def generate_ngram(sentence, length):
    sentence = sentence.strip().split(' ')
    return zip(*[sentence[i:] for i in range(length)])

if __name__ == '__main__':
    res = generate_ngram(query, 2)
    for bigram in res:
        print ' '.join(bigram)
