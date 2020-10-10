import sys
import datetime
import pprint
print(sys.version)
# 2.7.13 (default, Sep 30 2017, 13:16:00) 

# pyspark
from pyspark import SparkContext
sc = SparkContext('local', 'pyspark')
print(sc.version)
# 2.1.2

# NOTE: create output file for large outputs
#   $ python apache-spark.py > apache-spark.out

# creating RDD
fs = sc.textFile("spark/u.user")
# print(fs.count())
# 943

# show all
# print(fs.collect())

# create sample
sample = fs.takeSample(True, 5)
# print(sample)
# [u'540|28|M|engineer|91201', u'930|28|F|scientist|07310', u'736|48|F|writer|94618', u'172|55|M|marketing|22207', u'486|39|M|educator|93101']

fs_sample = sc.parallelize(sample)
# print(fs_sample.count())
# 5

# save to file
# fs_sample.saveAsTextFile("spark/fs_sample")

# apply functions to data
# -----------------------------------------------------------
def print_all(x): print(x)
fs_sample.foreach(print_all)
# 702|37|M|other|89104
# 621|17|M|student|60402
# 62|27|F|administrator|97214
# 698|28|F|programmer|06906
# 521|19|M|student|02146

def print_id(x): print(x.split('|')[0])
fs_sample.foreach(print_id)
# 506
# 10
# 889
# 798
# 561

# using parallelize to create samples before applying functions
sc.parallelize(fs.takeOrdered(5)).foreach(print_id)
# 100
# 101
# 102
# 103
# 104

# using lambda to filter
fs_student = fs.filter(lambda x: "student" in x)
# print(fs_student.count())
# 196

# transformations
# -----------------------------------------------------------
fs_numbers = sc.parallelize([1, 2, 3, 4, 5])
# print(fs_numbers.collect())
# [1, 2, 3, 4, 5]

fs_powers = fs_numbers.map(lambda x: x*x*x)
# print(fs_powers.collect())
# [1, 8, 27, 64, 125]

fs_combined = fs_numbers.filter(lambda x: x >= 4).map(lambda x: x*x*x)
# print(fs_combined.collect())
# [64, 125]

fs_words = sc.parallelize(["this is first", "this is second"]).flatMap(lambda x: x.split(" "))
# print(fs_words.collect())
# ['this', 'is', 'first', 'this', 'is', 'second']

# union
print(fs_numbers.union(sc.parallelize([3, 4, 5, 6, 7])).distinct().collect())
# [2, 4, 6, 1, 3, 5, 7]

# intersection
print(fs_numbers.intersection(sc.parallelize([3, 4, 5, 6, 7])).distinct().collect())
# [4, 3, 5]

# cartesian
print(fs_numbers.cartesian(sc.parallelize([1, 2])).collect())
# [(1, 1), (1, 2), (2, 1), (2, 2), (3, 1), (3, 2), (4, 1), (4, 2), (5, 1), (5, 2)]