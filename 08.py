#!/usr/bin/env python
# -*- coding: utf-8 -*-
query = 'This is a cipher message.'


def cipher(sent):
    return ''.join([chr(219-ord(char)) if char.islower() else char for char in sent])


if __name__ == '__main__':
    print cipher(query)
