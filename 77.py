#!/usr/bin/env python
# -*- coding: utf-8 -*-
import fileinput


def getAccuracy(ansList, predictList):
    amount = len(ansList)
    correct = 0.0
    for item in zip(ansList, predictList):
        if item == ('1', '1') or item == ('0', '1'):
            correct += 1
        else:
            continue
    return correct/amount


def getPrecision(ansList, predictList, tag):
    TP = 0.0
    FP = 0.0
    TP_item = ('1', '1')
    FP_item = ('0', '1')

    if tag == 'negitive':
        TP_item = ('0', '0')
        FP_item = ('1', '0')

    for item in zip(ansList, predictList):
        if item == TP_item:
            TP += 1
        elif item == FP_item:
            FP += 1
        else:
            continue
    return TP/(TP+FP)


def getRecall(ansList, predictList, tag):
    TP = 0.0
    FN = 0.0
    TP_item = ('1', '1')
    FN_item = ('1', '0')

    if tag == 'negitive':
        TP_item = ('0', '0')
        FN_item = ('0', '1')

    for item in zip(ansList, predictList):
        if item == TP_item:
            TP += 1
        elif item == FN_item:
            FN += 1
        else:
            continue
    return TP/(TP+FN)


def getF1(precision, recall):
    return 2*precision/(precision+recall)

ansList = []
predictList = []
for line in fileinput.input():
    ans, predict, prob = line.strip().split('\t')
    ansList.append(ans)
    predictList.append(predict)


precision_p = getPrecision(ansList, predictList, 'positive')
recall_p = getRecall(ansList, predictList, 'positive')
precision_n = getPrecision(ansList, predictList, 'negitive')
recall_n = getRecall(ansList, predictList, 'negitive')
print 'accuracy : {}'.format(getAccuracy(ansList, predictList))
print
print 'Positive'
print '----------------------------------'
print 'precision : {}'.format(precision_p)
print 'recall : {}'.format(recall_p)
print 'F1 measure : {}'.format(getF1(precision_p, recall_p))
print
print 'Negitive'
print '----------------------------------'
print 'precision : {}'.format(precision_n)
print 'recall : {}'.format(recall_n)
print 'F1 measure : {}'.format(getF1(precision_n, recall_n))
