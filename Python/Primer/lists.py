# 2018-06

lst_one = ["remove", "random"]
lst_two = [200, -2, [1.0, 0.0]]

# lists are mutable
lst_one[0] = "ADD"

print(lst_one)
# ['ADD', 'RANDOM']
print(lst_one[1])
# RANDOM

# length
print(len(lst_one))
# 2

# concatenate
lst = lst_one + lst_two
print(lst)
# ['ADD', 'RANDOM', 200, -2, [1.0, 0.0]]

# append
lst.append(None)
print(lst)
# ['ADD', 'random', 200, -2, [1.0, 0.0], None]

# convert to string before sorting
print(sorted(list(map(str,lst))))
# ['-2', '200', 'ADD', 'None', '[1.0, 0.0]', 'random']

# string to list
print(list("100B"))
# ['1', '0', '0', 'B']