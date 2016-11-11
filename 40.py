#!/usr/bin/env python
# -*- coding: utf-8 -*-
import fileinput


class Morph():
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def print_data(self):
        return '{}\t{},{},{}'.format(self.surface, self.base, self.pos, self.pos1)


# line = 表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用形,活用型,原形,読み,発音
def readData(fileName):
    sent = []
    sents = []
    for line in fileinput.input(fileName):
        line = line.split()
        if len(line) != 0:
            if line[0] == "EOS":
                sents.append(sent)
                sent = []
            elif line[0] == "*":
                continue
            else:
                surface = line[0]
                info = line[1].split(',')
                base, pos, pos1 = info[6], info[0], info[1]
                morph = Morph(surface, base, pos, pos1)
                sent.append(morph)
    return sents

if __name__ == '__main__':
    input_data = readData('neko.txt.cabocha')
    for sent in input_data[2]:
        print sent.print_data()
