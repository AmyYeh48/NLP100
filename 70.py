#!/usr/bin/env python
# -*- coding: utf-8 -*-
import fileinput
from random import shuffle

posFile = 'rt-polarity.pos'
negFile = 'rt-polarity.neg'


def readnTagData(filename, sign):
    res = []
    for line in fileinput.input(filename):
        res.append('{}{}'.format(sign, line))
    return res


if __name__ == '__main__':
    res = []
    posData = readnTagData(posFile, '+1 ')
    negData = readnTagData(negFile, '-1 ')
    res = posData+negData
    shuffle(res)
    for line in res:
        print line.strip()
