#!/usr/bin/env python
# -*- coding: utf-8 -*-
import fileinput

res_set = set()
for line in fileinput.input():
    line = line.split('\t')
    res_set.add(line[0])

for res in res_set:
    print res


# Linux Command
# cat hightemp.txt | cut -f 1 | sort | uniq
