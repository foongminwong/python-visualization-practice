    def test(self):

        stl = "mystl.stl"
        tmesh = trimesh.load(str(stl))
        # print(tmesh.vertices)
        print(tmesh.faces)
        points = extract_points(self)

        faces = self.decomposition.surface.surface_sampler_data
        list_of_tuples_faces = faces[0]
        list_of_lists_faces = [list(elem) for elem in list_of_tuples_faces]

        # print(list_of_lists_faces)

        obj = trimesh.Trimesh(points, faces)

        fileName = os.getcwd().split(os.sep)[-1]

        obj.fix_normals()

        obj.export(file_obj='testsmooth_' +
                        fileName + '.stl', file_type='stl')

        print("Export " + '\x1b[0;35;40m' + "testsmooth" +
              fileName + ".stl" + '\x1b[0m' + " successfully")
        # print(points)
        # print(list_of_lists_faces)
        # nested_lst_of_tuples = [tuple(l) for l in tmesh.faces]
        # print([nested_lst_of_tuples])def test(data=None):
        



def test(data=None):
    surface = NumpySTL(data)
    surface.test()
