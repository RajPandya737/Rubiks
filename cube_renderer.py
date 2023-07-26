import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

import collections
collections.Iterable = collections.abc.Iterable
collections.Mapping = collections.abc.Mapping
collections.MutableSet = collections.abc.MutableSet
collections.MutableMapping = collections.abc.MutableMapping
from rubik_solver import utils


class Cube_MPL:
    def __init__ (self, cube_string, solution=''):
        self.s = cube_string
        self.solution = 'Solution: ' + '-'.join(list(map(str, solution))) 

    def render(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        vertices, faces = self.reset_verticies_and_faces()
        ax.set_title(self.solution, fontsize=10)
        plt.suptitle("This should be your cube, follow the algorithm with red facing you and yellow facing up", fontsize=10)

        self.graph_setup(self.set_colors(), vertices, faces, ax)

    
    def graph_setup(self, colors, vertices, faces, ax):
        cubes = []
        for i, _ in enumerate(colors):
            cube = Poly3DCollection(faces, facecolors=colors[i], linewidths=1, edgecolors='black', alpha=0.99)
            cubes.append(cube)
        
        for cube in cubes:
            ax.add_collection3d(cube)


        # Set the axis limits
        ax.set_xlim([-2, 2])
        ax.set_ylim([-2, 2])
        ax.set_zlim([-2, 2])

        ax.set_xlabel('X-axis')
        ax.set_ylabel('Y-axis')
        ax.set_zlabel('Z-axis')

        #upper face

        cube_num = 0
        for z in range(0, -3, -1):
            for y in range(0, -3, -1):
                for x in range(-2, 1, 1):
                    try:
                        for vertex in vertices:
                            vertex[0] += x +0.5
                            vertex[1] += y + 0.5
                            vertex[2] += z + 0.5
                        cubes[cube_num].set_verts(faces)
                        vertices,faces = self.reset_verticies_and_faces()
                        cube_num += 1
                    except:
                        pass
        plt.show()


    def set_colors(self):
        colors = [
            [self.s[0], self.s[0], self.s[38], self.s[38], self.s[9], self.s[9]], 
            [self.s[1], self.s[1], self.s[37], self.s[37], 'black', 'black'],
            [self.s[2], self.s[2], self.s[36], self.s[36], self.s[29], self.s[29]],
            [self.s[3], self.s[3], 'black', 'black', self.s[10], self.s[10]],
            [self.s[4], self.s[4], 'black', 'black',  'black', 'black'],
            [self.s[5], self.s[5], 'black', 'black',  self.s[28], self.s[28]],
            [self.s[6], self.s[6], self.s[18], self.s[18],  self.s[11], self.s[11]],
            [self.s[7], self.s[7], self.s[19], self.s[19],  'black', 'black'],
            [self.s[8], self.s[8], self.s[20], self.s[20],  self.s[27], self.s[27]],
            ['black', 'black', self.s[41], self.s[41], self.s[10], self.s[10]],
            ['black', 'black', self.s[40], self.s[40], 'black', 'black'],
            ['black', 'black', self.s[39], self.s[39], self.s[32], self.s[32]],
            ['black', 'black', 'black', 'black', self.s[13], self.s[13]],
            ['black', 'black', 'black', 'black', 'black', 'black'],
            ['black', 'black', 'black', 'black', self.s[31], self.s[31]],
            ['black', 'black', self.s[21], self.s[21], self.s[14], self.s[14]],
            ['black', 'black', self.s[22], self.s[22], 'black', 'black'],
            ['black', 'black', self.s[23], self.s[23], self.s[30], self.s[30]],
            [self.s[51], self.s[51], self.s[44], self.s[44], self.s[15], self.s[15]],
            [self.s[52], self.s[52], self.s[43], self.s[43], 'black', 'black'],
            [self.s[53], self.s[53], self.s[42], self.s[42], self.s[35], self.s[35]],
            [self.s[48], self.s[48], 'black', 'black', self.s[12], self.s[12]],
            [self.s[49], self.s[49], 'black', 'black', 'black', 'black'],
            [self.s[50], self.s[50], 'black', 'black', self.s[34], self.s[34]],
            [self.s[45], self.s[45], self.s[24], self.s[24], self.s[16], self.s[16]],
            [self.s[46], self.s[46], self.s[25], self.s[25], 'black', 'black'],
            [self.s[47], self.s[47], self.s[26], self.s[26], self.s[33], self.s[33]]
        ]

        color_hash = {'r': 'red', 'y': 'yellow', 'b': 'blue', 'g': 'green', 'o': 'orange', 'w': 'white', 'black': 'black'}

        for i_1, color_set in enumerate(colors):
            for i_2, color in enumerate(color_set):
                colors[i_1][i_2] = color_hash[color]
        return colors

    def reset_verticies_and_faces(self):
        vertices = [
            [0, 0, 0],
            [1, 0, 0],
            [1, 1, 0],
            [0, 1, 0],
            [0, 0, 1],
            [1, 0, 1],
            [1, 1, 1],
            [0, 1, 1]
        ]
        faces = [
        [vertices[0], vertices[1], vertices[2], vertices[3]],  # Bottom face
        [vertices[4], vertices[5], vertices[6], vertices[7]],  # Top face
        [vertices[0], vertices[1], vertices[5], vertices[4]],  # Front face
        [vertices[2], vertices[3], vertices[7], vertices[6]],  # Back face
        [vertices[0], vertices[3], vertices[7], vertices[4]],  # Left face
        [vertices[1], vertices[2], vertices[6], vertices[5]]   # Right face
    ]
        return vertices, faces


# s = 'ryyyyyobyyogobobggwrggrowbrogbbggwwbrrgwowwwyrybrwboro'
# c = Cube_MPL(s, utils.solve(s, 'Kociemba'))
# c.render()
