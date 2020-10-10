# read from file
with open('path/to/file', 'r') as file:
    file.read()

# or
content = open('path/to/file', 'r').read()

# read lines
with open('path/to/file.txt', 'r') as file:
    for line in file.readlines():
        # do something

# write to file
with open('path/to/file.txt', 'w') as file:
    file.write('This is some text to write.')