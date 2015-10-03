# coding: utf-8

# Basic list comprehension
a_list = [1,2,3]
[elem * 2 for elem in a_list]

# Safe to assign to var used in comprehension
a_list = [elem * 2 for elem in a_list]
a_list

# Comprehension with a filter
[elem for elem in a_list if elem > 2]
import os
import glob

# Dictionary comprehension
pysizes = {f : os.stat(f).st_size for f in glob.glob('*.py')}
print(pysizes)

# Swapping keys and values in a dict
a_dict
a_dict = {value : key for key, value in a_dict.items()}
a_dict

# Set comprehensions
a_set = set(range(10))
a_set
{x ** 2 for x in a_set}
{x for x in a_set if x % 2 == 0}
{2**x for x in range(10)}
