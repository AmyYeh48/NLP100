#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

split_num = int(sys.argv[2])
with open(sys.argv[1], 'r') as f:
    lines = f.readlines()
    if len(lines) % split_num == 0:
        linecounts = len(lines) / split_num
        for i in range(split_num):
            with open('split_%s.txt' % (i+1), 'w') as writer:
                writer.writelines(lines[i*linecounts:(i+1)*linecounts])
    else:
        print 'This file can not be split into %s parts.' % split_num


# Linux Command
# split -l linecounts filename
# split -l 8 hightemp.txt
