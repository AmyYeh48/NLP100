#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.externals import joblib


if __name__ == '__main__':
    log_model = joblib.load('log_model.pkl')
    coefList = []
    for index, coef in enumerate(log_model.coef_.tolist()[0]):
        coefList.append((index, coef))
    coefList = sorted(coefList, key=lambda x: x[1], reverse=True)
    print 'Top 10'
    print coefList[:10]
    print 'Last 10'
    print coefList[-10:]
