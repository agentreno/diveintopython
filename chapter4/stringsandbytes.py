# coding: utf-8

# String formatting
a_string = "this is a {0}".format('string')
print(a_string)
type(a_string)
print('format can index lists: {0[0]}'.format(['a','b']))
print("and dictionaries: {0[a]}".format({'a':1,'b':2}))
print("format can process integers: {0:.1f}".format(0.11111))

# Multi-line string includes newlines
"""
A line
Another line
"""

# Common string operations
"a line\nanotherline".splitlines()
"NOTCAPS".lower()
"count a character".count('c')
"split.on.dots".split('.')
"split.on.first.dot.only".split('.',1)
"slice a string"[6:]
"slice a string"[:6]
"slice a string"[6:-3]

# Strings are sequences of unicode points, not bytes
type('abc')
type(b'abc')

# Bytes can be ASCII characters or byte values only
type(b'abc\xff')

# Bytes are immutable
try:
    b'abc'[0] = '\xff'
except:
    print("Exception!")
    
# Bytearrays are mutable
some_bytes = b'abc'
some_bytes[0]
a_bytearray = bytearray(some_bytes)
a_bytearray[0]
a_bytearray[0] = 255

# Strings become bytes when encoded, vice versa
"abc".encode('utf-8')
"abc".encode('utf-16')
b'\xff\xfea\x00b\x00c\x00'.decode('utf-16')
