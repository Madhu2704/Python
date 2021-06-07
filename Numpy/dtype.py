import numpy as np


def log(msg=None):
    print("-------------------------------------------")
    print(msg)


arr = np.array([1, 2, 3, 4])
log(arr.dtype)

arr = np.array(['apple', 'banana', 'cherry'])
log(arr.dtype)

# creating array with dtype
arr = np.array([1, 2, 3, 4], dtype='S')

print(arr)
print(arr.dtype)
