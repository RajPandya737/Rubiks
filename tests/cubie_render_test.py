 

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Define the vertices of the cube
def reset_verticies_and_faces():
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
# Define the faces of the cube using the vertices
faces = [
    [vertices[0], vertices[1], vertices[2], vertices[3]],  # Bottom face
    [vertices[4], vertices[5], vertices[6], vertices[7]],  # Top face
    [vertices[0], vertices[1], vertices[5], vertices[4]],  # Front face
    [vertices[2], vertices[3], vertices[7], vertices[6]],  # Back face
    [vertices[0], vertices[3], vertices[7], vertices[4]],  # Left face
    [vertices[1], vertices[2], vertices[6], vertices[5]]   # Right face
]

# Define colors for each face
colors = ['white', 'yellow', 'red', 'orange', 'blue', 'green']

# Create the Poly3DCollection and add it to the plot
cube1 = Poly3DCollection(faces, facecolors=colors, linewidths=1, edgecolors='black', alpha=0.99)
cube2 = Poly3DCollection(faces, facecolors=colors, linewidths=1, edgecolors='black', alpha=0.99)
cube3 = Poly3DCollection(faces, facecolors=colors, linewidths=1, edgecolors='black', alpha=0.99)
cube4 = Poly3DCollection(faces, facecolors=colors, linewidths=1, edgecolors='black', alpha=0.99)
cube5 = Poly3DCollection(faces, facecolors=colors, linewidths=1, edgecolors='black', alpha=0.99)
cube6 = Poly3DCollection(faces, facecolors=colors, linewidths=1, edgecolors='black', alpha=0.99)
cube7 = Poly3DCollection(faces, facecolors=colors, linewidths=1, edgecolors='black', alpha=0.99)
cube8 = Poly3DCollection(faces, facecolors=colors, linewidths=1, edgecolors='black', alpha=0.99)
cube9 = Poly3DCollection(faces, facecolors=colors, linewidths=1, edgecolors='black', alpha=0.99)

cube10 = Poly3DCollection(faces, facecolors=colors, linewidths=1, edgecolors='black', alpha=0.99)
cube11 = Poly3DCollection(faces, facecolors=colors, linewidths=1, edgecolors='black', alpha=0.99)
cube12 = Poly3DCollection(faces, facecolors=colors, linewidths=1, edgecolors='black', alpha=0.99)
cube13 = Poly3DCollection(faces, facecolors=colors, linewidths=1, edgecolors='black', alpha=0.99)
cube14 = Poly3DCollection(faces, facecolors=colors, linewidths=1, edgecolors='black', alpha=0.99)
cube15 = Poly3DCollection(faces, facecolors=colors, linewidths=1, edgecolors='black', alpha=0.99)
cube16 = Poly3DCollection(faces, facecolors=colors, linewidths=1, edgecolors='black', alpha=0.99)
cube17 = Poly3DCollection(faces, facecolors=colors, linewidths=1, edgecolors='black', alpha=0.99)
cube18 = Poly3DCollection(faces, facecolors=colors, linewidths=1, edgecolors='black', alpha=0.99)

cube19 = Poly3DCollection(faces, facecolors=colors, linewidths=1, edgecolors='black', alpha=0.99)
cube20 = Poly3DCollection(faces, facecolors=colors, linewidths=1, edgecolors='black', alpha=0.99)
cube21 = Poly3DCollection(faces, facecolors=colors, linewidths=1, edgecolors='black', alpha=0.99)
cube22 = Poly3DCollection(faces, facecolors=colors, linewidths=1, edgecolors='black', alpha=0.99)
cube23 = Poly3DCollection(faces, facecolors=colors, linewidths=1, edgecolors='black', alpha=0.99)
cube24 = Poly3DCollection(faces, facecolors=colors, linewidths=1, edgecolors='black', alpha=0.99)
cube25 = Poly3DCollection(faces, facecolors=colors, linewidths=1, edgecolors='black', alpha=0.99)
cube26 = Poly3DCollection(faces, facecolors=colors, linewidths=1, edgecolors='black', alpha=0.99)
cube27 = Poly3DCollection(faces, facecolors=colors, linewidths=1, edgecolors='black', alpha=0.99)





