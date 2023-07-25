 

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Define the vertices of the cube
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
colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange']

# Create the Poly3DCollection and add it to the plot
cube = Poly3DCollection(faces, facecolors=colors, linewidths=1, edgecolors='r', alpha=0.99)
cube2 = Poly3DCollection(faces, facecolors=colors, linewidths=1, edgecolors='r', alpha=0.99)
ax.add_collection3d(cube)
ax.add_collection3d(cube2)

# Set the axis limits
ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])
ax.set_zlim([-2, 2])

# Add labels for clarity (optional)
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')

shift_x, shift_y, shift_z = 0, 0, 0
for vertex in vertices:
    vertex[0] += shift_x
    vertex[1] += shift_y
    vertex[2] += shift_z
cube.set_verts(faces)

shift_x, shift_y, shift_z = 1, 1, 0
for vertex in vertices:
    vertex[0] += shift_x
    vertex[1] += shift_y
    vertex[2] += shift_z
cube2.set_verts(faces)

plt.show()
