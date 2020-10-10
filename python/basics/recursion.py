def recursive(x):
	# do something
	recursive(y)

# EXAMPLE: simple countdown
def countdown(n):
    if n <= 0:
        print("Countdown done...")
    else:
        print(n)
        countdown(n - 1)

countdown(5)
# 5
# 4
# 3
# 2
# 1
# Done.