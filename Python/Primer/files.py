# 2018-06

# write to file
with open("_file.txt", "w") as file:
    file.write("this is some text to write\nanother line")

# read from file
text = ""
with open("_file.txt", "r") as file:
    text = file.read()

# or
text = open("_file.txt", "r").read()
print(text)
# this is some text to write
# another line

# read lines
with open("_file.txt", "r") as file:
    for line in file.readlines():
        # do something
        pass