# tuples are immutable
tuple_one = (1.0, 'String', 4)
tuple_two = ('Alpha', 'Bravo', (1, 0))

print(tuple_one)                            # (1.0, 'String', 4)
print(tuple_two)                            # ('Alpha', 'Bravo', (1, 0))
print(tuple_two[2][1])                      # 0

# concatenate tuples
tuples = tuple_one + tuple_two
print(tuples)
# (1.0, 'String', 4, 'Alpha', 'Bravo', (1, 0))

# create tuple from a list
print(tuple([100, 'B']))
# (100, 'B')