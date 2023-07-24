# sets are unordered collections
my_set = {1.0, 10, "String", (1, 0, 1, 0)}

print(my_set)
# {'String', 1.0, 10, (1, 0, 1, 0)}
print("String" in my_set)
# True

# add
my_set.add("Python")
print(my_set)
# {1.0, 'String', 10, (1, 0, 1, 0), 'Python'}

# remove
my_set.remove("String")
print(my_set)
# {1.0, 10, (1, 0, 1, 0), 'Python'}

# set operations
set_one = {1, 2, 3}
set_two = {3, 4, 5}

# union
print(set_one | set_two)
# {1, 2, 3, 4, 5}

# Intersection
print(set_one & set_two)
# {3}

# Difference
print(set_one - set_two)
# {1, 2}

# Symmetric difference
print(set_one ^ set_two)
# {1, 2, 4, 5}

# subset and superset
set_a = {1, 2}
set_b = {1, 2}
set_c = {1, 2, 3, 4, 5}

# Strict subset
print(set_a < set_b)
# False

# Subset
print(set_a <= set_b)
# True
