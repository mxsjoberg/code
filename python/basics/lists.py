# lists are mutable
list_one = ['REMOVE', 'RANDOM']
list_two = [200, -2, [1.0, 0.0]]

list_one[0] = 'ADD'                 # ['ADD', 'RANDOM']
list_one[1]                         # RANDOM
len(list_one)                       # 2
len(list_two)                       # 3

# concatenate lists
list = list_one + list_two          # ['ADD', 'RANDOM', 200, -2, [1.0, 0.0]]

# list operations
list.append('NULL')                 # ['ADD', 'RANDOM', 200, -2, [1.0, 0.0], 'NULL']
list.sort()                         # [-2, 200, [1.0, 0.0], 'ADD', 'NULL', 'RANDOM']

# create list from a string
list_string = list('100B')          # ['1', '0', '0', 'B']

'''
Michael Sjoeberg
2018-11-05
https://github.com/michaelsjoeberg/python-playground/blob/master/basics/lists.py
'''