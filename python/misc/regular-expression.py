import re

text = "some random text to test regular expressions"
date = "2017-07-16"

# create pattern -> four letter word ending with "st"
pattern_text = "..st"
pattern = re.compile(pattern_text)

# search for pattern in text
re_search = re.search(pattern, text)
if (re_search):
	print(re_search.group())
	# test

# separate text
print(re.split(pattern, text))
# ['some random text to ', ' regular expressions']

# substitute word in text
print(re.sub(pattern, "learn", text, 1))
# some random text to learn regular expressions

# match
print(re.match("20[01][0-9].*[0-9][0-9].*[0-9][0-9]", date) != None)
# True