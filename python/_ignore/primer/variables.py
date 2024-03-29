# 2018-06

x = 6
y = "String"
z = 1.05
a = x

print(type(x))
# <class 'int'>
print(type(y))
# <class 'str'>
print(type(z))
# <class 'float'>
print(type(a))
# <class 'int'>

x = a = 6
y, z = "String", 1.05

print(x, y, z, a)
# 6 String 1.05 6

# list assignment
d, t, v = [230, 45, 12]
print(d, t, v)
# 230 45 12

# string assignment
a, b, c, d = "100B"
print(a, b, c, d)
# 1 0 0 B

string = "100B"
print(string[:3])
# 100
print(string[3:])
# B

# delete
del x
print(x)
# NameError: name 'x' is not defined