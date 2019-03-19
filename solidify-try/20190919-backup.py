    def solidify(self, totalDist,offset):

        # stl = input('Enter a STL filename:')
        stl = "mystl.stl"

        offset = 0.5
        total = 1.5

        tmesh = trimesh.load(str(stl))
        A = copy.deepcopy(tmesh)
        B = copy.deepcopy(tmesh)

        # reverse every triangles and flip every normals
        B.invert()

        # calculate A, B vertex normals
        vertexnormsA = A.vertex_normals
        vertexnormsB = B.vertex_normals

        distA =  (total/2)*(offset+1)
        distB = 1 - distA
        
        print(len(A.vertices))

        # # create a list to store  amount of distance for A to move
        # # amountDistA = []
        
        # for vnorm in A.vertex_normals:
        #     amountDistA.append(vnorm * distA)

        # check for unit normals
        # # for each vertexA, move vertexA to distA corresponding to vertexnormals of A
        for v in A.vertices:
            v += vnorm[v] * distA

        # # create a list to store  amount of distance for B to move
        # amountDistB = []
        
        # for vnorm in B.vertex_normals:
        #     amountDistB.append(vnorm * distB)

        # # for each vertexA, move vertexB to corresponding B vertex normals
        # for v in B.vertices:
        #     # for each amount of distance B
        #     for i in range(len(amountDistB)):
        #         v += amountDistB[i]


        # # add boundary faces
        # # concatenate, add new faces, not adding new vertices
        # faces = self.decomposition.surface
        # # # indices of this point, bounding sphere
        # sphere_curve = faces.sphere_curve.sampler_data #[[x,x,x],[0],[1]]

        # numVerts = len(A.vertices) # 3309 for a plane

        # T = []
        # for edge in sphere_curve:
        #     for i in range(numVerts-1):
        #         print(edge[i],edge[i+1],edge[i]+numVerts)
                # t1 = [edge[i],edge[i+1],edge[i]+numVerts]
                # t2 = [edge[i],edge[i]+numVerts,edge[i+1]+numVerts]
                # T.append(t1)
                # T.append(t2)
        
        # print(T)

#--------------------------------------------------------------------------------------------------------------------------------------------------#
# Export stl
        # newA = trimesh.Trimesh(A.vertices, A.faces)

        # fileName = os.getcwd().split(os.sep)[-1]

        # newA.export(file_obj='test_' +
        #                 fileName + '.stl', file_type='stl')

#---------------------------------------------------------------------------#

 
        # read mostrecent()
        # x.surface.sphere_curve
        # walk down the edge, add the triangles,
        # trimesh add vertices
        # for each edge, then for each consecutive pair
        # https://github.com/mikedh/trimesh/blob/master/trimesh/creation.py

        # Junk: testing some codes
        # create a list to store new vertices B
        # newvB = []
        # # for each vertexA, move vertexB to corresponding B vertex normals
        # for v in B.vertices:
        #     for vnorm in vertexnormsB:
        #         newvB.append(np.add(v,list(np.asarray(vnorm)*distB)))

    # def test(self):
    #     stl = "mystl.stl"
    #     tmesh = trimesh.load(str(stl))
    #     print(tmesh.vertices)
    #     print(tmesh.faces)
    #     nested_lst_of_tuples = [tuple(l) for l in tmesh.faces]
    #     print([nested_lst_of_tuples])


