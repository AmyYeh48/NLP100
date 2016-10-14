#!/usr/bin/env python
# -*- coding: utf-8 -*-
import fileinput
import sys

for line in fileinput.input(sys.argv[1]):
        if fileinput.filelineno() <= int(sys.argv[2]):
            print line.strip()
        else:
            break


# Linux Command
# head -number_of_lines hightemp.txt
