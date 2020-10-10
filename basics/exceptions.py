try:
    # do something

except ZeroDivisionError:
    print ('Cannot divide with zero.')
    # do something

except Exception as e:
    print ('Error: ' + str(e))
    # do something

finally:
    # do something

'''
Michael Sjoeberg
2018-11-05
https://github.com/michaelsjoeberg/python-playground/blob/master/basics/exceptions.py
'''