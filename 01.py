#!/usr/bin/env python
# -*- coding: utf-8 -*-
query = u'パタトクカシーー'


def skipwords(input_str):
    # [begin:end:step]
    return input_str[1::2]

if __name__ == '__main__':
    print skipwords(query)
