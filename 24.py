#!/usr/bin/env python
# -*- coding: utf-8 -*-
import fileinput
import re


# [[File:Scotland Parliament Holyrood.jpg|thumb|[[スコットランド議会]]議事堂]]
for line in fileinput.input():
    fileName = re.search('(File|ファイル):(.*?)\|', line)
    if fileName is not None:
        print fileName.group(2)


# Linux Command
# python 24.py UK.txt
