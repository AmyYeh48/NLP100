#!/usr/bin/env python
# -*- coding: utf-8 -*-
query = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."


def sort_by_alphabet(input_str):
    return sorted(input_str.strip().lower().split(' '))

if __name__ == '__main__':
    print sort_by_alphabet(query)
