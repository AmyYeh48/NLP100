#!/usr/bin/env python
# -*- coding: utf-8 -*-
import fileinput
import re
from collections import defaultdict


# [[記事名]]
# [[記事名|表示文字]]
# [[記事名#節名|表示文字]]
def remove_markup(inputstr):
    inputstr = re.sub(r"'{2,5}", "", inputstr)
    inputstr = re.sub(r"\[{2}([^|\]]+?\|)*(.+?)\]{2}", r"\2", inputstr)
    return inputstr


res = defaultdict()
for line in fileinput.input():
    template = re.search("^(.*?)\s=\s(.*)", line.strip(), re.S)
    if template is not None:
        res[template.group(1)] = remove_markup(template.group(2))

for (k, v) in sorted(res.items(), key=lambda x: x[0]):
    print '{}\t{}'.format(k, v)
