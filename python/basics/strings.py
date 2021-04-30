string = 'proton neutron'

print(string[:])                            # proton neutron
print(string[:2])                           # pr
print(string[-2:])                          # on
print(string[1:3])                          # ro

# reverse a string
print(string[::-1])
# notorp

# skip every second character
print(string[0:-1:2])
# poo

# built-ins
print(string.capitalize())                  # Proton neutron
print(string.title())                       # Proton Neutron
print(string.upper())                       # PROTON NEUTRON
print(string.lower())                       # proton neutron
print(string.center(20, '.'))               # ...proton neutron...

# conditionals
print(string.isdigit())                     # False
print(string.islower())                     # True
print(string.isupper())                     # False

# counting and finding letters in text
print(string.count('p', 0, len(string)))    # 1
print(string.find('t', 1, len(string)))     # 3

# removing whitespace from string
string = '    some text    '

print(string.lstrip())                      # 'some text    '
print(string.rstrip())                      # '    some text'
print(string.strip())                       # 'some text'