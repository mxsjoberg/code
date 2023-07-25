def simplify_parse_tree(tree):
    if (isinstance(tree, tuple)):
        # first value in tuple, remaining values in tuple
        operator, *operands = tree
        operands = [simplify_parse_tree(operand) for operand in operands]

        if all(isinstance(operand, int) for operand in operands):
            if operator == '+':
                return sum(operands)
            elif operator == '*':
                return eval('*'.join(map(str, operands)))

    return tree

# (1 + 2) * (3 + 4)
parse_tree = ('*', ('+', 1, 2), ('+', 3, 4))
print(simplify_parse_tree(parse_tree))
# 21

compiled = compile('(1 + 2) * (3 + 4)', '<string>', 'eval')
print(compiled.co_consts[0])
# 21

assert simplify_parse_tree(parse_tree) == compiled.co_consts[0]
