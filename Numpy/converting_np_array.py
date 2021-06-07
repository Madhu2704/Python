import numpy as np
"""
The best way to change the data type of an existing array,
 is to make a copy of the array with the astype() method.
"""
arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype('i')
print(newarr)
print(newarr.dtype)

newarr = arr.astype(bool)
print(newarr)
print(newarr.dtype)
