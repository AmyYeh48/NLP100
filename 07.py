#!/usr/bin/env python
# -*- coding: utf-8 -*-


x = 12
y = "気温"
z = 22.4


def printSent(x, y, z):
    return '{}時の{}は{}'.format(x, y, z)


if __name__ == '__main__':
    print printSent(x, y, z)
    while True:
        print '「x時のyはz」'
        x = raw_input('>> x : ')
        y = raw_input('>> y : ')
        z = raw_input('>> z : ')
        print printSent(x, y, z)
        print
