# https://en.wikipedia.org/wiki/Fermat%27s_Last_Theorem

# there are no positive integers a, b, and c such that a^n + b^n = c^n, for values of n grater than 2.
def check_fermat(a, b, c, n):
    if (a >= 0 and b >= 0 and c >= 0 and n > 2):
        if (a**n + b**n == c**n):
            print("Ok...")
            return True
        else:
            print(str(a**n + b**n) + " is not equal to " + str(c**n))
            return True
    else:
        print("Nope.")
        return False

check_fermat(2, 4, 6, 2)                        # Nope.
check_fermat(2, 4, 6, 8)                        # 65792 is not equal to 1679616

'''
Michael Sjoeberg
2019-09-12
https://github.com/michaelsjoeberg/python-playground/blob/master/applications/fermats-last-theorem-checker.py
'''