# -*- coding: utf-8 -*-
# from prettytable import PrettyTable

CABOCHA_FILE = './output/neko.txt.cabocha'


class Morph():
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1


class Chunk(object):
    def __init__(self):
        self.morphs = []
        self.dst = 0
        self.srcs = []


def get_lines(cabocha_filename):
    """

    :cabocha_filename: CaboCha File
    :returns: list

    """
    with open(cabocha_filename) as f:
        lines = f.readlines()
        line_list = []
        lines_list = []
        for line in lines[:300]:
            temp_list = line.split()
            if temp_list[0] == '*':
                temp_list[2] = temp_list[2].strip('D')
            for l in temp_list:
                line_list += l.split(",")
            lines_list.append(line_list)
            line_list = []
    return lines_list


# def get_morphs(lines):
#     # 文章全部
#     sentences = []
#     # 一文
#     sentence = []
#     for line in lines:
#         if line[0] == '*':
#             pass
#         elif line[0] == 'EOS' or line[2] == "句点":
#             # sentence.append(line)
#             sentences.append(sentence)
#             sentence = []
#         else:
#             sentence.append(line)
#     return sentences


def get_chunks(filename):
    lines = get_lines(filename)
    chunks = []
    for line in lines:
        if line[0] == '*':
            if line[1] == '0':
                chunks.append(Chunk())
                chunks[len(chunks)-1].dst = line[2]
            chunks[len(chunks)-1].srcs.append(int(line[1]))
        elif line[0] == 'EOS' or line[2] == "句点":
            pass
        else:
            chunks[len(chunks)-1].morphs.append(
                    Morph(
                        surface=line[0],
                        base=line[7],
                        pos=line[1],
                        pos1=line[2])
                    )
    return chunks


def main():
    # lines = get_lines(CABOCHA_FILE)
    # sentences = get_morphs(lines)
    chunks = get_chunks(CABOCHA_FILE)
    for chunk in chunks:
        print(chunk.dst,
              chunk.srcs,
              " ".join(morph.surface for morph in chunk.morphs)
              )

    # morph_sentence = []
    # morph_sentences = []

    # for sentence in sentences:
    #     for word in sentence:
    #         morph = Morph(
    #             surface=word[0],
    #             base=word[7],
    #             pos=word[1],
    #             pos1=word[2])
    #         morph_sentence.append(morph)
    #     morph_sentences.append(morph_sentence)
    #     morph_sentence = []

    # # 表示
    # t = PrettyTable(['surface', 'base', 'pos', 'pos1'])
    # for m in morph_sentences[0]:
    #     t.add_row([m.surface, m.base, m.pos, m.pos1])
    # for m in morph_sentences[3]:
    #     t.add_row([m.surface, m.base, m.pos, m.pos1])
    # print(t)


if __name__ == "__main__":
    main()
