import re

text = "some random text to test regular expressions on"
date = "2017-07-16"

# create a pattern to match (e.g. four letter word ending with 'st')
pattern_text = '..st'

# compile pattern
pattern = re.compile(pattern_text)

# search for pattern in text
re_search = re.search(pattern, text)
if (re_search): print(re_search.group())
# test

# separate text at whitespace
print(re.split(' ', text))
# ['some', 'random', 'text', 'to', 'test', 'regular', 'expressions', 'on']

# separate date at dash
print(re.split('-', date))
# ['2017', '07', '16']

# substitute word in text
print(re.sub('text', 'string', text, 1))
# some random string to test regular expressions on

# match regular expression
re_match = re.match("20[01][0-9].*[0-9][0-9].*[0-9][0-9]", date)

print(re_match == None)                     # False
print(re_match.pos)                         # 0