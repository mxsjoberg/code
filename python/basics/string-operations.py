string = 'proton neutron'
string.capitalize()         # Proton neutron
string.title()              # Proton Neutron
string.upper()              # PROTON NEUTRON
string.lower()              # proton neutron
string.center(20, '.')      # ...proton neutron...

# conditionals
string.isdigit()            # False
string.islower()            # True
string.isupper()            # False

# counting and finding letters in text
string.count('p', 0, len(string))       # 1
string.find('t', 1, len(string))        # 3

# removing whitespace from a string
string = '    some text    '
string.lstrip()                         # 'some text    '
string.rstrip()                         # '    some text'
string.strip()                          # 'some text'

'''
Michael Sjoeberg
2018-11-05
https://github.com/michaelsjoeberg/python-playground/blob/master/basics/string-operations.py
'''