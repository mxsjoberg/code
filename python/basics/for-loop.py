numbers = [1, 2, 3, 4]

for number in numbers:
    # do something

# nested
for i in range(10):
    for j in range(10):
        # do something

# iterating dictionaries
dict = {'Alpha': 1, 'Beta': 2}

for key in dict.keys():
    print (key)                     # Alpha Beta

for value in dict.values():
    print (value)                   # 1 2

for key, value in dict.items():
    print (key, value)              # ('Alpha', 1) ('Beta', 2)

'''
Michael Sjoeberg
2018-11-05
https://github.com/michaelsjoeberg/python-playground/blob/master/basics/for-loop.py
'''