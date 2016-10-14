# !/usr/bin/env python
# -*- coding: utf-8 -*-
import fileinput
col1 = []
col2 = []


def writeColumn(col_list, filename):
    with open(filename, 'w') as f:
        [f.writelines(line+'\n') for line in col_list]


for line in fileinput.input():
    line = line.strip().split('\t')
    col1.append(line[0])
    col2.append(line[1])

writeColumn(col1, 'col1.txt')
writeColumn(col2, 'col2.txt')


# Linux Command
# cut -f column_in_file filename
# cut -f 1 hightemp.txt
# cut -f 2 hightemp.txt
