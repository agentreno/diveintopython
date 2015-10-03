# coding: utf-8
a_set = {1}

# Create a set out of a list
set([1,1,1])

# Sets are unordered
set([1,'a',2,'b'])

# New empty set using set() not {}
type({})

# Add item
a_set.add(2)

# Add from another set
a_set.update({3,4,5})

# Delete set item (no error if doesn't exist)
a_set.discard(6)

# Delete set item (error if doesn't exist)
a_set.remove(1)

# Pop items
a_set.pop()

# Clear a set
a_set.clear()

a_set1 = {1,2,3}
a_set2 = {3,4,5}

# Unions, intersections, differences (in a not b)
a_set1.union(a_set2)
a_set1.intersection(a_set2)
a_set1.difference(a_set2)

# Symmetric difference (in a or b but not both)
a_set1.symmetric_difference(a_set2)

# Subsets and supersets
a_set1.issubset(a_set2)
a_set1.issuperset(a_set2)
