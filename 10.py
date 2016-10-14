#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys


with open(sys.argv[1], 'r') as f:
    print len(f.readlines())

# Linux Command
# cat hightemp.txt | wc -l
