# A tuple is a sequence of immutable Python objects. Tuples are sequences, just like lists.

tup1 = (1, 'Physics', 'Chemistry', 1197)

# Accessing the value from Tuple
print(tup1[0])

# Updating is Not possible in tuples
# Instead we can use the concate operation and assign it to new var
tup2 = (1, 2, 3) + (2, 34, 512)
print(tup2)

# Deleting the tuple elements is also not possible only we can delete the entire tuple
del tup1
print(tup1)

"""Basic Operations in the Tuple are 
Length of list=len()
concatenation of list= we use (+) operator
Repetition of same value in list = ('Hi')*4==>('Hi','Hi','Hi','Hi')
Membership using (in) operator 4 in list1==>True
Iteration using for loop
"""
