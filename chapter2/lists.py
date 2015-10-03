# coding: utf-8
a_list = ['a', 1, 'b', 2]
a_list[0]
print(a_list)

# First two elements 
a_list[:2]

# Last two elements
a_list[-2:]

# Missing left slice index is implicitly 0, missing right slice index is 
# implicitly the length of the list.")
print("e.g. a_list[:] = " + str(a_list[:]))
print("List concatenation temporarily creates another list in memory: [1] + [2] = " + str([1] + [2]))

# Append another item:
a_list.append('c')

# Extend a list with another list
a_list.extend([3])

# Insert an item at a specific position
a_list.insert(0, 'z')

# Count elements
a_list.count('z')

# Determine membership
'e' in a_list

# Find index of an item
a_list.index('z')

# Delete by index
del a_list[0]

# Delete by item
a_list.remove('a')

# Pop items by index(defaults to last element)
a_list.pop(0)

# Find non-existent element raises exception
a_list.index('banana')
