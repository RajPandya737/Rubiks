import numpy as np
from math import sin, cos, pi

#This is what the cube looks like, the positive axis are shown below, the faces are white, red, and green denoted by w r, g


    #     .------.
    #    /  r   /|
    #   /      / |
    #  +------+ g+
    #  |  w   | / 
    #  |      |/
    #  +------+

    # - ---------- + this is the x-axis, right is positive, when a rotation is applied, the piece moves down when viewing the white side


    # +
    # |
    # |
    # |     This is the y-axis, up is positive, when a rotation is applied, the piece moves left when viewing the white side
    # |
    # |
    # |
    # -

    #       -
    #      /
    #     /
    #    /      This is the z-azis, forward is positive
    #   /
    #  /
    # +


def rotation_matrix(axis, n):
    angle_sin = sin(n*pi/2)
    angle_cos = cos(n*pi/2)
    if axis == 'x':
        return np.array([[1,0,0], [0,angle_cos,-1*angle_sin], [0, angle_sin, angle_cos]])
    elif axis == 'y':
        return np.array([[angle_cos,0,angle_sin], [0,1,0], [-1*angle_sin, 0, angle_cos]])

    return 'Error, improper axis format provided'

class Cubie:
    def __init__(self, x, y, z, colors, type):
        #coordinates of the cubie
        self.x = x
        self.y = y
        self.z = z
        self.position = np.array([x, y, z])
        # colors of the cubie, in the form (cx, cy, cz) dependant on which axis it is facing
        self.colors = colors
        # type could be corner, edge, or center
        self.type = type
    
    #rotates passing through the x=axis
    def round_pos (self):
        self.position = np.array()


# Need to add color rotation
    def rotate_x(self, n):
        self.position = np.dot(rotation_matrix('x', n), self.position)
        self.position = np.round(self.position)
        print(self.position)

    def rotate_y(self, n):
        self.position = np.dot(rotation_matrix('y', n), self.position)
        self.position = np.round(self.position)
        print(self.position)



Piece = Cubie(0, 0, 1, ('o', 'b', 'w'), 'corner')

Piece.rotate_x(1)






