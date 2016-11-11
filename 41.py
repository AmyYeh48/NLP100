#!/usr/bin/env python
# -*- coding: utf-8 -*-
import fileinput
from collections import defaultdict

# 係り受け dependency
class Morph():
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def print_data(self):
        return '{}\t{},{},{}'.format(self.surface, self.base, self.pos, self.pos1)

# * 9 -1D 0/2 0.000000
# 思わ    動詞,自立,*,*,五段・ワ行促音便,未然形,思う,オモワ,オモワ
# なかっ  助動詞,*,*,*,特殊・ナイ,連用タ接続,ない,ナカッ,ナカッ
# た      助動詞,*,*,*,特殊・タ,基本形,た,タ,タ
# 。      記号,句点,*,*,*,*,。,。,。
# * 文節番号 係り先番号(dis) 主辞と機能語の位置 係関係のスコア
class chunk():
    def __init__(self):
        self.morphs = []
        self.dst = -1
        self.srcs = []


def readData(fileName):
    all_data = defaultdict(lambda: defaultdict(lambda: chunk))
    sentence_num = 0
    bunsetsu_num = 0
    for index, line in enumerate(fileinput.input(fileName)):
        line = line.strip().split()
        if len(line) != 0:
            if line[0] == "EOS":
                for i in all_data[sentence_num]:
                    if all_data[sentence_num][i].dst != -1:
                        all_data[sentence_num][all_data[sentence_num][i].dst].srcs.append(i)
                sentence_num += 1
            elif line[0] == "*":
                bunsetsu_num, dst, src = int(line[1]), int(line[2][:-1]), line[3]
                all_data[sentence_num][bunsetsu_num] = chunk()
                all_data[sentence_num][bunsetsu_num].dst = dst
            else:
                surface = line[0]
                info = line[1].split(',')
                base, pos, pos1 = info[6], info[0], info[1]
                morph = Morph(surface, base, pos, pos1)
                all_data[sentence_num][bunsetsu_num].morphs.append(morph)
    return all_data


if __name__ == '__main__':
    input_data = readData('neko.txt.cabocha')
    res = ""
    for bunsetsu_num in input_data[7]:
        res += "文節 No. " + str(bunsetsu_num) + " 「"
        for morph in input_data[7][bunsetsu_num].morphs:
                res += morph.surface
        res += "」かかり先文節番号" + str(input_data[7][bunsetsu_num].dst) + "\n"
    print res
