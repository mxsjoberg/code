try:
    # do something
    pass

except ZeroDivisionError:
    print('Cannot divide by zero.')
    # do something
    pass

except Exception as e:
    print('Error: ' + str(e))
    # do something
    pass

finally:
    # do something
    pass