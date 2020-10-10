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