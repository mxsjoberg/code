# 2023-08

import ast

program = """
x = 5
y = 10
z = x + y * 2
print(z)
"""

variables = {}

tree = ast.parse(program)
# print(len(ast.dump(tree)))
# 449

folded_tree = ast.Module(body=[], type_ignores=[])

# walk ast
for node in ast.walk(tree):
    if isinstance(node, ast.Assign):
        if isinstance(node.targets[0], ast.Name):
            if isinstance(node.value, ast.Num):
                variables[node.targets[0].id] = node.value.n
            else:
                folded_tree.body.append(node)
    if isinstance(node, ast.BinOp):
        if isinstance(node.left, ast.Name) and node.left.id in variables:
            node.left = ast.Num(n=variables[node.left.id])
        elif isinstance(node.right, ast.Name) and node.right.id in variables:
            node.right = ast.Num(n=variables[node.right.id])
        else:
            folded_tree.body.append(node)
    if isinstance(node, ast.Expr):
        folded_tree.body.append(node)

# print(variables)
# print(ast.dump(folded_tree))
# print(len(ast.dump(folded_tree)))
# 295

# fix missing locations
ast.fix_missing_locations(folded_tree)

# compile and execute folded tree
exec(compile(folded_tree, filename="<ast>", mode="exec"))
# 25