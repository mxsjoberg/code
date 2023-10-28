# 2018-06

numbers = [1, 2, 3, 4]

for number in numbers:
    # do something
    pass

# nested
for i in range(10):
    for j in range(10):
        # do something
        pass

# iterating dictionaries
dict = { 'a': 1, 'b': 2 }

for key in dict.keys(): print(key)
# a
# b

for value in dict.values(): print(value)
# 1
# 2

for key, value in dict.items(): print(key, value)
# a 1
# b 2

# while

x = 0
while (x < 10):
    # do something
    x += 1

print(x)
# 10