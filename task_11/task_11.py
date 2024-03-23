# Task 11

# Use multiprocessing to fill random values in a large numpy array.

# References:
# multiprocessing.shared_memory.SharedMemory
# concurrent.futures.ProcessPoolExecutor

# Read about:
# Python Global Interpreter Lock (GIL)
# Multiprocessing start methods: spawn, fork, forkserver

from multiprocessing import shared_memory
from concurrent.futures import ProcessPoolExecutor
import numpy as np


def fill_arr(sm_name,shape,slice):
    start = slice.start
    end = slice.stop
    len = end - start
    sm = shared_memory.SharedMemory(name=sm_name)
    arr = np.ndarray(shape,dtype=np.int16,buffer=sm.buf)
    arr[slice] = np.random.randint(0,100,len,dtype=np.int16)
    sm.close()

def runProcesses(size,p,sm_name="shared_arr"):
    chunks = size // p
    shape = (size,)
    arr = np.zeros(shape,dtype=np.int16)
    shared_arr= shared_memory.SharedMemory(name=sm_name, size=arr.nbytes,create=True)
    arr = np.ndarray(shape,dtype=arr.dtype,buffer=shared_arr.buf)
    futures = []
    with ProcessPoolExecutor(max_workers=p) as executor:
        for i in range(0,size,chunks):
            start = i
            end = i+chunks if i+chunks<size else size
            futures.append(executor.submit(fill_arr,sm_name,shape,slice(start,end)))
    for future in futures:
        future.result()
    print(arr)
    shared_arr.close()
    shared_arr.unlink()
    

if __name__ == "__main__":
    size = int(input("Enter the size of the array: "))
    p =int(input("Enter the number of processes: "))
    runProcesses(size,p)
    
