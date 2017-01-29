'''
This module takes a .npy file of triangular faces of an object and returns the volume of the object.
'''
from __future__ import division
import argparse
import logging
import numpy as np
log = logging.getLogger(__name__)


def _volume_tetrahedral(vertices):
    '''
    This function takes 3 points in x, y, z space and computes the volume of a tetrahedron.

    Args:
        vertices (:obj:`list` of :obj:`list`): List of 3 vertices of a triangles in x, y, z space

    Returns:
        float: volume of a tetrahedron with 3 vertex at the origin

    Examples:
        >>> vertices = [[0,0,1],[0,1,1],[0,1,0]]
        >>> _volume_tetrahedral(vertices)
        0.0

        >>> import numpy as np
        >>> vertices = np.array([[ 1,  0,  0], [ 1,  1,  1], [ 1,  0,  1]])
        >>> _volume_tetrahedral(vertices)
        0.16666666666666666
    '''
    assert [len(i) == 3 for i in vertices]  # validate that each point is in x,y,z space
    assert len(vertices) == 3  # assert that there are 3 vector
    a, b, c = vertices
    return np.dot(np.cross(a, b), c) / 6


def volume_mesh(array):
    '''
    This function takes a mesh (list of 3 points in x, y, z space) and computes the total volume of the mesh.

    Args:
        array (:obj:`list` of :obj:`list` of :obj:`list`): List of 3 vertices of a triangles in x, y, z space

    Returns:
        float: volume the mesh
    '''
    return sum(_volume_tetrahedral(triangle) for triangle in array)


if __name__ == '__main__':
    '''allows the user to run this module from the command line'''
    parser = argparse.ArgumentParser(description="calculate the volume of a stl file")
    parser.add_argument("-f", "--filename", required=True, help="path of STL file to process",
                        type=str)
    args = parser.parse_args()
    array = np.load(args.filename)
    print volume_mesh(array)
