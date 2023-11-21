import sys
import datetime
import pprint
print(sys.version)
# 2.7.13 (default, Sep 30 2017, 13:16:00) 

# initialise database
#
# hive > CREATE DATABASE log_db;
# hive > USE log_db;
# hive > CREATE TABLE logs (user String, time String, query String) ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t' LINES TERMINATED BY '\n' STORED AS TEXTFILE;
# hive > LOAD DATA LOCAL INPATH 'hive/query_logs.txt' OVERWRITE INTO TABLE logs;

# pyhive
from pyhive import hive

#cursor = hive.connect('localhost').cursor()
cursor = hive.connect('localhost', port=10000, auth='KERBEROS', kerberos_service_name='hive')
cursor.execute('SHOW TABLES')
cursor.fetchall()


# cursor.execute('SELECT * FROM logs LIMIT 10')

# print (cursor.fetchall())

'''
Michael Sjoeberg
2020-05-13
https://github.com/michaelsjoeberg/python-playground/blob/master/data-science/apache-hive.py
'''