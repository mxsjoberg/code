# tuples are immutable
tuple_one = (1.0, 'String', 4)
tuple_two = ('Alpha', 'Bravo', (1, 0))

tuple_one                           # (1.0, 'String', 4)
tuple_two                           # ('Alpha', 'Bravo', (1, 0))
tuple_two[2][1]                     # 0

# concatenate tuples
tuple = tuple_one + tuple_two
# (1.0, 'String', 4, 'Alpha', 'Bravo', (1, 0))

# create tuple from a list
tuple_list = tuple([100, 'B'])
# (100, 'B')