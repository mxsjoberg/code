# dictionaries are hash tables, key:value pairs
dct = {
    'Adam': ['adam@email.com', 2445055],
    'Bard': 'bard@email.com'
}

print(dct)                              # {'Adam': ['adam@email.com', 2445055], 'Bard': 'bard@email.com'}
print(dct['Adam'])                      # ['adam@email.com', 2445055]
print(dct['Adam'][1])                   # 2445055

# update value
dct['Bard'] = 'bard@anotheremail.com'
print(dct)
# {'Adam': ['adam@email.com', 2445055], 'Bard': 'bard@anotheremail.com'}

# add key:value pair
dct['Cole'] = 'cole@email.com'
print(dct)
# {'Adam': ['adam@email.com', 2445055], 'Bard': 'bard@anotheremail.com', 'Cole': 'cole@email.com'}

# remove key:value pair
del dct['Cole']

print('Cole' in dct)                    # False
print('Adam' in dct)                    # True

# create dictionary from a list of tuples
dct_list_tuples = dict([(1, "x"), (2, "y"), (3, "z")])
print(dct_list_tuples)
# {1: 'x', 2: 'y', 3: 'z'}