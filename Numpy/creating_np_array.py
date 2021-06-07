"""
NumPy is used to work with arrays. The array object in NumPy is called ndarray.
We can create a NumPy ndarray object by using the array() function.
To create an ndarray, we can pass a list,
 tuple or any array-like object into the array() method, 
 and it will be converted into an ndarray:
"""
import numpy as np

# list
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))

# tuples
arr = np.array((1, 2, 3, 4, 5))
print(arr)
print(type(arr))
