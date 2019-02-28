from transform import *
from matrix import *
from draw import *

def argify(line):
    line = line.split()
    for i in range(len(line)):
        line[i] = int(line)


def parse(fname, edge, transform, screen, color):
    transform = {
        "line": add_edge,
        "scale": dilate,
        "move": translate,
        "rotate": rotate
    }
    control = {
        "ident": ident,
        "apply": matrix_mult,
        "display": display,
        "save": save
    }
    f = open(fname, 'r')
    for line in f:
        if line in control:
            control[line]
        elif line in transform:
            args = f.next()
