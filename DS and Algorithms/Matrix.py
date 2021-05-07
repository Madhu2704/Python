# Matrix is a special case of two dimensional
# array where each data element is of strictly same size
from numpy import *


def log(msg=""):
    print(f"-----------------{msg}-----------------------")


matrix_array = array([['Monday', 1, 2, 3],
                      ['Tuesday', 4, 5, 6],
                      ['Wednesday', 7, 8, 9]])

# print(matrix_array)
m = reshape(matrix_array, (3, 4))
print(m)
log("Accessing the Values")
# Accessing the Values
print(m[2])
print(m[2][3])
log("Adding a row in Matrix")
# Adding a row in Matrix
m_r = append(m, [['Thrusday', 10, 11, 12]], 0)
print(m_r)
log("Adding a Column")
# Adding a Column
m_c = insert(m, [4], [[1], [2], [3]], 1)
print(m_c)
log("Delete a row")
# Delete a row
m = delete(m, [1], 0)
print(m)
log("Delete a Column")
# Delete a Column
m = delete(m, [2], 1)
print(m)
log("updating a row")
# updating a row
m[1] = ['Friday', 0, 0]
print(m)
