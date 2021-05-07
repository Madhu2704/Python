from array import *

# array(type_code,[initial_elements])
sequence_of_numbers = array('i', [10, 20, 30, 40])
# Traverse of Array
for number in sequence_of_numbers:
    print(number)

# Accessing the Elements
print(sequence_of_numbers[3])

# Inserting New Values
# array.insert(index,value)
# Insert will not over write the values it shifts the values to  next indexes
print(sequence_of_numbers.insert(1, 80))
print(sequence_of_numbers.insert(4, 80))
print(sequence_of_numbers)

# Remove of element (only the first occurence)
sequence_of_numbers.remove(80)
print(sequence_of_numbers)

# searching basing on the value
# returns back the index if the value is present in the  array
print(sequence_of_numbers.index(10))
#If value is not present it throughs the error(array.index(x): x not in array)
print(sequence_of_numbers.index(90))

# Updating (If want to over write the value in a particular index)
sequence_of_numbers[1] = 455
print(sequence_of_numbers)
