import re

text = "some random text to test regular expressions on"
date = "2017-07-16"

# create a pattern to match (a four letter word ending with 'st')
pattern_text = '..st'

# compile pattern
pattern = re.compile(pattern_text)

# search for pattern in text
re_search = re.search(pattern, text)
if (re_search):
    re_search.group()                   # test

# separate text at whitespace
text_split = re.split(' ', text)
text_split                              # ['some', 'random', 'text', 'to', 'test', 'regular', 'expressions', 'on']

# separate date at dash
date_split = re.split('-', date)
date_split                              # ['2017', '07', '16']

# substitute word in text
re_substitute = re.sub('text', 'string', text, 1)
re_substitute                           # some random string to test regular expressions on

# match regular expression
re_match = re.match("20[01][0-9].*[0-9][0-9].*[0-9][0-9]", date)
re_match == None                        # False
re_match.pos                            # 0