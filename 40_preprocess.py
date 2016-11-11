import CaboCha
import fileinput


def make_analyzed_file(inputFile):
    c = CaboCha.Parser()
    for line in fileinput.input(inputFile):
        tree = c.parse(line.strip())
        print tree.toString(CaboCha.FORMAT_LATTICE)

if __name__ == '__main__':
    make_analyzed_file('neko.txt')
