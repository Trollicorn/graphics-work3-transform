from matrix import *
from math import cos,sin,radians

def translate(matrix,args):
    x = args[0]
    y = args[1]
    z = args[2]
    m = new_matrix()
    ident(new_matrix)
    m[3][0] = x
    m[3][1] = y
    m[3][2] = z
    matrix_mult(m,matrix)

def dilate(matrix,args):
    x = args[0]
    y = args[1]
    z = args[2]
    m = new_matrix()
    ident(new_matrix)
    m[0][0] = x
    m[1][1] = y
    m[2][2] = z
    matrix_mult(m,matrix)

def rotate(matrix,args):
    axis = args[0]
    angle = args[1]
    ax = {
        'x': rotateX,
        'y': rotateY,
        'z': rotateZ
    }
    ax.get(axis)(matrix,angle)

def rotateX(matrix,angle):
    m = new_matrix()
    ident(new_matrix)
    rad = randians(angle)
    m[0][0] = cos(rad)
    m[0][1] = sin(rad)
    m[1][0] = -1 * m[0][1]
    m[1][1] = m[0][0]
    matrix_mult(m,matrix)

def rotateY(matrix,angle):
    m = new_matrix()
    ident(new_matrix)
    rad = randians(angle)
    m[1][1] = cos(rad)
    m[1][2] = sin(rad)
    m[2][1] = -1 * m[1][2]
    m[2][2] = m[1][1]
    matrix_mult(m,matrix)

def rotateZ(matrix,angle):
    m = new_matrix()
    ident(new_matrix)
    rad = randians(angle)
    m[2][2] = cos(rad)
    m[2][0] = sin(rad)
    m[0][2] = -1 * m[2][0]
    m[0][0] = m[2][2]
    matrix_mult(m,matrix)
