# single assignment
x = 6
y = 'String'
z = 1.05
a = x

x, y, z, a                  # (6, 'String', 1.05, 6)

# types
type(x)                     # int
type(y)                     # str
type(z)                     # float
type(a)                     # int

# multiple assignment
x = a = 6
y, z = 'String', 1.05

x, y, z, a                  # (6, 'String', 1.05, 6)

# list assignment
d, t, v = [230, 45, 12]     # (230, 45, 12)

# string assignment
a, b, c, d = '100B'         # ('1', '0', '0', 'B')

# or
string = '100B'
number = string[:3]
letter = string[3:]
number, letter              # ('100', 'B')

# delete a variable
del n
n                           # NameError: name 'n' is not defined