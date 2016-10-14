#!/usr/bin/env python
# -*- coding: utf-8 -*-
import fileinput
from collections import Counter

res = []
for line in fileinput.input():
    res.append(line.strip().split('\t')[0])
for key, counts in Counter(res).most_common():
    print key


# Linux Command
# cat hightemp.txt | cut -f 1 | sort | uniq -c | sort -r | cut -c 6-
