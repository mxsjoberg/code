from datetime import datetime
from datetime import timedelta

now = datetime.now()
print(now)
# 2018-06-15 18:23:51.500993

future = now + timedelta(12)
print(future)
# 2018-06-27 18:23:59.351647

print(now.year)
# 2018
print(now.month)
# 6
print(now.day)
# 15
print(now.hour)
# 18
print(now.minute)
# 23

# difference between dates
difference = future - now
print(difference.days)
# 12