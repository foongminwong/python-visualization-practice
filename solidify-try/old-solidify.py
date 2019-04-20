    def solidify(self, totalDist, offset):

        # stl = input('Enter a STL filename:')

        stl = "mystl.stl"

        offset = 0
        total = 0.1

        tmesh = trimesh.load(str(stl))
        A = copy.deepcopy(tmesh)
        B = copy.deepcopy(tmesh)

        # reverse every triangles and flip every normals
        B.invert()

        # calculate A, B vertex normals
        vertexnormsA = A.vertex_normals
        vertexnormsB = B.vertex_normals

        distA = (total) * (offset + 1) / 2
        distB = (total) * (1 - (offset + 1) / 2)

        # print(len(A.vertices))
        # # create a list to store  amount of distance for A to move
        # # amountDistA = []

        # for vnorm in A.vertex_normals:
        #     amountDistA.append(vnorm * distA)

        # # for each vertexA, move vertexA to distA corresponding to vertexnormals of A
        # for v in A.vertices:
        #     v += vnorm[v] * distA

        # create A & B vertices that move corresponding to vertex normals and
        # distance
        A.vertices = [v + vn * distA for v,
                      vn in zip(A.vertices, A.vertex_normals)]
        B.vertices = [v + vn * distB for v,
                      vn in zip(B.vertices, B.vertex_normals)]

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

        ####

        # FIND when it drops the point (two libraries)
        # WHAT POINT IT THROWS AWAY THE DISCONNECTED THE EXTRA POINT
        # 	WHEN YOUT TRIMESH
        # unreferenced vertices

        ####

        faces = self.decomposition.surface

        # print(self.decomposition.)
        # # # indices of this point, bounding sphere
        sphere_curve = faces.sphere_curve.sampler_data  # [[x,x,x],[0],[1]]

        numVerts = len(A.vertices)

        T = []

        f = A.facets_boundary
        print(f)
        ff = [l.tolist() for l in f]
        ff = list(chain.from_iterable(ff))
        print(ff)

        # print(sphere_curve)

        print(sphere_curve)
        for edge in sphere_curve:
            # for edge in ff:
                # for i in range(numVerts-1):
            for i in range(len(edge) - 1):
                # t1 = [edge[i],edge[i+1],edge[i]+numVerts]
                # t2 = [edge[i],edge[i]+numVerts,edge[i+1]+numVerts]
                # t1 = [edge[i],edge[i+1],edge[i]+len(edge)]
                # t2 = [edge[i],edge[i]+len(edge),edge[i+1]+len(edge)]

                t1 = [edge[i], edge[i + 1], edge[i] + numVerts]
                t2 = [edge[i + 1], edge[i] + numVerts, edge[i + 1] + numVerts]

                T.append(t1)
                T.append(t2)

#--------------------------------------------------------------------------------------------------------------------------------------------------#
# Export stl
        newA = trimesh.Trimesh(A.vertices, A.faces)

        newA.fix_normals()

        fileName1 = os.getcwd().split(os.sep)[-1]

        newA.export(file_obj='newA_' +
                    fileName1 + '.stl', file_type='stl')

        newB = trimesh.Trimesh(B.vertices, B.faces)

        fileName2 = os.getcwd().split(os.sep)[-1]

        newB.fix_normals()

        newB.export(file_obj='newB_' +
                    fileName2 + '.stl', file_type='stl')

        Q = np.concatenate((newA.vertices, newB.vertices), axis=0)

        newBoundary = trimesh.Trimesh(Q, T)

        newBoundary.fix_normals()

        # newBoundary.fill_holes()

        newBoundary.export(file_obj='newBoundary_' +
                           fileName2 + '.stl', file_type='stl')

        finalmesh = newA + newB + newB

        finalmesh.export(file_obj='final_' +
                         fileName2 + '.stl', file_type='stl')

        #  python3 solidify.py && ~/stlviewer/./stlviewer final_whitney.stl

        # mesh1 = trimesh.load('newA_whitney.stl')

        # mesh2 = trimesh.load('newB_whitney.stl')
        # final = trimesh.load('final_whitney.stl')
        # final.show()
        # mesh1.show()

        # (mesh2).show()

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
