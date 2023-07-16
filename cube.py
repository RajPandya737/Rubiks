

"""
This is what the cube looks like, the positive axis are shown below, the faces are white, red, and green denoted by w r, g

A colored square is on the y-axis when it is at a 90 degree angle to the y-axis, x-axis when it is 90 degrees to the x-axis
and z-axis when it is 90 degrees to the z-axis. 

In this situation, the red squares are on the y-axis, 
white squares oin the z-axis, and green squares on the x-axis


        .------.
       /  r   /|
      /      / |
     +------+ g+
     |  w   | / 
     |      |/
     +------+

    - ---------- + This is the x-axis, right is positive, when a rotation is applied, the piece moves along the x-z plane


    +
    |
    |
    |     This is the y-axis, up is positive, when a rotation is applied, the piece moves along the y-z plane
    |
    |
    |
    -

          -
         /
        /
       /      This is the z-azis, forward is positive
      /
     /
    +

"""

import numpy as np
from math import sin, cos, pi


def rotation_matrix(axis, n):
    
    n = n%4
    sin_hash = {90: 1, 180: 0, 270:-1, 360:0}
    cos_hash = {90: 0, 180: -1, 270:0, 360:1}
    angle_sin = sin_hash[90*n]
    angle_cos = cos_hash[90*n]

    # angle_sin = sin(n*pi/2)
    # angle_cos = cos(n*pi/2)
    if axis == 'y':
        return np.array([[1,0,0], [0,angle_cos,-1*angle_sin], [0, angle_sin, angle_cos]])
    elif axis == 'x':
        return np.array([[angle_cos,0,angle_sin], [0,1,0], [-1*angle_sin, 0, angle_cos]])

    return 'Error, improper axis format provided'

class Cubie:
    def __init__(self, x, y, z, colors, type):
        # coordinates of the cubie
        self.x = x
        self.y = y
        self.z = z
        self.position = np.array([x, y, z])
        # colors of the cubie, in the form (cx, cy, cz) dependant on which axis it is facing
        self.colors = colors
        # type could be corner, edge, or center
        self.type = type
    
    def round_pos (self):
        self.position = np.array()


# Need to add color rotation
# Rotate function pass along that axis, perpendicular to the other 2 axises
    def rotate_x(self, n):
        self.position = np.dot(rotation_matrix('x', n), self.position)
        self.position = np.round(self.position)

        #if rotated on the x-axis, the color facing up/down (y-axis) will not change, but x and z colors will be swapped
        for i in range(n):
            self.colors = (self.colors[2], self.colors[1], self.colors[0])
        
    def rotate_y(self, n):
        self.position = np.dot(rotation_matrix('y', n), self.position)
        self.position = np.round(self.position)

        #If rotated on the y-axis, the color facing the right/left (x-axis) will not change, but the y and z colors will be swapped
        for i in range(n):
            self.colors = (self.colors[0], self.colors[2], self.colors[1])




Piece = Cubie(1, 1, 1, ('g', 'r', 'w'), 'corner')
Piece.rotate_x(1)


# class Cube:
#     def __init__(self):
#         self.cubies = []

#     def insert_cubie_single (self, cubie):
#         self.cubies.append(cubie)

#     def insert_cubie_group (self, cubie_list):
#         for cubie in cubie_list:
#             self.cubies.append(cubie)
#     def __str__(self) -> str:
#         pass






