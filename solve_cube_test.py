from cube import Cubie, Cube
cubies = [
Cubie(0 , 0, 1, (None, None, 'w'), 'center'),
Cubie( 0,   0,    -1, (None, None, 'y'), 'center'),
Cubie(0 , 1,  0, (None, 'r', None), 'center'),
Cubie( 0,  -1,     0, (None, 'o', None), 'center'),
Cubie(1 , 0,  0, ('g', None, None), 'center'),
Cubie(-1,   0,     0, ('b', None, None), 'center'),
Cubie(-1,   1,     1, ('b', 'w', 'o'), 'corner'),
Cubie(0 , 1,  1, (None, 'y', 'b'), 'edge'),
Cubie(1 , 1,  1, ('w', 'g', 'r'), 'corner'),
Cubie(-1,   0,     1, ('o', None, 'y'), 'edge'),
Cubie(1 , 0,  1, ('g', None, 'y'), 'edge'),
Cubie(-1,  -1,     1, ('b', 'r', 'y'), 'corner'),
Cubie( 0,  -1,  1, (None, 'g', 'o'), 'edge'),
Cubie( 1,  -1,  1, ('o', 'y', 'b'), 'corner'),
Cubie(1 , 1, 0, ('b', 'o', None), 'edge'),
Cubie(-1,   1,  0, ('w', 'b', None), 'edge'),
Cubie(-1,  -1,  0, ('r', 'b', None), 'edge'),
Cubie( 1,  -1,  0, ('y', 'r', None), 'edge'),
Cubie(-1,   1, -1, ('w', 'r', 'b'), 'corner'),
Cubie( 0,   1, -1, (None, 'o', 'w'), 'edge'),
Cubie( 1,   1, -1, ('o', 'g', 'y'), 'corner'),
Cubie(-1,   0, -1, ('g', None, 'w'), 'edge'),
Cubie( 1,   0, -1, ('r', None, 'g'), 'edge'),
Cubie(-1,  -1, -1, ('g', 'o', 'w'), 'corner'),
Cubie( 0,  -1, -1, (None, 'w', 'r'), 'edge'),
Cubie( 1,  -1, -1, ('g', 'y', 'r'), 'corner')
    ]

cube = Cube(cubies)

print(cube.solve_cube())