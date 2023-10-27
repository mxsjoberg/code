lst_one = ['REMOVE', 'RANDOM']
lst_two = [200, -2, [1.0, 0.0]]

# lists are mutable
lst_one[0] = 'ADD'

print(lst_one)                      # ['ADD', 'RANDOM']
print(lst_one[1])                   # RANDOM

# length of list
print(len(lst_one))                 # 2
print(len(lst_two))                 # 3

# concatenate lists
lst = lst_one + lst_two
print(lst)
# ['ADD', 'RANDOM', 200, -2, [1.0, 0.0]]

# list operations
lst.append('NULL')
print(lst)
# ['ADD', 'RANDOM', 200, -2, [1.0, 0.0], 'NULL']

# convert to string before sorting (Python 3)
print(sorted(list(map(str,lst))))
# ['-2', '200', 'ADD', 'NULL', 'RANDOM', '[1.0, 0.0]']

# create list from a string
print(list('100B'))
# ['1', '0', '0', 'B']