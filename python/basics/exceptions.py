try:
    pass
    # do something

except ZeroDivisionError:
    print('Cannot divide by zero.')
    # do something

except Exception as e:
    print('Error: ' + str(e))
    # do something

finally:
    pass
    # do something