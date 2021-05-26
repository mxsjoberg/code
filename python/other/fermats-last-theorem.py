# https://en.wikipedia.org/wiki/Fermat%27s_Last_Theorem
#
# there are no positive integers a, b, and c such that a^n + b^n = c^n, for values of n grater than 2.

def check_fermat(a, b, c, n):
    if (a >= 0 and b >= 0 and c >= 0 and n > 2):
        if (a ** n + b ** n == c ** n):
            print("This is impossible!")
            return True
        else:
            print(str(a ** n + b ** n) + " != " + str(c ** n))
            return True
    else:
        return False

check_fermat(0, 1, 2, 3)
# 1 != 8

check_fermat(2, 4, 6, 8)
# 65792 != 1679616