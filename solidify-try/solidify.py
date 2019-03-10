import os
import numpy as np
import dill
import numpy as np
import matplotlib
from stl import mesh
import trimesh
import copy 

class ReversableList(list):
    """ Create a ReversableList object for reversing order of data """

    def reverse(self):
        """ A reverse function for raw surface data

        Returns a reversed list
        """
        return list(reversed(self))

# load stl
mesh = trimesh.load('mystl.stl')

A = copy.deepcopy(mesh)
B = copy.deepcopy(mesh)

# reverse every triangles and flip every normals
B.invert()

# calculate A, B vertex normals
vertexnormsA = A.vertex_normals
vertexnormsB = B.vertex_normals

offset = 0.5
total = 1.5

distA =  (total/2)*(offset+1)
distB = 1 - distA

for v in vertexnormsA:
	print(v+distA)

for v in vertexnormsB:	
	print(v+distB)


#
print("No errors!")
