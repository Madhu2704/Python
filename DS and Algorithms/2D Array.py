"""
Two dimensional array is an array within an array.
It is an array of arrays.
In this type of array the position of an data element is referred by two indices instead of one.
So it represents a table with rows an dcolumns of data.
In the below example of a two dimensional array,
    observer that each array element itself is also an array.
"""

Day_wise_reports = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print(Day_wise_reports)

# Accessing the Values
print(Day_wise_reports[2])
print(Day_wise_reports[0][2])

for r in Day_wise_reports:
    for c in r:
        print(c, end=" ")
    print()

# insertion
Day_wise_reports.insert(2, [13, 14, 15, 16])
print(Day_wise_reports)

# Updation
Day_wise_reports[3] = [11, 19]
Day_wise_reports[0][3] = 7


#Deletion of 2D Array

del Day_wise_reports[3]
print(Day_wise_reports)
