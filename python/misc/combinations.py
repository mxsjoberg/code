from itertools import combinations_with_replacement

my_list = ['A', 'B']
combinations = []

for item in list(range(len(my_list))):
    combinations.append(list(combinations_with_replacement(my_list, item + 1)))

print(combinations)
# [[('A',), ('B',)], [('A', 'A'), ('A', 'B'), ('B', 'B')]]

# flatten
combinations = [a for b in combinations for a in b]
print(combinations)
# [('A',), ('B',), ('A', 'A'), ('A', 'B'), ('B', 'B')]