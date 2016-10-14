#!/usr/bin/env python
# -*- coding: utf-8 -*-
query = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."


def count_alphabet(input_str):
    return [len(word.rstrip(',.')) for word in input_str.strip().split(' ')]

if __name__ == '__main__':
    print count_alphabet(query)
