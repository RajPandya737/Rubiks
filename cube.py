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

    - ---------- + This is the x-axis, right is positive, when a rotation is applied, the layer moves about the x-axis
#   -1    0    1

    +  1
    |
    |
    |  0  This is the y-axis, up is positive, when a rotation is applied, the layer moves about the y-axis
    |
    |
    |  -1
    -

          -  -1
         /
        /
       /  0   This is the z-azis, forward is positive, when a rotation is applied, the layer moves about the z-axis
      /
     /
    +  1

"""

import numpy as np
from math import sin, cos, pi
import collections.abc
#hyper needs the four following aliases to be done manually.
collections.Iterable = collections.abc.Iterable
collections.Mapping = collections.abc.Mapping
collections.MutableSet = collections.abc.MutableSet
collections.MutableMapping = collections.abc.MutableMapping
from rubik_solver import utils


def rotation_matrix(axis, n):
    
    n = n%4
    sin_hash = {90: 1, 180: 0, 270:-1, 360:0}
    cos_hash = {90: 0, 180: -1, 270:0, 360:1}
    angle_sin = sin_hash[90*n]
    angle_cos = cos_hash[90*n]

    # angle_sin = sin(n*pi/2)
    # angle_cos = cos(n*pi/2)
    if axis == "x":
        return np.array([[1,0,0], [0,angle_cos,-1*angle_sin], [0, angle_sin, angle_cos]])
    elif axis == "y":
        return np.array([[angle_cos,0,angle_sin], [0,1,0], [-1*angle_sin, 0, angle_cos]])
    elif axis == "z":
        return np.array([[angle_cos, -1*angle_sin, 0], [angle_sin,angle_cos,0], [0, 0, 1]])

    return "Error, improper axis format provided"

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
    
    def round_pos(self):
        self.position = np.array()


    def rotate_x(self, n):
        # The piece moves downwards when facing the white
        self.position = np.dot(rotation_matrix("x", n), self.position)
        for i in range(n):
            self.colors = (self.colors[0], self.colors[2], self.colors[1])
        
    def rotate_y(self, n):
        self.position = np.dot(rotation_matrix("y", n), self.position)

        #If rotated on the y-axis, the color facing the right/left (x-axis) will not change, but the y and z colors will be swapped
        for i in range(n):
            self.colors = (self.colors[2], self.colors[1], self.colors[0])
        
    def rotate_z(self, n):
        self.position = np.dot(rotation_matrix("z", n), self.position)

        #If rotated on the y-axis, the color facing the right/left (x-axis) will not change, but the y and z colors will be swapped
        for i in range(n):
            self.colors = (self.colors[1], self.colors[0], self.colors[2])



class Cube:
    def __init__(self, cubies: list):
        self.cubies = cubies

    def __str__(self):
        to_return = ""

        # Yellow face

        for i in range (-1, 2):
            for j in range(-1,2):
                to_return += self.get_cubies_by_position(j, i, -1).colors[2]

        # Blue Face Baby, yea yea aight
        for i in range (-1, 2):
            for j in range(-1,2):
                to_return += self.get_cubies_by_position(-1, j, i).colors[0]

        # Red Face
        
        for i in range (-1, 2):
            for j in range(-1,2):
                to_return += self.get_cubies_by_position(j, 1, i).colors[1]

        # Green Face

        for i in range (-1, 2):
            for j in range(-1,2):
                to_return += self.get_cubies_by_position(1, -j, i).colors[0]

        # Orange Face
        for i in range (-1, 2):
            for j in range(-1,2):
                to_return += self.get_cubies_by_position(-j, -1, i).colors[1]

        # White Face

        for i in range (-1, 2):
            for j in range(-1,2):
                to_return += self.get_cubies_by_position(j, -i, 1).colors[2]
        
        return to_return
    
    def add_cubie(self, cubie):
        self.cubies.append(cubie)
    
    def remove_cubie(self, cubie):
        self.cubies.remove(cubie)

    
    def get_cubies(self):
        return self.cubies
    
    def get_cubies_by_position(self, x,y,z):
        for cubie in self.cubies:
            if cubie.position[0] == x and cubie.position[1] == y and cubie.position[2] == z:
                return cubie

    def rotate_x(self, n, layer):
        for cubie in self.cubies:
            if cubie.position[0] == layer:
                cubie.rotate_x(n)
    
    def rotate_y(self, n, layer):
        for cubie in self.cubies:
            if cubie.position[1] == layer:
                cubie.rotate_y(n)
    
    def rotate_z(self, n, layer):
        for cubie in self.cubies:
            if cubie.position[2] == layer:
                cubie.rotate_z(n)

    def solve_cube_str(self):
        str_rep = self.__str__()
        return utils.solve(str_rep, 'Kociemba')

