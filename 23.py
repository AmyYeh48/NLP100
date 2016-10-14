#!/usr/bin/env python
# -*- coding: utf-8 -*-
import fileinput
import re


# ===音楽===
for line in fileinput.input():
    section = re.search('^(=+)\s*(.*?)\s*(=+)', line)
    if section is not None:
        print section.group(2), len(section.group(1)) - 1
