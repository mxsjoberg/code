# 2018-06

try:
    x = 1 / 0 # ops!

except ZeroDivisionError:
    print("error: cannot divide by zero")
    # do something
    pass

# general exception

except Exception as e:
    print(f"error: ${e}")
    # do something
    pass

finally:
    # do something
    pass