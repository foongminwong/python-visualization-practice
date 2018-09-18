from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure ()

ax = fig.add_subplot (1, 1, 1, projection = '3d', aspect = 1)

# octahedron
A = [ 0.17770898,  0.72315927,  0.66742804]
B = [-0.65327074, -0.4196453 ,  0.63018661]
C = [ 0.65382635,  0.42081934, -0.62882604]
D = [-0.17907021, -0.72084723, -0.66956189]
E = [-0.73452809,  0.5495376 , -0.39809158]
F = [ 0.73451554, -0.55094017,  0.39617148]

OCTO = [[E, A, B],
        [E, B, D],
        [E, D, C],
        [E, C, A],
        [F, A, B],
        [F, B, D],
        [F, D, C],
        [F, C, A],
]

ax.add_collection3d (Poly3DCollection (OCTO))

# sphere
u = np.linspace (0, np.pi, 30)
v = np.linspace (0, 2 * np.pi, 30)
x = np.outer (np.sin (u), np.sin (v))
y = np.outer (np.sin (u), np.cos (v))
z = np.outer (np.cos (u), np.ones_like (v))
ax.plot_wireframe (x, y, z, alpha = 0.3)

plt.show ()
