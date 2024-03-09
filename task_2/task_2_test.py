import numpy as np
from task2 import time_taken, arr,byte_arr,recreated_arr

def test_time():
    assert isinstance(time_taken,float)

def compare_arrays():
    assert arr.all() == recreated_arr.all()

def test_shape():
    assert arr.shape ==(1000,1000)
    assert recreated_arr.shape == arr.shape

def test_type():
    assert arr.dtype == np.float64
    assert recreated_arr.dtype == np.float64
    assert isinstance(byte_arr,bytes) == True

