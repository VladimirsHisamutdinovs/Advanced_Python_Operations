# https://www.programiz.com/python-programming/shallow-deep-copy

# Copying of an object in Python
list_one = [[1, 2, 3], [4, 5, 6], [7, 8, 'x']]
list_two = list_one

list_two[2][2] = 9

print('List One:', list_one)
print('ID of List One:', id(list_one))

print('List Two:', list_two)
print('ID of List Two:', id(list_two))

# Import Copy module

import copy

# copy --> copy() - for a shallow copy
# copy --> deepcopy() - for a deep copy

# Shallow Copy

list_one = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
list_two = copy.copy(list_one)

print('List One:', list_one)
print('List Two:', list_two)

# Adding new nested object using Shallow copy:

# list_one = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# list_two = copy.copy(list_one)

list_two[2][2] = '10'

print('List One:', list_one)
print('List Two:', list_two)

# Deep Copy

deep_list_one = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
deep_list_two = copy.deepcopy(deep_list_one)

print('Deep List One:', deep_list_one)
print('Deep List Two:', deep_list_two)

# Adding new nested object using Deep copy:

#deep_list_one = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#deep_list_two = copy.deepcopy(deep_list_one)

deep_list_two[2][2] = '10'

print('Deep List One:', deep_list_one)
print('Deep List Two:', deep_list_two)

