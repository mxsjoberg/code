# https://bitbucket.org/xmonader/pybloomfilter/src/default/
import sys
import datetime
import pprint
print(sys.version)
# 2.7.13 (default, Sep 30 2017, 13:16:00) 

# pybloomfilter
from pybloomfilter import BloomFilter

bf = BloomFilter(6000, 0.01)

first_words = []

with open("bloomfilter/spam_websites.txt") as file:
	for word in file:
		if (len(first_words) < 514):
			first_words.append(word.strip())
		else:
			bf.add(str.encode(word.strip()))

for word in first_words:
	if (str.encode(word) in bf):
		print(('{} : false positive').format(word))

'''
Michael Sjoeberg
2020-05-13
https://github.com/michaelsjoeberg/python-playground/blob/master/data-science/bloomfilter.py
'''