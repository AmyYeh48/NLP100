#!/usr/bin/env python
# -*- coding: utf-8 -*-
import fileinput
import re


# [[Category:イギリス|*]]
for line in fileinput.input():
    category = re.search("^\[\[Category:(.*?)(|\|.*)\]\]$", line)
    if category is not None:
        print category.group(1)


# Linux Command
# python 22.py UK_Category_line.txt
