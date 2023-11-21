"""
This is how to design and use embedded
domain-specific languages in Python.
"""

import sys

"""
functions
    add     : sum all arguments
    sub     : subtract tail from head
types
    int
    float
arguments
    out     : stdin to use previous output as input
            : stdout to print
"""
program = """
Module add 1 2 3 type=float out=stdin
Module sub stdin 1 2 type=int out=stdout
"""

# Module definition
class Module:
    # Add function
    def add(*args, **kwargs):
        type_ = globals()["__builtins__"].getattr(globals()["__builtins__"], kwargs["type"])
        return sum(map(type_, args))
    # Sub function
    def sub(*args, **kwargs):
        type_ = globals()["__builtins__"].getattr(globals()["__builtins__"], kwargs["type"])
        return float(args[0]) if type_ == 'float' else int(args[0]) - sum(map(type_, args[1:]))

def get_args(tokens, STDIN):
    args = []
    kwargs = {}
    for token in tokens:
        # kwargs
        if '=' in token:
            k, v = token.split('=', 1)
            kwargs[k] = v
        # args
        else:
            # replace stdin with previous output
            if token == "stdin":
                if STDIN != "": args.append(STDIN)
                else: raise Exception("no previous output")
            else:
                args.append(token)
    return args, kwargs

def interpret(program):
    STDIN = ""
    lines = [line for line in program.splitlines() if line]
    # print(lines)
    # ['Module add 1 2 3 type=float out=stdin', 'Module sub stdin 1 2 type=int out=stdout']

    for line in lines:
        tokens = line.split()
        args, kwargs = get_args(tokens[2:], STDIN)

        # print(args, kwargs)
        # ['1', '2', '3'] {'type': 'float', 'out': 'stdin'}
        # [6.0, '1', '2'] {'type': 'int', 'out': 'stdout'}

        # print(getattr(sys.modules[__name__], tokens[0]))
        # <class '__main__.Module'>
        # <class '__main__.Module'>

        # print(getattr(getattr(sys.modules[__name__], tokens[0]), tokens[1]))
        # <function Module.add at 0x1024545e0>
        # <function Module.sub at 0x108ed9620>

        result = getattr(getattr(sys.modules[__name__], tokens[0]), tokens[1])(*args, **kwargs)
        if "out" in kwargs:
            if kwargs["out"] == "stdin": STDIN = result
            if kwargs["out"] == "stdout": print(result)

interpret(program) # 3