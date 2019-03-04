from display import *
from draw import *
from matrix import *
from parse import *
from transform import *
from math import cos,sin,tan,radians

screen = new_screen()
color = [ 0, 127, 255 ]
edges = []
transform = new_matrix()
ident(transform)

#rotateX(transform,32)
#print_matrix(transform)

#parse( 'script', edges, transform, screen, color )

f = open("art.txt","w")
points = []
octa = [[],[],[],[]]
for i in range(225,3376,450):
    points.append([int(200*cos(radians(i/10))),int(200*sin(radians(i/10)))])
const = cos(radians(22.5))
tans = sin(radians(22.5))
for i in range(8):
    f.write("line\n")
    f.write(str(int(points[i][0]*const)) + " " + str(int(points[i][1]*const)) + " 0 ")
    f.write(str(int(points[(i+1)%8][0]*const)) + " " + str(int(points[(i+1)%8][1]*const)) + " 0\n")
f.write("translate\n")
f.write("0 0 " + str(-2 * int(200*sin(radians(22.5)))) + "\n")
f.write("apply\nident\n")
for i in range(8):
    f.write("line\n")
    f.write(str(int(points[i][0]*const)) + " " + str(int(points[i][1]*const)) + " 0 ")
    f.write(str(int(points[(i+1)%8][0]*const)) + " " + str(int(points[(i+1)%8][1]*const)) + " 0\n")
f.write("translate\n")
f.write("0 0 " + str(int(200*sin(radians(22.5)))+int(200*cos(radians(22.5)))) + "\n")
f.write("apply\nident\n")
for i in range(8):
    f.write("line\n")
    f.write(str(int(points[i][0]*tans)) + " " + str(int(points[i][1]*tans)) + " 0 ")
    f.write(str(int(points[(i+1)%8][0]*tans)) + " " + str(int(points[(i+1)%8][1]*tans)) + " 0\n")
f.write("translate\n")
f.write("0 0 " + str(-2*int(200*cos(radians(22.5)))) + "\n")
f.write("apply\nident\n")
for i in range(8):
    f.write("line\n")
    f.write(str(int(points[i][0]*tans)) + " " + str(int(points[i][1]*tans)) + " 0 ")
    f.write(str(int(points[(i+1)%8][0]*tans)) + " " + str(int(points[(i+1)%8][1]*tans)) + " 0\n")
f.write("translate\n")
f.write("0 0 " + str(int(200*cos(radians(22.5)))) + "\n")
f.write("apply\nident\n")

f.write("rotate\nx 90\n")
f.write("apply\nident\n")
f.write("rotate\ny 22.5\n")
f.write("apply\nident\n")

for j in range(4):
    for i in range(8):
        f.write("line\n")
        f.write(str(points[i][0]) + " " + str(points[i][1]) + " 0 ")
        f.write(str(points[(i+1)%8][0]) + " " + str(points[(i+1)%8][1]) + " 0\n")
    f.write("rotate\ny 45\n")
    f.write("apply\n")
f.write("rotate\nz 20\nrotate\nx 20\nrotate\ny 20\n")
f.write("translate\n250 250 0\n")
f.write("apply\nsave\nart.png\n")
f.close()
parse("art.txt",edges,transform,screen,color)
