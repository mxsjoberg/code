# dictionaries are hash tables, key:value pairs
dict = {'Adam': ['adam@email.com', 2445055],
        'Bard': 'bard@email.com'}

dict                    # {'Adam': ['adam@email.com', 2445055], 'Bard': 'bard@email.com'}
dict['Adam']            # ['adam@email.com', 2445055]
dict['Adam'][1]         # 2445055

# update value
dict['Bard'] = 'bard@anotheremail.com'
dict                    # {'Adam': ['adam@email.com', 2445055], 'Bard': 'bard@anotheremail.com'}

# add key:value pair
dict['Cole'] = 'cole@email.com'
dict                    # {'Cole': 'cole@email.com', 'Adam': ['adam@email.com', 2445055], 'Bard': 'bard@anotheremail.com'}

# remove key:value pair
del dict['Cole']        # {'Adam': ['adam@email.com', 2445055], 'Bard': 'bard@anotheremail.com'}

'Cole' in dict          # False
'Adam' in dict          # True

# create dictionary from a list of tuples
dict_list_tuples = dict([(1, "x"), (2, "y"), (3, "z")])
dict_list_tuples
# {1: 'x', 2: 'y', 3: 'z'}