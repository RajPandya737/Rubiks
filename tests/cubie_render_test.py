import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def cubes(sides):
    data = np.ones(sides, dtype=bool)
    alpha = 1
    colors = np.empty(sides + [4], dtype=float)
    colors[0] = [1, 0, 0, alpha]
    colors[1] = [1, 0, 0, alpha]
    colors[2] = [1, 0, 0, alpha]

    fig = plt.figure(figsize=(9, 9))
    ax = fig.add_subplot(111, projection='3d')
    ax.voxels(data, facecolors=colors, edgecolors='white')
    plt.title("Demonstrating three-dimensional cubes")
    plt.show()

def main():
    sides = [3, 3, 3]  # Changed to create a 3x3x3 cube
    cubes(sides)

if __name__ == "__main__":
    main()
