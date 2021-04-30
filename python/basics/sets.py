# sets are unordered collections
set = {1.0, 10, 'String', (1, 0, 1, 0)}
print(set)
# {(1, 0, 1, 0), 1.0, 10, 'String'}

print('String' in set)                  # True
print('Java' in set)                    # False

# add to set
set.add('Python')
print(set)
# {1.0, 'String', (1, 0, 1, 0), 10, 'Python'}

# remove from set
set.remove('Python')
print(set)
# {1.0, 'String', (1, 0, 1, 0), 10}

# set operations
set_one = {1, 2, 3}
set_two = {3, 4, 5}

print(set_one | set_two)                # {1, 2, 3, 4, 5}   (Union)
print(set_one & set_two)                # {3}               (Intersection)
print(set_one - set_two)                # {1, 2}            (Difference)
print(set_one ^ set_two)                # {1, 2, 4, 5}      (Symmetric difference)

# subset and superset
set_a = {1, 2}
set_b = {1, 2}
set_c = {1, 2, 3, 4, 5}

print(set_a < set_b)                    # False             (Strict subset)
print(set_a <= set_b)                   # True              (Subset)
print(set_c > set_a)                    # True              (Strict superset)