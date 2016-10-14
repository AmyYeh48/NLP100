#!/usr/bin/env python
# -*- coding: utf-8 -*-
query1 = "paraparaparadise"
query2 = "paragraph"


def generate_ngram(word, length):
    word = [alp for alp in word]
    return zip(*[word[i:] for i in range(length)])


if __name__ == '__main__':
    x = set([''.join(bigram) for bigram in generate_ngram(query1, 2)])
    y = set([''.join(bigram) for bigram in generate_ngram(query2, 2)])
    print '{}\t{}'.format('x: ', x)
    print '{}\t{}'.format('y: ', y)
    print '{}\t{}'.format('union', x | y)
    print '{}\t{}'.format('intersection', x & y)
    print '{}\t{}'.format('difference', x-y)
    print '{}\t{}'.format('is \'se\' in x', 'se' in x)
    print '{}\t{}'.format('is \'se\' in y', 'se' in y)
