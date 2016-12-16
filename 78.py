#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Reference : https://www.codementor.io/python/tutorial/data-science-python-r-sentiment-classification-machine-learning
import fileinput
import re
from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import stopwords
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report


stopwords_list = list(set(stopwords.words('english')))
stemmer = SnowballStemmer("english", ignore_stopwords=True)
sentence_df = pd.DataFrame()


def checkstopwords(word):
    return word in stopwords_list


def getFeature(sentence):
    result = []
    label, sent = sentence[:2], re.sub("[^a-zA-Z]", " ", sentence[3:]).split(' ')
    for word in sent:
        if not checkstopwords(word) and word != '':
            try:
                stemmered = stemmer.stem(word)
                if stemmered != '':
                    result.append(stemmered)
            except:
                continue
    return (label, ' '.join(list(set(result))))


def setDataFrame(fileName):
    temp_sentence_df = pd.DataFrame()
    for line in fileinput.input(fileName):
        label_feature = getFeature(line.strip())
        label, feature = label_feature[0], label_feature[1]
        if label == '+1':
            label = 1
        else:
            label = 0
        temp_sentence_df = temp_sentence_df.append(pd.DataFrame([[label, feature]]))
    temp_sentence_df.columns = ["Sentiment", "Text"]
    temp_sentence_df.index = range(len(temp_sentence_df))
    return temp_sentence_df


def tokenize(text):
    return re.sub("[^a-zA-Z]", " ", text).split()


def getVectorizer(sentence_df):
    words_list = []
    for sentence in sentence_df.Text:
        for word in sentence.split():
            words_list.append(word)
    len(set(words_list))
    vectorizer = CountVectorizer(
        analyzer='word',
        tokenizer=tokenize,
        lowercase=True,
        stop_words='english',
        max_features=int(len(set(words_list))*0.5)
    )
    return vectorizer


def crossValidation(start, end, corpus_data_features_nd, sentence_df):
    x_train_index = [i for i in range(0, start)] + [i for i in range(end+1, len(corpus_data_features_nd))]
    X_train = corpus_data_features_nd[x_train_index]
    X_test = corpus_data_features_nd[start:end]
    y_train = pd.concat([sentence_df.Sentiment[0:start], sentence_df.Sentiment[end+1:len(corpus_data_features_nd)]])
    y_test = sentence_df.Sentiment[start:end]
    log_model = LogisticRegression()
    log_model = log_model.fit(X=X_train, y=y_train)
    y_pred = log_model.predict(X_test)
    print(classification_report(y_test, y_pred))


if __name__ == '__main__':
    # sentence_df = setDataFrame('sentiment.txt')
    # print len(sentence_df)
    # vectorizer = getVectorizer(sentence_df)
    # corpus_data_features = vectorizer.fit_transform(sentence_df.Text.tolist())
    # corpus_data_features_nd = corpus_data_features.toarray()
    # crossValidation(0, 2132, corpus_data_features_nd, sentence_df)
    # crossValidation(2133, 4265, corpus_data_features_nd, sentence_df)
    # crossValidation(4266, 6398, corpus_data_features_nd, sentence_df)
    # crossValidation(6399, 8531, corpus_data_features_nd, sentence_df)
    # crossValidation(8532, 10662, corpus_data_features_nd, sentence_df)

    P = 0.0
    R = 0.0
    F = 0.0
    S = 0.0
    for line in fileinput.input('res.txt'):
        line = line.strip()
        if 'avg / total' in line:
            print line.split('     ')
            _, precision, recall, f1score, support = line.split('     ')
            P += float(precision)
            R += float(recall)
            F += float(f1score)
            S += float(support)
    print '\tprecision\trecall\tf1-score\tsupport'
    print 'Average\t{}\t{}\t{}\t{}'.format(P/5, R/5, F/5, S/5)
