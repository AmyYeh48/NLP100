#!/usr/bin/env python
# -*- coding: utf-8 -*-
import fileinput
from collections import Counter


# 表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用型,活用形,原形,読み,発音
def meCab_transfer(mecabfile):
    sents = []
    sent = []
    for line in fileinput.input(mecabfile):
        if 'EOS' in line:
            if len(sent) > 0:
                sents.append(sent)
            sent = []
        else:
            surface, features = line.strip().split('\t')
            features = features.split(',')
            sentDict = {
                'surface': surface,
                'base': features[6],
                'pos': features[0],
                'pos1': features[1]
            }
            sent.append(sentDict)
    return sents


# [{'base': '少し', 'pos': '副詞', 'surface': '少し', 'pos1': '助詞類接続'},
def wordCount(sents):
    res = []
    for sent in sents:
        for word in sent:
            res.append(word['surface'])
    return Counter(res)

if __name__ == '__main__':

    fileName = 'neko.txt.mecab'
    sents_dict = meCab_transfer(fileName)
    word_counts = wordCount(sents_dict)
    for word, count in word_counts.most_common():
        print '{}\t{}'.format(word, count)
