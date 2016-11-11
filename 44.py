#!/usr/bin/env python
# -*- coding: utf-8 -*-
import fileinput
from collections import defaultdict
import pydotplus

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


def pair_chunk(sentence):
    pair = []
    for bunsetsu_num in sentence:
        if sentence[bunsetsu_num].dst != -1:
            temp1 = [morph for morph in sentence[bunsetsu_num].morphs if morph.pos != '記号' ]
            temp2 = [morph for morph in sentence[sentence[bunsetsu_num].dst].morphs if morph.pos != '記号' ]
            pair.append((temp1, temp2))
    return pair


def is_NV(chunks_pair):
    has_N = "名詞" in [morph.pos for morph in chunks_pair[0]]
    has_V = "動詞" in [morph.pos for morph in chunks_pair[1]]
    return has_N and has_V


def sentence_to_dot(index, sentence):
    head = "digraph sentence{} ".format(index)
    body_head = "{ graph [rankdir = LR]; "
    temp1 = ""
    temp2 = ""
    body_list = []
    for chunk_pair in sentence:
        temp1 = ''.join([ morph.surface for morph in chunk_pair[0]])
        temp2 = ''.join([ morph.surface for morph in chunk_pair[1]])
        body_list.append('"{}"->"{}"; '.format(temp1, temp2))
    return head + body_head + ''.join(body_list) + '}'


def sentences_to_dots(sentences):
    dots = []
    for index, sentence in enumerate(sentences):
        dots.append(sentence_to_dot(index, sentence))
    return dots


def save_graph(dot, file_name):
    g = pydotplus.graph_from_dot_data(dot)
    g.write_jpeg(file_name, prog='dot')


if __name__ == '__main__':
    input_data = readData('neko.txt.cabocha')
    pair_sentences = []
    res_NVs = []
    for sentence_num in input_data:
        pair = pair_chunk(input_data[sentence_num])
        pair_sentences.append(pair)
    dots = sentences_to_dots(pair_sentences)
    save_graph(dots[48], 'graph{}.jpg'.format(48))
