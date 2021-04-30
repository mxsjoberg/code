# create file
with open('test.txt', 'w') as file:
    pass

# read from file
with open('test.txt', 'r') as file:
    file.read()

# or
content = open('test.txt', 'r').read()

# read lines
with open('test.txt', 'r') as file:
    for line in file.readlines():
        # do something
        pass

# write to file
with open('test.txt', 'w') as file:
    file.write('This is some text to write.')