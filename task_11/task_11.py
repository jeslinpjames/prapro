# Task 11

# Use multiprocessing to fill random values in a large numpy array.

# References:
# multiprocessing.shared_memory.SharedMemory
# concurrent.futures.ProcessPoolExecutor

# Read about:
# Python Global Interpreter Lock (GIL)
# Multiprocessing start methods: spawn, fork, forkserver

import multiprocessing.shared_memory.SharedMemory 
import concurrent.futures.ProcessPoolExecutor
import numpy as np


def fill_arr(slice):
    start = slice.start
    end = slice.stop
    len = end - start
    arr[start:end] =np.random.randint(0,100,len)


