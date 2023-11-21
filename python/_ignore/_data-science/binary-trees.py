# https://en.wikipedia.org/wiki/Binary_tree
from blist import sorteddict

# create new b-tree
b_tree = sorteddict(first="Michael", last="Sjoeberg", birthday=[1750, 1, 1])
b_tree
# sorteddict({'birthday': [1750, 1, 1], 'first': 'Michael', 'last': 'Sjoeberg'})

# add key=value
b_tree['email'] = "michael@doolio.co"
b_tree
# sorteddict({'birthday': [1750, 1, 1], 'email': 'michael@doolio.co', 'first': 'Michael', 'last': 'Sjoeberg'})

# list keys
list(b_tree.keys())
# ['birthday', 'email', 'first', 'last']