ax.add_collection3d(cube1)
ax.add_collection3d(cube2)
ax.add_collection3d(cube3)
ax.add_collection3d(cube4)
ax.add_collection3d(cube5)
ax.add_collection3d(cube6)
ax.add_collection3d(cube7)
ax.add_collection3d(cube8)
ax.add_collection3d(cube9)

ax.add_collection3d(cube10)
ax.add_collection3d(cube11)
ax.add_collection3d(cube12)
ax.add_collection3d(cube13)
ax.add_collection3d(cube14)
ax.add_collection3d(cube15)
ax.add_collection3d(cube16)
ax.add_collection3d(cube17)
ax.add_collection3d(cube18)

ax.add_collection3d(cube19)
ax.add_collection3d(cube20)
ax.add_collection3d(cube21)
ax.add_collection3d(cube22)
ax.add_collection3d(cube23)
ax.add_collection3d(cube24)
ax.add_collection3d(cube25)
ax.add_collection3d(cube26)
ax.add_collection3d(cube27)



# Set the axis limits
ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])
ax.set_zlim([-2, 2])

# Add labels for clarity (optional)
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')

shift_x, shift_y, shift_z = -1.5, 0.5, 0.5
for vertex in vertices:
    vertex[0] += shift_x
    vertex[1] += shift_y
    vertex[2] += shift_z
cube1.set_verts(faces)
vertices,faces = reset_verticies_and_faces()

shift_x, shift_y, shift_z = -0.5, 0.5, 0.5
for vertex in vertices:
    vertex[0] += shift_x
    vertex[1] += shift_y
    vertex[2] += shift_z
cube2.set_verts(faces)
vertices,faces = reset_verticies_and_faces()

shift_x, shift_y, shift_z = 0.5, 0.5, 0.5
for vertex in vertices:
    vertex[0] += shift_x
    vertex[1] += shift_y
    vertex[2] += shift_z
cube3.set_verts(faces)
vertices,faces = reset_verticies_and_faces()

shift_x, shift_y, shift_z = -1.5, -0.5, 0.5
for vertex in vertices:
    vertex[0] += shift_x
    vertex[1] += shift_y
    vertex[2] += shift_z
cube4.set_verts(faces)
vertices,faces = reset_verticies_and_faces()

shift_x, shift_y, shift_z = -0.5, -0.5, 0.5
for vertex in vertices:
    vertex[0] += shift_x
    vertex[1] += shift_y
    vertex[2] += shift_z
cube5.set_verts(faces)
vertices,faces = reset_verticies_and_faces()

shift_x, shift_y, shift_z = 0.5, -0.5, 0.5
for vertex in vertices:
    vertex[0] += shift_x
    vertex[1] += shift_y
    vertex[2] += shift_z
cube6.set_verts(faces)
vertices,faces = reset_verticies_and_faces()

shift_x, shift_y, shift_z = -1.5, -1.5, 0.5
for vertex in vertices:
    vertex[0] += shift_x
    vertex[1] += shift_y
    vertex[2] += shift_z
cube7.set_verts(faces)
vertices,faces = reset_verticies_and_faces()

shift_x, shift_y, shift_z = -0.5, -1.5, 0.5
for vertex in vertices:
    vertex[0] += shift_x
    vertex[1] += shift_y
    vertex[2] += shift_z
cube8.set_verts(faces)
vertices,faces = reset_verticies_and_faces()

shift_x, shift_y, shift_z = 0.5, -1.5, 0.5
for vertex in vertices:
    vertex[0] += shift_x
    vertex[1] += shift_y
    vertex[2] += shift_z
cube9.set_verts(faces)
vertices,faces = reset_verticies_and_faces()








shift_x, shift_y, shift_z = -1.5, 0.5, -0.5
for vertex in vertices:
    vertex[0] += shift_x
    vertex[1] += shift_y
    vertex[2] += shift_z
cube10.set_verts(faces)
vertices,faces = reset_verticies_and_faces()

shift_x, shift_y, shift_z = -0.5, 0.5, -0.5
for vertex in vertices:
    vertex[0] += shift_x
    vertex[1] += shift_y
    vertex[2] += shift_z
cube11.set_verts(faces)
vertices,faces = reset_verticies_and_faces()

shift_x, shift_y, shift_z = 0.5, 0.5, -0.5
for vertex in vertices:
    vertex[0] += shift_x
    vertex[1] += shift_y
    vertex[2] += shift_z
