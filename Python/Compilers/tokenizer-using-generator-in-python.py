import re

token_pattern = r'[a-zA-Z_][a-zA-Z0-9_]*|\d+|<=|>=|==|!=|[<>]=?|=|[+\-*/;(){}]'

tokens = {
    'if': 'IF',
    'else': 'ELSE',
    'number': 'NUM',
    'identifier': 'ID',
    'assignment': 'ASSIGN',
    'operator': 'OP',
    'unknown': '?',
}

# tokenize
def tokenize(code):
    for match in re.findall(token_pattern, code):
        # yield to return generator (lazy evaluation)
        if tokens.get(match):       yield (tokens[match], match)
        elif match.isdigit():       yield (tokens['number'], match)
        elif match.isidentifier():  yield (tokens['identifier'], match)
        elif match in '=':          yield (tokens['assignment'], match)
        elif match in '+-*/<>':     yield (tokens['operator'], match)
        elif match in '()/{/};':    pass
        else:                       yield (tokens['unknown'], match)

code = """if (x < 10) { x = x + 1; }"""

for token in tokenize(code): print(token)
# ('IF', 'if')
# ('ID', 'x')
# ('OP', '<')
# ('NUM', '10')
# ('ID', 'x')
# ('ASSIGN', '=')
# ('ID', 'x')
# ('OP', '+')
# ('NUM', '1')