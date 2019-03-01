from transform import *
from matrix import *
from draw import *

def argify(line):
    args = line.split()
    for i in range(len(args)):
        args[i] = int(args[i])
    return args

def parse(fname, edge, orders, screen, color):
    transform = {
        "line": add_edge,
        "scale": dilate,
        "move": translate,
        "rotate": rotate
    }
    control = {
        "ident": lambda: ident(orders),
        "apply": lambda: matrix_mult(orders,edge)
    }
    f = open(fname, 'r')
    for line in f:
        if line in control:
            control[line]
        elif line in transform:
            args = f.next()
            transform[line](orders,argify(line))
        elif line == "save":
            name = f.next()
            save_extension(name)
        elif line == "display":
            draw_lines(edge,screen,color)
            display(screen)
    f.close()
