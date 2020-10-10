from itertools import combinations_with_replacement

lst = ['A', 'B', 'C']               # ['A', 'B', 'C']
combinations = []                   # []


# for each item in list
for item in list(range(len(lst))):
    # append combination to combinations list
    combinations.append(list(combinations_with_replacement(lst, item + 1)))

# [[('A',), ('B',), ('C',)],
#  [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')],
#  [('A', 'A', 'A'), ('A', 'A', 'B'), ('A', 'A', 'C'), ('A', 'B', 'B'), ('A', 'B', 'C'), ('A', 'C', 'C'), ('B', 'B', 'B'), ('B', 'B', 'C'), ('B', 'C', 'C'), ('C', 'C', 'C')]]

# flatten list of lists
combinations = [item for row in combinations for item in row]

# [('A',), ('B',), ('C',), 
#  ('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C'),
#  ('A', 'A', 'A'), ('A', 'A', 'B'), ('A', 'A', 'C'), ('A', 'B', 'B'), ('A', 'B', 'C'), ('A', 'C', 'C'), ('B', 'B', 'B'), ('B', 'B', 'C'), ('B', 'C', 'C'), ('C', 'C', 'C')]

'''
Michael Sjoeberg
2018-11-05
https://github.com/michaelsjoeberg/python-playground/blob/master/data-science/combinations.py
'''