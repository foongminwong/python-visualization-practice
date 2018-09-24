from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib.pyplot as plt
import numpy as np
import bertini_real

fig = plt.figure ()
ax = fig.add_subplot (1, 1, 1, projection = '3d', aspect = 1)

data = bertini_real.data.ReadMostRecent();
tuples = data.surface.surface_sampler_data

#extract points from vertices
def extractPoints(data):
	points = []

	for v in data.vertices:
		q=[None]*3 #preallocation

		for i in range(3):
			q[i]=v['point'][i].real
		points.append(q)
	return points

points = extractPoints(data)

T = []
#T=[[points[f],points[s],points[t]]]

#loop over them, see Matlab code
# for each tri on that face, two loops
for i in range(0):
	
	for j in range(0):
		f = int(tuples[i][j][0])
		s = int(tuples[i][j][1])
		t = int(tuples[i][j][2])
		k = [points[f],points[s],points[t]]
		T.append(k)

#f = int(tuples[0][0][0])
#s = int(tuples[0][0][1])
#t = int(tuples[0][0][2])

# T grows through the loop
#for t in points
ax.add_collection3d(Poly3DCollection(T))

plt.show()

