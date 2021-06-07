# ndim Object tells us the dimension of the array(0D,1D,2D,3D)etc
import numpy as np


def log(msg=None):
    print("-------------------------------------------")
    print(msg)


numpy_array_0D = np.array(42)
numpy_array_1D = np.array([1, 2, 3, 4])
numpy_array_2D = np.array([[1, 2, 3], [4, 5, 6]])
numpy_array_3D = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

log(numpy_array_0D.ndim)
log(numpy_array_1D.ndim)
log(numpy_array_2D.ndim)
log(numpy_array_3D.ndim)
