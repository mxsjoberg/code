# reading-log-files-with-pyspark.py
from pyspark import SparkContext

# load file
log_file = "file.txt"

# create context
sc = SparkContext("local", "app")

# create RDD
RDD = sc.textFile(log_file).cache()

# count
count = RDD.filter(lambda s: "a" in s).count()
print(('Lines with \'a\': {}').format(count))
# Lines with 'a': 2

# stop
sc.stop()