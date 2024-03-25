# Task 2

# Create a 1000 x 1000 random numpy array
# Measure how long the creation takes
# Convert the array into bytes
# Recreate the array from the bytes

# References:
# time package
# numpy package
# np.frombuffer

import numpy as np
import time

t1 = time.time()
arr = np.random.randn(1000, 1000)
t2 = time.time()
time_taken = t2 - t1
print("Time Taken =", time_taken)
print("Random array : ", arr[0][:10])
byte_arr = arr.tobytes()
print("Byte array = ", byte_arr[:10])

arr_type = arr.dtype
recreated_arr = np.frombuffer(byte_arr, dtype=arr_type).reshape(1000, 1000)
print("Recreated array :", recreated_arr[0][:10])
