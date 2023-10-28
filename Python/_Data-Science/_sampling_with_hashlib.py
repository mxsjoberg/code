import sys
import datetime
import pprint
print(sys.version)
# 3.8.2 (default, May  6 2020, 02:49:43)

# hashlib
import hashlib

logs = (
	('brad', 'event a', 2),
	('charlie', 'event a', 3),
	('charlie', 'event a', 4),
	('brad', 'event b', 5),
	('brad', 'event c', 6),
	('maria', 'event a', 7),
	('maria', 'event a', 7),
	('maria', 'event a', 7),
	('roger', 'event a', 7),
	('roger', 'event b', 8),
	('alan', 'event c', 0),
	('alan', 'event b', 1),
	('boris', 'event b', 1),
	('cornelius', 'event b', 1),
	('dragan', 'event b', 1),
	('elaine', 'event b', 1),
	('elaine', 'event b', 1)
)

sample = []
buckets = 3
alpha = 2

# index of event type in item (note: second element)
key_id = 1

for i in range(len(logs)):
	hash_id = int(hashlib.sha1(logs[i][key_id].encode('utf-8')).hexdigest(), 16) % buckets

	# collisions
	#print(('id: {}; hash(id): {}').format(logs[i][key_id], hash_id))

	if (hash_id < alpha): sample.append((hash_id, logs[i]))

pprint.pprint(sample)
# [(0, ('brad', 'event a', 2)),
#  (0, ('charlie', 'event a', 3)),
#  (0, ('charlie', 'event a', 4)),
#  (1, ('brad', 'event b', 5)),
#  (0, ('maria', 'event a', 7)),
#  (0, ('maria', 'event a', 7)),
#  (0, ('maria', 'event a', 7)),
#  (0, ('roger', 'event a', 7)),
#  (1, ('roger', 'event b', 8)),
#  (1, ('alan', 'event b', 1)),
#  (1, ('boris', 'event b', 1)),
#  (1, ('cornelius', 'event b', 1)),
#  (1, ('dragan', 'event b', 1)),
#  (1, ('elaine', 'event b', 1)),
#  (1, ('elaine', 'event b', 1))]

'''
Michael Sjoeberg
2020-05-13
https://github.com/michaelsjoeberg/python-playground/blob/master/data-science/sampling_with_hashlib.py
'''