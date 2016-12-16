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
from sklearn.externals import joblib
import matplotlib.pyplot as plt

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


def pre_recl(answer_list, predicted_list):
    TP = 0.0 ; FP = 0.0 ; TN = 0.0 ; FN = 0.0
    for ans, pred in zip(answer_list, predicted_list):
        if pred == 1 and ans == 1:
            TP += 1
        elif pred == 1 and ans == 0:
            FP += 1
        elif pred == 0 and ans == 0:
            TN += 1
        elif pred == 0 and ans == 1:
            FN += 1
        else:
            print("Something is wrong.")

    precision = TP / (TP + FP)
    recall = TP / (TP + FN)

    return precision, recall


def prediction(threshold=0.5):
    predicted_list = []
    for i in prob_list:
        if i >= threshold:
            predicted_list.append(1)
        else:
            predicted_list.append(0)

    return predicted_list


def frange(x, y, jump):
    while x < y:
        yield x
        x += jump


def no_79(threshold, answer_list):
    predicted_list = prediction(threshold)
    precision, recall = pre_recl(answer_list, predicted_list)

    return precision, recall


if __name__ == '__main__':
    sentence_df = setDataFrame('sentiment.txt')
    # print sentence_df[0:10]
    vectorizer = getVectorizer(sentence_df)
    corpus_data_features = vectorizer.fit_transform(sentence_df.Text.tolist())
    corpus_data_features_nd = corpus_data_features.toarray()
    vocab = vectorizer.get_feature_names()

    log_model = LogisticRegression()
    log_model = log_model.fit(X=corpus_data_features_nd[0:len(sentence_df)], y=sentence_df.Sentiment)
    prob_list = []
    for item in (log_model.predict_proba(corpus_data_features_nd[0:len(sentence_df)])).tolist():
        prob_list.append(item[1])
    predicted_list = prediction(0.4)
    answer_list = sentence_df.Sentiment.tolist()
    precision, recall = pre_recl(answer_list, predicted_list)
    precision_list = []
    recall_list = []
    for threshold in frange(0.00, 1.00, 0.05):
        precision, recall = no_79(threshold, answer_list)
        precision_list.append(precision)
        recall_list.append(recall)

    plt.plot(precision_list, recall_list)
    plt.title('precision - recall')
    plt.xlabel('precision')
    plt.ylabel('recall')
    plt.show()
