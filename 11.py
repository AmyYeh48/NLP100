#!/usr/bin/env python
# -*- coding: utf-8 -*-
import fileinput


for line in fileinput.input():
    print line.strip().replace('\t', ' ')


# Linux Command

# sed -e s/'origin'/'replaced'/g filename
# sed -e s/$'\t'/' '/g hightemp.txt

# tr 'origin' 'replaced'
# cat hightemp.txt | tr '\t' ' '

# expand -t space_count filename
# expand -t 1 hightemp.txt
