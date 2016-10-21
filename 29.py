#!/usr/bin/env python
# -*- coding: utf-8 -*-
import fileinput
import re
from collections import defaultdict
import requests


api_url = "https://en.wikipedia.org/w/api.php"


def search(keyword, target_dict):
    for k, v in target_dict.items():
        if type(v) == list:
            for sub_kv in v:
                search(keyword, sub_kv)
        elif type(v) == dict:
            search(keyword, v)
        else:
            if k == keyword:
                print v


def remove_markup(inputstr):
    inputstr = re.sub(r"'{2,5}", "", inputstr)
    inputstr = re.sub(r"\[{2}([^|\]]+?\|)*(.+?)\]{2}", r"\2", inputstr)
    inputstr = re.sub(r"\[(.*?)\]", "", inputstr)
    inputstr = re.sub(r"<.*?>", "", inputstr)
    return inputstr


res = defaultdict()
for line in fileinput.input():
    template = re.search("^(.*?)\s=\s(.*)", line.strip(), re.S)
    if template is not None:
        res[template.group(1)] = remove_markup(template.group(2))


para = '?action={}&titles=File:{}&prop={}&format={}&iiprop={}'.format(
        "query", res["|国旗画像"], "imageinfo", "json", "url")
api_url += para
result = requests.get(api_url).json()
search('url', result)
