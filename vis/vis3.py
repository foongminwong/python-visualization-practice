from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib.pyplot as plt
import numpy as np
import bertini_real
fig = plt.figure ()
ax = fig.add_subplot (1, 1, 1, projection = '3d', aspect = 1)

sphere_data = bertini_real.data.ReadMostRecent();
sphere_tuples = sphere_data.surface.surface_sampler_data

f = int(sphere_tuples[0][0])
s = int(sphere_tuples[0][1])
t = int(sphere_tuples[0][2])

f1 = sphere_data.vertices[f]
s1 = sphere_data.vertices[s]
t1 = sphere_data.vertices[t]

fx= f1['point'][0].real
fy= f1['point'][1].real
fz= f1['point'][2].real

sx=s1['point'][0].real
sy=s1['point'][1].real
sz=s1['point'][2].real

tx = t1['point'][0].real
ty = t1['point'][1].real
tz = t1['point'][2].real

ff = [fx,fy,fz]
ss = [sx,sy,sz]
tt = [tx,ty,tz]
ax.scatter(ff,ss,tt)
ax.plot3D(ff,ss,tt)
plt.show()



