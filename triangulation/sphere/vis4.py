from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib.pyplot as plt
import numpy as np
import bertini_real

fig = plt.figure ()
ax = fig.add_subplot (1, 1, 1, projection = '3d', aspect = 1)


sphere_data = bertini_real.data.ReadMostRecent();
sphere_tuples = sphere_data.surface.surface_sampler_data


#loop over them, see Matlab code
# for each tri on that face, two loops
f = int(sphere_tuples[0][0])
s = int(sphere_tuples[0][1])
t = int(sphere_tuples[0][2])

#junk
f1 = sphere_data.vertices[f]
s1 = sphere_data.vertices[s]
t1 = sphere_data.vertices[t]
f2 = sphere_data.vertices[f]
s2 = sphere_data.vertices[s]
t2 = sphere_data.vertices[t]

#quiz: don't use append
def extractPoints(data):
	points = []

	for v in data.vertices:
		q=[None]*3 #preallocation

		for i in range(3):
			q[i]=v['point'][i].real
		points.append(q)
	return points

points = extractPoints(sphere_data)
#junk
fx= f1['point'][0].real
fy= f1['point'][1].real
fz= f1['point'][2].real

sx=s1['point'][0].real
sy=s1['point'][1].real
sz=s1['point'][2].real

tx = t1['point'][0].real
ty = t1['point'][1].real
tz = t1['point'][2].real

#junk
ff = [fx,fy,fz]
ss = [sx,sy,sz]
tt = [tx,ty,tz]

# here (T grows through the loop)
T = []
T=[[points[f],points[s],points[t]]]
ax.add_collection3d(Poly3DCollection(T))
#ax.scatter(ff,ss,tt)
#ax.plot3D(ff,ss,tt)
plt.show()

