# coding: utf-8
a_tuple = (1,2,3)
print("Immutable tuple: " + str(a_tuple))
def is_it_true(anything):
    if anything:
        print("True")
    else:
        print("False")
        
print("Empty tuple is false")
is_it_true(tuple())
is_it_true(a_tuple)
print("Fill variables in one go")
(a,b,c) = (1,2,3)
a
b
c
