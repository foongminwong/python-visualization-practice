    def fvtostl(self):

        def extract_points(data):
            """Extract points from vertices"""

            points = []

            for vertex in data.vertices:
                """ we use 3 here because a triangle consists
                of three points """
                point = [None]*3

                for j in range(3):
                    point[j] = vertex['point'][j].real
                points.append(point)
            return points

        data = self.decomposition
        points = extract_points(data)
        faces = self.decomposition.surface.surface_sampler_data
       
        # add vertex and surface to mesh
        vertex = []
        
        for p in points:
            vertex.append(p)

        vertex_np_array = np.array(vertex)

        face = []

        for f in faces: # for each face
            for tri in f: # for triangle in face
                face.append([tri[0],tri[1],tri[2]])

        face_np_array = np.array(face)
 
        obj = mesh.Mesh(np.zeros(face_np_array.shape[0], dtype=mesh.Mesh.dtype))

        for i, f in enumerate(face_np_array):
            for j in range(3):
                obj.vectors[i][j] = vertex_np_array[f[j],:]

        # get object filename
        fileName = os.getcwd().split(os.sep)[-1]

        obj.save('a' + fileName + '.stl')

        normmesh = trimesh.load_mesh('a' + fileName + '.stl')

        normmesh.fix_normals()

        for facet in normmesh.facets:
            normmesh.visual.face_colors[facet] = trimesh.visual.random_color()

        # normmesh.show()
        
        normmesh.export(file_obj='anorm' + fileName + '.stl', file_type='stl')
        print('Export STL successfully!')


def fvtostl(data=None):
    surface = GlumpyPlotter(data)
    surface.fvtostl()