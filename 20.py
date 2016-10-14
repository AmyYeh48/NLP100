#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import fileinput
import sys


def extract_json(filename):
    for line in fileinput.input(filename):
        article = json.loads(line)
        if article['title'] == u'イギリス':
            return article['text'].encode('utf-8')
    return ""


if __name__ == '__main__':
    print extract_json(sys.argv[1])


# Linux Command
# python 20.py jawiki-country.json > UK.txt
