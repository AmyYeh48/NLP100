#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import shuffle


sent = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."


def shuffled(word):
    new_word = [char for char in word[1:-1]]
    shuffle(new_word)
    return word[0]+''.join([char for char in new_word])+word[-1]


def typoglycemia(sent):
    sent = sent.strip().split(' ')
    return ' '.join([shuffled(word) if len(word) > 4 else word for word in sent])


if __name__ == '__main__':
    print typoglycemia(sent)