cube12.set_verts(faces)
vertices,faces = reset_verticies_and_faces()

shift_x, shift_y, shift_z = -1.5, -0.5, -0.5
for vertex in vertices:
    vertex[0] += shift_x
    vertex[1] += shift_y
    vertex[2] += shift_z
cube13.set_verts(faces)
vertices,faces = reset_verticies_and_faces()

shift_x, shift_y, shift_z = -0.5, -0.5, -0.5
for vertex in vertices:
    vertex[0] += shift_x
    vertex[1] += shift_y
    vertex[2] += shift_z
cube14.set_verts(faces)
vertices,faces = reset_verticies_and_faces()

shift_x, shift_y, shift_z = 0.5, -0.5, -0.5
for vertex in vertices:
    vertex[0] += shift_x
    vertex[1] += shift_y
    vertex[2] += shift_z
cube15.set_verts(faces)
vertices,faces = reset_verticies_and_faces()

shift_x, shift_y, shift_z = -1.5, -1.5, -0.5
for vertex in vertices:
    vertex[0] += shift_x
    vertex[1] += shift_y
    vertex[2] += shift_z
cube16.set_verts(faces)
vertices,faces = reset_verticies_and_faces()

shift_x, shift_y, shift_z = -0.5, -1.5, -0.5
for vertex in vertices:
    vertex[0] += shift_x
    vertex[1] += shift_y
    vertex[2] += shift_z
cube17.set_verts(faces)
vertices,faces = reset_verticies_and_faces()

shift_x, shift_y, shift_z = 0.5, -1.5, -0.5
for vertex in vertices:
    vertex[0] += shift_x
    vertex[1] += shift_y
    vertex[2] += shift_z
cube18.set_verts(faces)
vertices,faces = reset_verticies_and_faces()






shift_x, shift_y, shift_z = -1.5, 0.5, -1.5
for vertex in vertices:
    vertex[0] += shift_x
    vertex[1] += shift_y
    vertex[2] += shift_z
cube19.set_verts(faces)
vertices,faces = reset_verticies_and_faces()

shift_x, shift_y, shift_z = -0.5, 0.5, -1.5
for vertex in vertices:
    vertex[0] += shift_x
    vertex[1] += shift_y
    vertex[2] += shift_z
cube20.set_verts(faces)
vertices,faces = reset_verticies_and_faces()

shift_x, shift_y, shift_z = 0.5, 0.5, -1.5
for vertex in vertices:
    vertex[0] += shift_x
    vertex[1] += shift_y
    vertex[2] += shift_z
cube21.set_verts(faces)
vertices,faces = reset_verticies_and_faces()

shift_x, shift_y, shift_z = -1.5, -0.5, -1.5
for vertex in vertices:
    vertex[0] += shift_x
    vertex[1] += shift_y
    vertex[2] += shift_z
cube22.set_verts(faces)
vertices,faces = reset_verticies_and_faces()

shift_x, shift_y, shift_z = -0.5, -0.5, -1.5
for vertex in vertices:
    vertex[0] += shift_x
    vertex[1] += shift_y
    vertex[2] += shift_z
cube23.set_verts(faces)
vertices,faces = reset_verticies_and_faces()

shift_x, shift_y, shift_z = 0.5, -0.5, -1.5
for vertex in vertices:
    vertex[0] += shift_x
    vertex[1] += shift_y
    vertex[2] += shift_z
cube24.set_verts(faces)
vertices,faces = reset_verticies_and_faces()

shift_x, shift_y, shift_z = -1.5, -1.5, -1.5
for vertex in vertices:
    vertex[0] += shift_x
    vertex[1] += shift_y
    vertex[2] += shift_z
cube25.set_verts(faces)
vertices,faces = reset_verticies_and_faces()

shift_x, shift_y, shift_z = -0.5, -1.5, -1.5
for vertex in vertices:
    vertex[0] += shift_x
    vertex[1] += shift_y
    vertex[2] += shift_z
cube26.set_verts(faces)
vertices,faces = reset_verticies_and_faces()

shift_x, shift_y, shift_z = 0.5, -1.5, -1.5
for vertex in vertices:
    vertex[0] += shift_x
    vertex[1] += shift_y
    vertex[2] += shift_z
cube27.set_verts(faces)
vertices,faces = reset_verticies_and_faces()






plt.show()
