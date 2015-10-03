import re
s = '100 BROAD ROAD APT. 3'
# Raw strings don't have any escape chars:
print(r"re.sub substitutes, \b is a word boundary")
print(re.sub(r'\bROAD\b', 'RD.', s))

# Compact regular expression for roman numeral validity
pattern = """
   ^                 # beginning of string
   M{0,3}            # thousands - 0 to 3 Ms
   (CM|CD|D?C{0,3})  # hundreds - 900 (CM), 400 (CD), 0-300 (0-3 Cs),
                     #  or 500-800 (D, followed by 0-3 Cs)
   (XC|XL|L?X{0,3})  # tens - 90 (XC), 40 (XL), 0-30 (0-3 Cs),
                     #  or 50-80 (L, followed by 0-3 Xs)
   (IX|IV|V?I{0,3})  # ones - 9 (IX), 4 (IV), 0-3 (0-3 Is),
                     #  or 5-8 (V, followed by 0-3 Is)
   $                 # end of string
   """

print(re.search(pattern, 'MMMDCCCLXXXVIII', re.VERBOSE))

# Compact regular expression for US phone number capturing
phonePattern = re.compile(r"""
                     # don't match beginning of string to allow prefixes
   (\d{3})           # area code is 3 digits
   \D*               # optional separator (* is 0 or more, \D non-digit)
   (\d{3})           # trunk is 3 digits
   \D*               # optional separator
   (\d{4})           # rest of number is 4 digits
   \D*               # optional separator
   (\d*)             # optional extension number any length
   $                 # end of string
   """, re.VERBOSE)
print(phonePattern.search("work 1-(800) 555.1212 #1234").groups())
print(phonePattern.search("800-555-1212"))
