#!/usr/bin/env python
# -*- coding: utf-8 -*-
import fileinput


if __name__ == '__main__':
    for line in fileinput.input():
        if 'Category' in line:
            print line.strip()


# Linux Command
# python 21.py UK.txt > UK_Category_line.txt
