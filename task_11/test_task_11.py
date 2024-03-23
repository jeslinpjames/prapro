from task_11 import runProcesses, fill_arr
import numpy as np
import pytest
from multiprocessing import shared_memory


def test_runProcesses():
    sm_name = "test_shared_memory"
    size = 1000
    p = 10

    arr = runProcesses(size, p, sm_name)

    assert arr.shape == (size,)
    assert arr.dtype == np.int16
    assert np.all(arr >= 0) and np.all(arr < 100)


def test_fill_arr():
    sm_name = "test_shared_memory"
    size = 10
    shape = (size,)
    shared_arr = shared_memory.SharedMemory(
        name=sm_name, size=shape[0] * np.dtype(np.int16).itemsize, create=True
    )
    arr = np.ndarray(shape, dtype=np.int16, buffer=shared_arr.buf)
    arr.fill(0)

    # Test filling the entire array
    fill_arr(sm_name, shape, slice(0, size))
    assert np.all(arr >= 0) and np.all(arr < 100)

    # Test filling a subset of the array
    arr.fill(0)
    fill_arr(sm_name, shape, slice(2, 6))
    assert np.all(arr[:2] == 0) and np.all(arr[6:] == 0)
    assert np.all(arr[2:6] >= 0) and np.all(arr[2:6] < 100)

    shared_arr.close()
    shared_arr.unlink()
