#!/usr/bin/env python
# -*- coding: utf-8 -*-
query1 = u'パトカー'
query2 = u'タクシー'


def merge(input_str1, input_str2):
    return ''.join([''.join(pair) for pair in zip(input_str1, input_str2)])

if __name__ == '__main__':
    print merge(query1, query2)
