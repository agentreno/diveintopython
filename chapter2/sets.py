# coding: utf-8
a_set = {1}
print("Create a set out of a list: set([1,1,1]) = " + str(set([1,1,1])))
print("Sets are unordered: set([1,'a',2,'b']) = " + str(set([1,'a',2,'b'])))
print("New empty set using set() not {}: type({}) = " + str(type({})))
print("Add to set: a_set.add(2)")
a_set.add(2)
print("Add other set elements to a set: a_set.update({3,4,5})")
a_set.update({3,4,5})
print("Silently delete set item if item doesn't exist: a_set.discard(6)")
a_set.discard(6)
print("Delete set item, error if item doesn't exist: a_set.remove(1)")
a_set.remove(1)
print("Pop items from set: a_set.pop()")
a_set.pop()
print("Clear a set: a_set.clear()")
a_set.clear()
a_set1 = {1,2,3}
a_set2 = {3,4,5}
a_set1 
a_set2
print("a_set1.union(a_set2) = " + str(a_set1.union(a_set2)))
print("a_set1.intersection(a_set2) = " + str(a_set1.intersection(a_set2)))
print("a_set1.difference(a_set2) = " + str(a_set1.difference(a_set2)))
print("a_set1.symmetric_difference(a_set2) = " + str(a_set1.symmetric_difference(a_set2)))
print("a_set1.issubset(a_set2) = " + str(a_set1.issubset(a_set2)))
print("a_set1.issuperset(a_set2) = " + str(a_set1.issuperset(a_set2)))
