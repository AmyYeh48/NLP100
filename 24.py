#!/usr/bin/env python
# -*- coding: utf-8 -*-
import fileinput
import re


for line in fileinput.input():
    fileName = re.search('(File|ファイル):(.*?)\|', line)
    if fileName is not None:
        print fileName.group(2)


# Linux Command
# python 24.py UK.txt
