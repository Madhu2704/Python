"""
In Dictionary each key is separated from its value by a colon (:),
the items are separated by commas,
and the whole thing is enclosed in curly braces
"""

empty_dictionary_ele = {}

dictionary_ele = {'name': 'Madhu prakash', 'age': 24}

# Accessing the value from the dictionary
print(dictionary_ele['age'])

# Updating Dictionary
dictionary_ele['age'] = 45

#Delete the Dictionary Elements

# Removes entry with 'name'
del dictionary_ele['name']

# Clears all the entires in dict
dictionary_ele.clear()

# delete entire dictionary
del dictionary_ele



"""
 More than one entry per key not allowed. Which means no duplicate key is allowed. 
 When duplicate keys encountered during assignment, the last assignment wins. 
"""