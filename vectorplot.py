import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Function to plot ray-triangle intersection
def plot_ray_triangle_intersection(ray_origin, ray_direction, triangle_vertices):
    # Extract triangle vertices
    V0, V1, V2 = triangle_vertices

    # Create figure
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Plot triangle
    x = [V0[0], V1[0], V2[0], V0[0]]
    y = [V0[1], V1[1], V2[1], V0[1]]
    z = [V0[2], V1[2], V2[2], V0[2]]
    ax.plot_trisurf(x, y, z, color='orange', alpha=0.5)

    # Plot ray
    t_values = np.linspace(0, 5, 100)
    ray_points = np.array([ray_origin + t * ray_direction for t in t_values])

    ax.plot(ray_points[:, 0], ray_points[:, 1], ray_points[:, 2], color='blue', label='Ray', linestyle='-', linewidth=2)

    # Plot origin
    ax.scatter(ray_origin[0], ray_origin[1], ray_origin[2], color='red', s=100, label='Ray Origin')

    # Labels and formatting
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.legend()

    plt.title('Ray-Triangle Intersection')
    plt.show()

# Define triangle vertices (V0, V1, V2)
V0 = np.array([0, 0, 0])
V1 = np.array([1, 0, 0])
V2 = np.array([0, 1, 0])

# Define ray origin and direction
ray_origin = np.array([0.1, 0.1, -1])
ray_direction = np.array([0, 0, 1])

# Plot the ray and triangle
plot_ray_triangle_intersection(ray_origin, ray_direction, [V0, V1, V2])
