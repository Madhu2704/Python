"""
set is a collection of items not in any particular order.
The elements in the set are immutable(cannot be modified) but the set as a whole is mutable.
There is no index attached to any element in a python set.
So they do not support any indexing or slicing operation.
"""


def log(msg=""):
    print(f"-----------------{msg}-----------------------")


Days = set(['Mon', 'Tues', 'Wed', "Thru", "Fri", "Sat", "Sun"])
Months = {"Jan", "Feb", "Mar"}
Dates = {21, 22, 23}
log("printing the sets")
print(Days)
print(Months)
print(Dates)
log()

log("Accessing Individual values")
for day in Days:
    print(day)
log()

log("Add items to the set")
Dates.add(24)
print(Dates)
log()

log("Remove Items From Sets")
Dates.discard(22)
print(Dates)
log()

log("Union of two sets")
a = {1, 2, 34, 44, 55}
b = {5, 3, 4, 5, 22, 33, 44, 55}
print(a | b)
log()

log("Intersection of 2 sets")
print(a & b)
log()

log("Difference of two sets")
print(a - b)
log()

log("Checking a is subset or superset of b")
print(a <= b)
print(a >= b)
