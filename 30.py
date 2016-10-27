#!/usr/bin/env python
# -*- coding: utf-8 -*-
import fileinput


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

if __name__ == '__main__':

    fileName = 'neko.txt.mecab'
    res = meCab_transfer(fileName)

    for sent in res:
        print str(sent).decode("string-escape")
