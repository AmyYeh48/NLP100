# !/usr/bin/env python
# -*- coding: utf-8 -*-


def merge(col1, col2):
    resList = ['\t'.join(combine) for combine in zip(col1, col2)]
    for res in resList:
        print res


def readfile(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f.readlines()]


if __name__ == '__main__':
    col1 = readfile('col1.txt')
    col2 = readfile('col2.txt')
    merge(col1, col2)


# Linux Command
# paste first_column second_column
# paste col1.txt col2.txt
