import sys
import datetime
import pprint
#print(sys.version)
# 3.8.1 (default, Jan  8 2020, 16:15:59) 

# pymongo
import pymongo
#print(pymongo.version)
# 3.10.1

# NOTE: initiate mongodb database
#   $ mkdir mongodb; cd mongodb
#   $ mkdir -p data/db
#   $ mongod --dbpath=./data/db

# NOTE: import dataset (require running mongod instance)
#   $ mongoimport --db test --collection restaurants --drop --file mongodb.json

# client = MongoClient('localhost', 27017)
client = pymongo.MongoClient('mongodb://localhost:27017/')
print(client)
# MongoClient(host=['localhost:27017'], document_class=dict, tz_aware=False, connect=True)

# show databases
print(client.list_database_names())
# ['admin', 'config', 'local', 'test']

# select database
db = client.test
# db = client['test']

# show collections
print(db.list_collection_names())
# ['restaurants']

# select collection
collection = db.restaurants
# collection = db['restaurants']

# count documents in collection
print(collection.count_documents({}))
# 25359

# show documents in collection (note: limit large collections)
for document in collection.find().limit(10): pprint.pprint(document)
# {'_id': ObjectId('5ebbd5be7e882f638d7a46f9'),
#  'address': {'building': '203',
#              'coord': [-73.97822040000001, 40.6435254],
#              'street': 'Church Avenue',
#              'zipcode': '11218'},
#  'borough': 'Brooklyn',
#  'cuisine': 'Ice Cream, Gelato, Yogurt, Ices',
#  'grades': [{'date': datetime.datetime(2014, 2, 10, 0, 0),
#              'grade': 'A',
#              'score': 2},
#             {'date': datetime.datetime(2013, 1, 2, 0, 0),
#              'grade': 'A',
#              'score': 13},
#             {'date': datetime.datetime(2012, 1, 9, 0, 0),
#              'grade': 'A',
#              'score': 3},
#             {'date': datetime.datetime(2011, 11, 7, 0, 0),
#              'grade': 'P',
#              'score': 12},
#             {'date': datetime.datetime(2011, 7, 21, 0, 0),
#              'grade': 'A',
#              'score': 13}],
#  'name': 'Carvel Ice Cream',
#  'restaurant_id': '40360076'}
# ...

# delete duplicates
collection.delete_many({ "restaurant_id": "41704620" })

# insert document into collection
collection.insert_one({
    "address": {
        "street": "2 Avenue",
        "zipcode": "10075",
        "building": "1480",
        "coord": [ -73.9557413, 40.7720266 ]
    },
    "borough": "Manhattan",
    "cuisine": "Italian",
    "grades": [
        {
            "date": datetime.datetime(2014, 10, 1, 0, 0),
            "grade": "A",
            "score": 11
        }, {
            "date": datetime.datetime(2014, 1, 16, 0, 0),
            "grade": "B",
            "score": 17
        }
    ],
    "name": "Vella",
    "restaurant_id": "41704620"
})

# print(collection.find({ "restaurant_id": "41704620" }).count())
pprint.pprint(collection.find_one({ "restaurant_id": "41704620" }))
# {'_id': ObjectId('5ebbdfd6833677f47e1bdbb3'),
#  'address': {'building': '1480',
#              'coord': [-73.9557413, 40.7720266],
#              'street': '2 Avenue',
#              'zipcode': '10075'},
#  'borough': 'Manhattan',
#  'cuisine': 'Italian',
#  'grades': [{'date': datetime.datetime(2014, 10, 1, 0, 0),
#              'grade': 'A',
#              'score': 11},
#             {'date': datetime.datetime(2014, 1, 16, 0, 0),
#              'grade': 'B',
#              'score': 17}],
#  'name': 'Vella',
#  'restaurant_id': '41704620'}

# counting documents
print(collection.count_documents({ "address.zipcode": "10005", "cuisine": "Italian" }))
# 3

# logical operators
print(collection.count_documents({ "$and": [{ "address.zipcode": "10005" }, { "cuisine": "Italian" }] }))
# 3

print(collection.count_documents({ "$or": [{ "address.zipcode": "10005" }, { "cuisine": "Italian" }] }))
# 1135

print(collection.count_documents({ "$and": [{ "address.zipcode": "10005" }, { "cuisine": { "$ne": "Italian" } }] }))
# 66

# sorting documents (note: prejecting name only)
q_sorted = collection.find({ "address.zipcode": "10005", "cuisine": "Italian" }, { "name": 1 }).sort([ ("name", 1) ])
for document in q_sorted.limit(2): pprint.pprint(document)
# {'_id': ObjectId('5ebbd5be7e882f638d7a6522'), 'name': 'Cipriani Club 55'}
# {'_id': ObjectId('5ebbd5be7e882f638d7a9032'), 'name': "Dave'S Hoagies"}

# query selectors (note: projecting name and grades.score only)
q_selected = collection.find({ "grades": { "$elemMatch": { "score": { "$gt": 80 } } }}, { "name": 1, "grades.score": 1 })
for document in q_selected.limit(2): pprint.pprint(document)
# {'_id': ObjectId('5ebbd5be7e882f638d7a485a'),
#  'grades': [{'score': 11},
#             {'score': 131},
#             {'score': 11},
#             {'score': 25},
#             {'score': 11},
#             {'score': 13}],
#  'name': "Murals On 54/Randolphs'S"}
# {'_id': ObjectId('5ebbd5be7e882f638d7a48f9'),
#  'grades': [{'score': 5},
#             {'score': 8},
#             {'score': 12},
#             {'score': 2},
#             {'score': 9},
#             {'score': 92},
#             {'score': 41}],
#  'name': 'Gandhi'}

# updating documents
collection.update({ "name": "Juniors", "restaurant_id": "40719736" }, { "$set": { "restaurant_id": "10" } })
pprint.pprint(collection.find_one({ "name": "Juniors" }))
# {'_id': ObjectId('5ebbd5be7e882f638d7a51b0'),
#  'address': {'building': '',
#              'coord': [-73.97705599999999, 40.752998],
#              'street': 'Grand Central Terminal',
#              'zipcode': '10017'},
#  'borough': 'Manhattan',
#  'cuisine': 'American',
#  'grades': [{'date': datetime.datetime(2014, 6, 16, 0, 0),
#              'grade': 'A',
#              'score': 9},
#             {'date': datetime.datetime(2014, 2, 21, 0, 0),
#              'grade': 'B',
#              'score': 18},
#             {'date': datetime.datetime(2013, 1, 23, 0, 0),
#              'grade': 'A',
#              'score': 5},
#             {'date': datetime.datetime(2012, 8, 20, 0, 0),
#              'grade': 'B',
#              'score': 21},
#             {'date': datetime.datetime(2011, 8, 25, 0, 0),
#              'grade': 'A',
#              'score': 10}],
#  'name': 'Juniors',
#  'restaurant_id': '10'}

# aggregate
q_aggregate = collection.aggregate([{ "$group": { "_id": "$borough", "count": { "$sum": 1} } }])
for document in q_aggregate: pprint.pprint(document)
# {'_id': 'Missing', 'count': 51}
# {'_id': 'Staten Island', 'count': 969}
# {'_id': 'Manhattan', 'count': 10259}
# {'_id': 'Bronx', 'count': 2338}
# {'_id': 'Queens', 'count': 5656}
# {'_id': 'Brooklyn', 'count': 6086}

# explain
pprint.pprint(collection.find({ "grades.score": { "$gt": 90} }, { "grades.score": 1 }).explain())