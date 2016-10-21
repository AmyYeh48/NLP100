#!/usr/bin/env python
# -*- coding: utf-8 -*-
import fileinput
import re
from collections import defaultdict


res = defaultdict()
# |テンプレート名 = テンプレート内容
for line in fileinput.input():
    template = re.search("^(.*?)\s=\s(.*)", line.strip(), re.S)
    if template is not None:
        res[template.group(1)] = re.sub(r"'{2,5}", "", template.group(2))

for (k, v) in sorted(res.items(), key=lambda x: x[0]):
    print '{}\t{}'.format(k, v)
