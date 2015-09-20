# coding: utf-8
a_dict = {'a':1, 'b':2}
a_dict['c'] = 3
len(a_dict)
'a' in a_dict
a_refdict = a_dict
a_refdict['d'] = 4
print("Assignment doesn't copy dictionaries: " + str(a_dict))
import copy
a_copydict = copy.copy(a_refdict)
del a_refdict['d']
print("But the copy module can copy dictionaries: " + str(a_copydict))
print("Correctly formatted lists can be dicts:")
dict([ ['a', 1], ['b', 2] ])
