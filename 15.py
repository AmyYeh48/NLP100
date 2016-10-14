#!/usr/bin/env python
# -*- coding : utf-8 -*-
import sys


with open(sys.argv[1], 'r') as f:
    for line in f.readlines()[-int(sys.argv[2]):]:
            print line.strip()


# Linux Command
# tail -number_of_lines hightemp.txt
# tail -10 hightemp.txt
