#!/usr/bin/env python
# -*- coding: utf-8 -*-
import fileinput
import re
from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import stopwords
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import classification_report
from sklearn.externals import joblib


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


if __name__ == '__main__':
    sentence_df = setDataFrame('sentiment.txt')
    vectorizer = getVectorizer(sentence_df)
    corpus_data_features = vectorizer.fit_transform(sentence_df.Text.tolist())
    corpus_data_features_nd = corpus_data_features.toarray()
    vocab = vectorizer.get_feature_names()
    log_model = joblib.load('log_model.pkl')

    testData = corpus_data_features_nd[0:len(sentence_df)]
    probList = []
    for item in (log_model.predict_proba(testData)).tolist():
        probList.append(item[1])

    predictList = []
    for item in (log_model.predict(testData)).tolist():
        predictList.append(item)

    ansList = sentence_df.Sentiment.tolist()

    for ans, pred, prob in zip(ansList, predictList, probList):
        print("\t".join([str(ans), str(pred), str(prob)]))
