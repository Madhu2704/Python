# Lists are same as Array but Items in list need not be the same type
# Lists are Mutable and Can be updated after Intializing
list1 = ['physics', 1, 2, 3.4, 5]

# Accessing the Elements in the List
print(list1[3])

# Updating or Overwriting the Value in list
list1[3] = 55
print(list1)

# Delete the Value from List(Need to mention the index of the element to remove)
del list1[3]
print(list1)

"""Basic Operations in the List are 
Length of list=len()
concatenation of list= we use (+) operator
Repetition of same value in list = ['Hi']*4==>['Hi','Hi','Hi','Hi']
Membership using (in) operator 4 in list1==>True
Iteration using for loop
"""
