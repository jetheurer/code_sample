'''
This module contains tests for the methods in the volumepy file
'''

import numpy as np
import os
from volume.volume import volume_polygon

TOLERANCE = 1e10


def filepath(filename):
    '''
    returns the explict path of the file
    '''
    dir_path = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(dir_path, 'examples', filename)


def test_unit_cube():
    '''Tests that the volume of a unit cube is 1'''
    path = filepath('unit_cube_qppp.npy')
    data = np.load(path)
    vol = volume_polygon(data)
    assert np.isclose(vol, 1.0, atol=TOLERANCE)


def test_unit_square():
    '''Tests that the volume of a unit square is 0'''
    path = filepath('unit_sq.npy')
    data = np.load(path)
    vol = volume_polygon(data)
    assert np.isclose(vol, 0.0, atol=TOLERANCE)


def test_robot():
    '''Tests that the volume of the Robot is 43677.4'''
    path = filepath('Robot_Maker_Faire_65pc.npy')
    data = np.load(path)
    vol = volume_polygon(data)
    assert np.isclose(vol, 43677.42582662092, atol=TOLERANCE)


def test_shell():
    '''Tests that the volume of the shell is 3.66'''
    path = filepath('shell.npy')
    data = np.load(path)
    vol = volume_polygon(data)
    assert np.isclose(vol, 3.6586764273115655, atol=TOLERANCE)
