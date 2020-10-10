from datetime import datetime
from datetime import timedelta

now = datetime.now()            # 2018-06-15 18:23:51.500993
future = now + timedelta(12)    # 2018-06-27 18:23:59.351647

now.year                        # 2018
now.month                       # 6
now.day                         # 15
now.hour                        # 18
now.minute                      # 23

# difference between dates
difference = future - now

difference                      # 12 days, 0:00:00
difference.days                 # 12

'''
Michael Sjoeberg
2018-11-05
https://github.com/michaelsjoeberg/python-playground/blob/master/basics/datetime.py
'''