from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib.pyplot as plt

import numpy as np
fig = plt.figure ()
ax = fig.add_subplot (1, 1, 1, projection = '3d', aspect = 1)



# extract and flatten points from the vertices
# decomposition.vertices[ii]['point']

#once!!!  store the result in self (the plotter object)

vertices = []
vertices.append([ 0.17770898,  0.72315927,  0.66742804])
vertices.append([-0.65327074, -0.4196453 ,  0.63018661])
vertices.append([ 0.65382635,  0.42081934, -0.62882604])
vertices.append([-0.17907021, -0.72084723, -0.66956189])
vertices.append([-0.73452809,  0.5495376 , -0.39809158])
vertices.append([ 0.73451554, -0.55094017,  0.39617148])



#happens in the plot_samples function

for ii in range(num_faces):
	#already have this data
	# sampler_data[face_index] = [[4,0,1],
	# 		[4,1,3],
	# 		[4,3,2],
	# 		[4,2,0],
	# 		[5,0,1],
	# 		[5,1,3],
	# 		[5,3,2],
	# 		[5,2,0],
	# ]

	actual_data = []
	for t in sampler_data[ii]:
		actual_data.append([vertices[t[0]],vertices[t[1]],vertices[t[2]]])

	ax.add_collection3d (Poly3DCollection (actual_data))


# at the very end of the plot call
plt.show ()


