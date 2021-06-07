import numpy as np

"""
We pass slice instead of index like this: [start:end].

We can also define the step, like this: [start:end:step].

If we don't pass start its considered 0

If we don't pass end its considered length of array in that dimension

If we don't pass step its considered 1
"""


def log(msg=None):
    print("-------------------------------------------")
    print(msg)


numpy_array_1D = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
numpy_array_2D = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
numpy_array_3D = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

log(numpy_array_1D[1:])
log(numpy_array_1D[:7])
log(numpy_array_1D[1::2])


log(numpy_array_2D[0, 1:])

log(numpy_array_2D[0:2, 1:2])
