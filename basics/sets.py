# sets are unordered collections
set = {1.0, 10, 'String', (1, 0, 1, 0)}
set                     # set([(1, 0, 1, 0), 10, 'String', 1.0])

'String' in set         # True
'Java' in set           # False

# add to set
set.add('Python')       # set(['Python', (1, 0, 1, 0), 10, 'String', 1.0])

# remove from set
set.remove('Python')    # set([(1, 0, 1, 0), 10, 'String', 1.0])

# set operations
set_one = {1, 2, 3}     # set([1, 2, 3])
set_two = {3, 4, 5}     # set([3, 4, 5])

set_one | set_two       # set([1, 2, 3, 4, 5])      (Union)
set_one & set_two       # set([3])                  (Intersection)
set_one - set_two       # set([1, 2])               (Difference)
set_one ^ set_two       # set([1, 2, 4, 5])         (Symmetric difference)

# subset and superset
set_a = {1, 2}
set_b = {1, 2}
set_c = {1, 2, 3, 4, 5}

set_a < set_b           # False                     (Strict subset)
set_a <= set_b          # True                      (Subset)
set_c > set_a           # True                      (Strict superset)

'''
Michael Sjoeberg
2018-11-05
https://github.com/michaelsjoeberg/python-playground/blob/master/basics/sets.py
'''