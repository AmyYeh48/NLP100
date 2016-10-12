#!/usr/bin/env python
# -*- coding : utf-8 -*-
query = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."


def generate_new(input_str):
    result = ''
    num = set([1, 5, 6, 7, 8, 9, 15, 16, 19])
    for (index, word) in enumerate(input_str.strip().split()):
        if index+1 in num:
            result += word[0]
        else:
            result += word[:2]
    return result

if __name__ == '__main__':
    print generate_new(query)
