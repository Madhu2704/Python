
import numpy as np


def log(msg=None):
    print("-------------------------------------------")
    print(msg)


numpy_array_1D = np.array([1, 2, 3, 4])
numpy_array_2D = np.array([[1, 2, 3], [4, 5, 6]])
numpy_array_3D = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
log(numpy_array_1D[0])
log(numpy_array_2D[0, 2])
log(numpy_array_3D[0, 1, 1])


# negative Indexing
log('##Negative Indexing')
log(numpy_array_3D[0, 1, -1])
