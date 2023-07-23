# Shunting Yard Algorithm is a method for parsing
# mathematical expressions specified in infix
# notation

# https://en.wikipedia.org/wiki/Shunting-yard_algorithm

PRECEDENCE = { 'func': 3, '^': 2, '/': 1, '*': 1, '+': 0, '-': 0 }

def parse(input_):
    operator = []
    output = []
    tokens = list(input_)
    while len(tokens) > 0:
        char = tokens[0]
        # number
        if char.isnumeric():
            output.append(char)
        # function
        if char.isalpha():
            function = [char]
            i = 1
            while tokens[i].isalpha():
                function.append(tokens[i])
                i += 1
            operator.append(('func', ''.join(function)))
            # advance
            tokens = tokens[i - 1:]
        # operator
        if char in ['+', '-', '*', '/', '^']:
            # precedence
            while len(operator) > 0:
                op = operator.pop()
                if op[0] == 'func':
                    output.append(op[1])
                elif op not in ['(', '^'] and (op in PRECEDENCE and PRECEDENCE[op] >= PRECEDENCE[char]):
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
                if op[0] == 'func':
                    output.append(op[1])
                elif op != '(':
                    output.append(op)
                else:
                    break
        tokens = tokens[1:]
    # pop operators
    while len(operator) > 0:
        op = operator.pop()
        if op[0] == 'func':
            output.append(op[1])
        else:
            output.append(op)

    return ' '.join(output)

assert parse("3 + 4 * 2 / (1 - 5) ^2 ^3") == "3 4 2 * 1 5 - 2 3 ^ ^ / +"
assert parse("sin(max(2, 3) / 3 * pi)") == "2 3 max 3 / pi * sin"
