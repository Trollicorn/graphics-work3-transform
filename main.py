from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()
"""
print("new matrix:")
print_matrix(matrix)

print("\nidentity matrix")
ident(matrix)

print_matrix(matrix)
"""
m0 = [ [1,4,7],[2,5,8],[3,6,9]]
m1 = [ [4,10,3],[12,5,6],[7,8,1]]
print_matrix(m0)
print("\n")
print_matrix(m1)
print("\n")
matrix_mult(m1,m0)
print_matrix(m1)
print("\n")
print_matrix(m0)

# expect
#  33  40  26
#  84 109  74
# 135 178 122


#draw_lines( matrix, screen, color )
#display(screen)
