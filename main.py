from display import *
from draw import *
from matrix import *
from parse import *
from transform import *

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
transform = new_matrix()
ident(transform)

parse( 'script', edges, transform, screen, color )
