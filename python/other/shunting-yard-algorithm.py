# https://en.wikipedia.org/wiki/Shunting_yard_algorithm
INPUT = "3 + 4 * 2 / (1 - 5) ^2 ^3"

output = []
operator = []

precedence = { '^': 2, '/': 1, '*': 1, '+': 0, '-': 0 }

# read input
for char in list(INPUT):
	# whitespace
	if char.isspace():
		pass
	# number
	if char.isnumeric():
		output.append(char)
	# operator
	if char in ['+', '-', '*', '/', '^']:
		# precedence
		while len(operator) > 0:
			op = operator.pop()
			if op != '(' and (op != '^' and precedence[op] >= precedence[char]):
				output.append(op)
			else:
				# break
				operator.append(op)
				break
		operator.append(char)
	# left parenthesis
	if char == '(':
		operator.append(char)
	# right parenthesis
	if char == ')':
		if '(' not in operator: print("Error: Mismatched parentheses")
		while len(operator) > 0:
			op = operator.pop()
			if op != '(':
				output.append(op)
			else:
				break

# pop operators
while len(operator) > 0:
	output.append(operator.pop())

print(' '.join(output))
# 3 4 2 * 1 5 - 2 3 ^ ^ / +