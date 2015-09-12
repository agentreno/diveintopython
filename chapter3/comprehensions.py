# coding: utf-8
a_list = [1,2,3]
[elem * 2 for elem in a_list]
print("Safe to assign to var used in comprehension")
a_list = [elem * 2 for elem in a_list]
a_list
[elem for elem in a_list if elem > 2]
import os
import glob
pysizes = {f : os.stat(f).st_size for f in glob.glob('*.py')}
print(pysizes)
print("Swapping keys and values in a dict")
a_dict
a_dict = {value : key for key, value in a_dict.items()}
a_dict
a_set = set(range(10))
a_set
{x ** 2 for x in a_set}
{x for x in a_set if x % 2 == 0}
{2**x for x in range(10)}
