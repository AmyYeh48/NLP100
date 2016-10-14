#!/usr/bin/env python
# -*- coding: utf-8 -*-
import fileinput

data_list = []
for line in fileinput.input():
        data_list.append(tuple(line.strip().split('\t')))
for res in sorted(data_list, key= lambda x: float(x[2]), reverse=True):
    print '\t'.join(res)


# Linux Command
# cat filename | sort -k keyword_column -r(reverse)
# cat hightemp.txt | sort -k 3 -r
