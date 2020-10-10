string = 'proton neutron'
string[:]                               # proton neutron
string[:2]                              # pr
string[-2:]                             # on
string[1:3]                             # ro

# reverse a string
string[::-1]                            # notorp

# skip every second character
string[0:-1:2]                          # poo

# built-ins
string.capitalize()                     # Proton neutron
string.title()                          # Proton Neutron
string.upper()                          # PROTON NEUTRON
string.lower()                          # proton neutron
string.center(20, '.')                  # ...proton neutron...

# conditionals
string.isdigit()                        # False
string.islower()                        # True
string.isupper()                        # False

# counting and finding letters in text
string.count('p', 0, len(string))       # 1
string.find('t', 1, len(string))        # 3

# removing whitespace from a string
string = '    some text    '
string.lstrip()                         # 'some text    '
string.rstrip()                         # '    some text'
string.strip()                          # 'some text'